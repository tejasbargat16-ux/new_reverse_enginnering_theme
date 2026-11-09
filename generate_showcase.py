import base64
import os

def get_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

icon_dark = get_b64('icons/res/drawable-xxhdpi/icon_folder.png')
icon_light = get_b64('icons/res/drawable-xxhdpi/icon_folder_light.png')
grid_four_dark = get_b64('icons/res/drawable-xxhdpi/folder_bg_grid_four_reserved.png')
grid_four_light = get_b64('icons/res/drawable-xxhdpi/folder_bg_grid_four_light_reserved.png')
open_bg = get_b64('launcher/res/drawable-xxhdpi/folder_background.png')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OnePlus Nord Series Folder Design</title>
    <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
    <style>
        .glow-nord {{
            box-shadow: 0 0 25px rgba(0, 229, 255, 0.35);
        }}
    </style>
</head>
<body class="bg-[#0d1117] text-gray-200 p-6 font-sans">
    <div class="max-w-4xl mx-auto space-y-8">
        <!-- Header -->
        <div class="border-b border-cyan-500/30 pb-4">
            <div class="flex items-center space-x-3">
                <span class="px-2.5 py-1 text-xs font-bold uppercase tracking-wider rounded bg-cyan-500/20 text-cyan-400 border border-cyan-500/40">OnePlus Nord Design</span>
                <span class="text-xs text-gray-400">OxygenOS Aquamorphic Aesthetics</span>
            </div>
            <h1 class="text-2xl font-bold text-white mt-2 flex items-center gap-2">
                <span class="text-cyan-400">✦</span> OnePlus Nord Series Folder UI Redesign
            </h1>
            <p class="text-sm text-gray-400 mt-1">Custom tailored for HyperOS / MIUI theme engine with Nord Cyan (#00E5FF) and frosted obsidian glass.</p>
        </div>

        <!-- Palette & Specs -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <div class="p-3 rounded-lg bg-[#161b22] border border-cyan-500/20 flex flex-col items-center">
                <div class="w-7 h-7 rounded-full bg-[#00e5ff] shadow-[0_0_10px_#00e5ff] mb-2"></div>
                <span class="font-mono font-semibold text-white">#00E5FF</span>
                <span class="text-gray-400">Nord Cyan Accent</span>
            </div>
            <div class="p-3 rounded-lg bg-[#161b22] border border-teal-500/20 flex flex-col items-center">
                <div class="w-7 h-7 rounded-full bg-[#00bac7] shadow-[0_0_10px_#00bac7] mb-2"></div>
                <span class="font-mono font-semibold text-white">#00BAC7</span>
                <span class="text-gray-400">Nord Signature Teal</span>
            </div>
            <div class="p-3 rounded-lg bg-[#161b22] border border-gray-700 flex flex-col items-center">
                <div class="w-7 h-7 rounded-full bg-[#0f151c] border border-gray-600 mb-2"></div>
                <span class="font-mono font-semibold text-white">#0F151C (75%)</span>
                <span class="text-gray-400">Obsidian Dark Glass</span>
            </div>
            <div class="p-3 rounded-lg bg-[#161b22] border border-gray-700 flex flex-col items-center">
                <div class="w-7 h-7 rounded-full bg-[#eef7fa] border border-cyan-300 mb-2"></div>
                <span class="font-mono font-semibold text-white">#EEF7FA (70%)</span>
                <span class="text-gray-400">Aquamorphic Light</span>
            </div>
        </div>

        <!-- Cards Section -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Standard Folder Icon -->
            <div class="bg-[#161b22] rounded-xl p-5 border border-cyan-500/20 flex flex-col items-center text-center">
                <h3 class="text-sm font-semibold text-white mb-1">Homescreen Folder Icon</h3>
                <p class="text-xs text-gray-400 mb-4">257×256 Squircle with Nord Glow</p>
                <div class="relative p-6 rounded-2xl bg-gradient-to-b from-[#1c232d] to-[#12161d] border border-gray-800 flex items-center justify-center min-h-[160px] w-full">
                    <img src="{icon_dark}" class="w-24 h-24 object-contain transition-transform hover:scale-105" alt="Nord Dark Folder Icon">
                </div>
                <div class="mt-3 text-left w-full space-y-1 text-xs text-gray-400">
                    <div>• <strong class="text-gray-200">Shape:</strong> OxygenOS Continuous Squircle</div>
                    <div>• <strong class="text-gray-200">Rim:</strong> Glowing #00E5FF 1.75px contour</div>
                    <div>• <strong class="text-gray-200">Fill:</strong> Frosted translucent glassmorphism</div>
                </div>
            </div>

            <!-- Enlarged Big Folder -->
            <div class="bg-[#161b22] rounded-xl p-5 border border-cyan-500/20 flex flex-col items-center text-center">
                <h3 class="text-sm font-semibold text-white mb-1">2×2 Enlarged Folder (Super Folder)</h3>
                <p class="text-xs text-gray-400 mb-4">440×440 OxygenOS Card</p>
                <div class="relative p-4 rounded-2xl bg-gradient-to-b from-[#1c232d] to-[#12161d] border border-gray-800 flex items-center justify-center min-h-[160px] w-full">
                    <img src="{grid_four_dark}" class="w-28 h-28 object-contain transition-transform hover:scale-105" alt="Enlarged Folder Dark">
                </div>
                <div class="mt-3 text-left w-full space-y-1 text-xs text-gray-400">
                    <div>• <strong class="text-gray-200">Ratio:</strong> 440×440 for 2×2 desktop grid</div>
                    <div>• <strong class="text-gray-200">Aura:</strong> Top-down Nord ambient cyan glow</div>
                    <div>• <strong class="text-gray-200">Corners:</strong> Smooth ~96px continuous radius</div>
                </div>
            </div>

            <!-- Opened Folder Window -->
            <div class="bg-[#161b22] rounded-xl p-5 border border-cyan-500/20 flex flex-col items-center text-center">
                <h3 class="text-sm font-semibold text-white mb-1">Opened Folder Modal</h3>
                <p class="text-xs text-gray-400 mb-4">396×646 Expanded View</p>
                <div class="relative p-3 rounded-2xl bg-gradient-to-b from-[#1c232d] to-[#12161d] border border-gray-800 flex items-center justify-center min-h-[160px] w-full">
                    <img src="{open_bg}" class="h-36 object-contain transition-transform hover:scale-105" alt="Nord Open Folder Background">
                </div>
                <div class="mt-3 text-left w-full space-y-1 text-xs text-gray-400">
                    <div>• <strong class="text-gray-200">Header:</strong> Nord Cyan gradient banner aura</div>
                    <div>• <strong class="text-gray-200">Fill:</strong> Deep #0E1219 at 88% alpha</div>
                    <div>• <strong class="text-gray-200">Frame:</strong> Mirrored across launcher modules</div>
                </div>
            </div>
        </div>

        <!-- Light Mode Variations -->
        <div class="bg-[#161b22] rounded-xl p-5 border border-gray-800">
            <h3 class="text-sm font-semibold text-white mb-3 flex items-center gap-2">
                <span class="text-cyan-400">☼</span> Light Mode Aquamorphic Variants
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="p-4 rounded-xl bg-gray-900 border border-gray-800 flex items-center space-x-4">
                    <img src="{icon_light}" class="w-16 h-16 object-contain" alt="Nord Light Icon">
                    <div class="text-xs">
                        <div class="font-semibold text-gray-200">icon_folder_light.png</div>
                        <div class="text-gray-400 mt-0.5">Crystalline translucent body with #00BAC7 Nord Teal border stroke.</div>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-gray-900 border border-gray-800 flex items-center space-x-4">
                    <img src="{grid_four_light}" class="w-16 h-16 object-contain" alt="Nord Light Enlarged Folder">
                    <div class="text-xs">
                        <div class="font-semibold text-gray-200">folder_bg_grid_four_light_reserved.png</div>
                        <div class="text-gray-400 mt-0.5">Crisp frosted glass 2×2 card with top specular sheen.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- File Manifest & Status -->
        <div class="bg-[#111419] rounded-xl p-4 border border-cyan-500/20 text-xs space-y-2">
            <div class="font-semibold text-cyan-400 uppercase tracking-wide">Configured & Applied Files</div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-gray-300 font-mono">
                <div>✓ icons/.../icon_folder.png</div>
                <div>✓ icons/.../icon_folder_light.png</div>
                <div>✓ icons/.../folder_bg_grid_four_reserved.png</div>
                <div>✓ icons/.../folder_bg_grid_four_light_reserved.png</div>
                <div>✓ launcher/.../folder_background.png</div>
                <div>✓ launcher/.../folder_content_bg_dark.png</div>
                <div>✓ launcher/nightmode/.../folder_*.png</div>
                <div>✓ com.mi.android.globallauncher/.../folder_*.png</div>
                <div>✓ launcher/theme_values.xml</div>
                <div>✓ launcher/nightmode/theme_values.xml</div>
                <div>✓ com.mi.android.globallauncher/theme_values.xml</div>
                <div>✓ com.mi.android.globallauncher/nightmode/theme_values.xml</div>
            </div>
        </div>
    </div>
</body>
</html>
"""

target_dir = r"C:\Users\tejas\.gemini\antigravity\brain\c9bdfec2-462c-47d2-ab8d-999e335d4174"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "nord_folder_showcase.html")
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Saved preview HTML to {target_path}")

