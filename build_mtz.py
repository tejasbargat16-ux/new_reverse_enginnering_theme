"""
Script to repack the extracted theme modules into a ready-to-install .mtz (MIUI Theme) package.
"""

import os
import zipfile
import io

def zip_directory_to_bytes(dir_path, compress_type=zipfile.ZIP_DEFLATED):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', compression=compress_type) as zf:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, dir_path).replace(os.sep, '/')
                zf.write(full_path, rel_path)
    return buf.getvalue()

def build_mtz(output_mtz_path="Dark_HOS3_Nord_Edition.mtz"):
    print(f"Building MTZ package: {output_mtz_path}...")
    
    description_xml = """<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<package>
    <title>Dark HOS3 Nord Edition</title>
    <author>@HyperOSsignals</author>
    <designer>Mydul Islam &amp; Tejas</designer>
    <version>1.0</version>
    <uiVersion>17</uiVersion>
    <description>Dark HOS3 with OnePlus Nord Series custom folder UI (Nord Cyan accents &amp; frosted glass).</description>
</package>
"""

    modules = [
        ("icons", zipfile.ZIP_STORED),
        ("launcher", zipfile.ZIP_DEFLATED),
        ("com.mi.android.globallauncher", zipfile.ZIP_DEFLATED),
        ("lockstyle", zipfile.ZIP_DEFLATED),
        ("statusbar", zipfile.ZIP_DEFLATED),
        ("clock_2x4", zipfile.ZIP_DEFLATED),
        ("com.android.settings", zipfile.ZIP_DEFLATED),
        ("com.android.incallui", zipfile.ZIP_DEFLATED),
        ("com.android.phone", zipfile.ZIP_DEFLATED),
        ("contact", zipfile.ZIP_DEFLATED),
        ("mms", zipfile.ZIP_DEFLATED),
        ("com.miui.securitycenter", zipfile.ZIP_DEFLATED),
        ("miui.systemui.plugin", zipfile.ZIP_DEFLATED),
    ]

    with zipfile.ZipFile(output_mtz_path, 'w', compression=zipfile.ZIP_DEFLATED) as mtz:
        # 1. description.xml
        mtz.writestr("description.xml", description_xml)
        
        # 2. Module zips
        for mod_name, comp_type in modules:
            if os.path.isdir(mod_name):
                print(f"Packing module: {mod_name}")
                mod_bytes = zip_directory_to_bytes(mod_name, comp_type)
                mtz.writestr(mod_name, mod_bytes)
        
        # 3. Wallpaper & Lockscreen
        if os.path.exists(os.path.join("wallpaper", "file.jpg")):
            print("Adding default_wallpaper.jpg")
            with open(os.path.join("wallpaper", "file.jpg"), "rb") as f:
                mtz.writestr("wallpaper/default_wallpaper.jpg", f.read())
                
        if os.path.exists(os.path.join("lockscreen", "file.jpg")):
            print("Adding default_lockscreen.jpg")
            with open(os.path.join("lockscreen", "file.jpg"), "rb") as f:
                mtz.writestr("lockscreen/default_lockscreen.jpg", f.read())

    print(f"Successfully generated: {output_mtz_path} ({os.path.getsize(output_mtz_path) / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    build_mtz()

