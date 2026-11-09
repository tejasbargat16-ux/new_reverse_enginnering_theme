import os
import urllib.request
import json

BASE_RAW = "https://raw.githubusercontent.com/morluto/rea/main/.agents/skills"
BASE_API = "https://api.github.com/repos/morluto/rea/contents/.agents/skills"

GLOBAL_SKILLS_DIR = r"C:\Users\tejas\.gemini\skills"
LOCAL_SKILLS_DIR = os.path.abspath(r".agents\skills")

def fetch_dir(api_url, local_target):
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        items = json.loads(resp.read().decode("utf-8"))
        
    for item in items:
        target_path = os.path.join(local_target, item["name"])
        if item["type"] == "dir":
            os.makedirs(target_path, exist_ok=True)
            fetch_dir(item["url"], target_path)
        elif item["type"] == "file":
            download_url = item["download_url"]
            print(f"Downloading {item['name']} -> {target_path}")
            req_file = urllib.request.Request(download_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_file) as file_resp:
                content = file_resp.read()
            with open(target_path, "wb") as f:
                f.write(content)

def main():
    print("=== Installing REA Skill from https://github.com/morluto/rea.git ===")
    
    # 1. Fetch skills list
    req = urllib.request.Request(BASE_API, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        skill_items = json.loads(resp.read().decode("utf-8"))
        
    for skill in skill_items:
        if skill["type"] != "dir":
            continue
        skill_name = skill["name"]
        print(f"\nProcessing skill: {skill_name}")
        
        # Paths for global and workspace
        global_path = os.path.join(GLOBAL_SKILLS_DIR, skill_name)
        local_path = os.path.join(LOCAL_SKILLS_DIR, skill_name)
        
        os.makedirs(global_path, exist_ok=True)
        os.makedirs(local_path, exist_ok=True)
        
        # Download into global
        fetch_dir(skill["url"], global_path)
        
        # Mirror to local workspace
        for root, dirs, files in os.walk(global_path):
            rel = os.path.relpath(root, global_path)
            dest_dir = os.path.join(local_path, rel) if rel != "." else local_path
            os.makedirs(dest_dir, exist_ok=True)
            for f in files:
                src = os.path.join(root, f)
                dst = os.path.join(dest_dir, f)
                with open(src, "rb") as sf, open(dst, "wb") as df:
                    df.write(sf.read())
                    
    print("\n=== Updating mcp_config.json with REA MCP Server ===")
    mcp_config_path = r"C:\Users\tejas\.gemini\antigravity\mcp_config.json"
    if os.path.exists(mcp_config_path):
        with open(mcp_config_path, "r", encoding="utf-8") as f:
            mcp_data = json.load(f)
    else:
        mcp_data = {"mcpServers": {}}
        
    if "mcpServers" not in mcp_data:
        mcp_data["mcpServers"] = {}
        
    mcp_data["mcpServers"]["rea"] = {
        "command": "npx",
        "args": ["-y", "rea-agents@latest", "mcp"]
    }
    
    with open(mcp_config_path, "w", encoding="utf-8") as f:
        json.dump(mcp_data, f, indent=2)
    print(f"Updated {mcp_config_path} successfully!")

if __name__ == "__main__":
    main()

