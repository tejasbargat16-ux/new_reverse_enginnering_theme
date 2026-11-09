"""
Script to generate OnePlus Nord Series folder assets for HyperOS/MIUI theme.
Designs included:
1. icons/res/drawable-xxhdpi/icon_folder.png (257x256) - Dark mode closed folder icon
2. icons/res/drawable-xxhdpi/icon_folder_light.png (257x256) - Light mode closed folder icon
3. icons/res/drawable-xxhdpi/folder_bg_grid_four_reserved.png (440x440) - Dark mode 2x2 enlarged folder
4. icons/res/drawable-xxhdpi/folder_bg_grid_four_light_reserved.png (440x440) - Light mode 2x2 enlarged folder
5. launcher/res/drawable-xxhdpi/folder_background.png (396x646) - Opened folder modal
6. launcher/res/drawable-xxhdpi/folder_content_bg_dark.png (200x200) - Opened folder content fill
7. Mirrored to nightmode and com.mi.android.globallauncher
"""

import os
import shutil
from PIL import Image, ImageDraw, ImageFilter

def create_nord_squircle_icon(w=257, h=256, is_light=False):
    scale = 2
    sw, sh = w * scale, h * scale
    pad = 8
    radius = int(min(w, h) * 0.235 * scale)
    
    img = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    
    # 1. Outer ambient cyan glow
    if not is_light:
        glow = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.rounded_rectangle(
            [pad - 4, pad - 4, sw - pad + 4, sh - pad + 4],
            radius=radius + 4,
            outline=(0, 229, 255, 50),
            width=6
        )
        glow = glow.filter(ImageFilter.GaussianBlur(radius=7))
        img = Image.alpha_composite(img, glow)
    
    # 2. Base glass body
    card = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(card)
    
    if is_light:
        fill_color = (238, 246, 250, 180)
        cdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, fill=fill_color)
        
        # Specular sheen on upper half
        sheen = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(sheen)
        sdraw.rounded_rectangle([pad + 2, pad + 2, sw - pad - 2, sh // 2], radius=radius - 2, fill=(255, 255, 255, 50))
        card = Image.alpha_composite(card, sheen)
    else:
        # Deep obsidian frosted slate
        fill_color = (15, 21, 28, 190)
        cdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, fill=fill_color)
        
        # Subtle ambient radial glow radiating from top-left (Nord Cyan)
        amb = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        adraw = ImageDraw.Draw(amb)
        max_r = int(radius * 2.2)
        for r in range(max_r, 0, -6):
            alpha = int(32 * (1.0 - r / max_r))
            adraw.ellipse([pad - 10, pad - 10, pad - 10 + r, pad - 10 + r], fill=(0, 229, 255, alpha))
        amb = amb.filter(ImageFilter.GaussianBlur(radius=8))
        card = Image.alpha_composite(card, amb)
        
        # Specular light edge catch on top rim
        spec = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        spdraw = ImageDraw.Draw(spec)
        spdraw.line([pad + radius, pad + 2, sw - pad - radius, pad + 2], fill=(255, 255, 255, 75), width=3)
        spec = spec.filter(ImageFilter.GaussianBlur(radius=1.5))
        card = Image.alpha_composite(card, spec)
        
    img = Image.alpha_composite(img, card)
    
    # 3. Nord Teal perimeter stroke
    stroke_layer = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stroke_layer)
    if is_light:
        sdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, outline=(0, 186, 199, 130), width=4)
    else:
        # Bright Nord Cyan stroke (#00E5FF)
        sdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, outline=(0, 229, 255, 120), width=4)
    
    img = Image.alpha_composite(img, stroke_layer)
    
    # Downsample using high quality Lanczos filter
    final_img = img.resize((w, h), Image.Resampling.LANCZOS)
    return final_img


def create_nord_enlarged_folder_bg(w=440, h=440, is_light=False):
    scale = 2
    sw, sh = w * scale, h * scale
    pad = 12
    radius = int(min(w, h) * 0.22 * scale)
    
    img = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    
    # Outer ambient cyan glow
    if not is_light:
        glow = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.rounded_rectangle(
            [pad - 6, pad - 6, sw - pad + 6, sh - pad + 6],
            radius=radius + 6,
            outline=(0, 229, 255, 45),
            width=8
        )
        glow = glow.filter(ImageFilter.GaussianBlur(radius=9))
        img = Image.alpha_composite(img, glow)
        
    # Base card
    card = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(card)
    
    if is_light:
        fill_color = (239, 247, 250, 185)
        cdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, fill=fill_color)
        
        sheen = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(sheen)
        sdraw.rounded_rectangle([pad + 2, pad + 2, sw - pad - 2, sh // 2], radius=radius - 2, fill=(255, 255, 255, 55))
        card = Image.alpha_composite(card, sheen)
    else:
        # Dark obsidian slate
        fill_color = (15, 20, 27, 195)
        cdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, fill=fill_color)
        
        # Soft ambient radial cyan aura in top half
        amb = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        adraw = ImageDraw.Draw(amb)
        max_r = int(sw * 0.7)
        cx = sw // 2
        for r in range(max_r, 0, -10):
            alpha = int(30 * (1.0 - r / max_r))
            adraw.ellipse([cx - r // 2, pad, cx + r // 2, pad + r], fill=(0, 229, 255, alpha))
        amb = amb.filter(ImageFilter.GaussianBlur(radius=12))
        card = Image.alpha_composite(card, amb)
        
        # Specular light edge catch on top rim
        spec = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
        spdraw = ImageDraw.Draw(spec)
        spdraw.line([pad + radius, pad + 3, sw - pad - radius, pad + 3], fill=(255, 255, 255, 80), width=4)
        spec = spec.filter(ImageFilter.GaussianBlur(radius=2))
        card = Image.alpha_composite(card, spec)
        
    img = Image.alpha_composite(img, card)
    
    # Perimeter stroke
    stroke_layer = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stroke_layer)
    if is_light:
        sdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, outline=(0, 186, 199, 135), width=5)
    else:
        sdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, outline=(0, 229, 255, 125), width=5)
        
    img = Image.alpha_composite(img, stroke_layer)
    
    final_img = img.resize((w, h), Image.Resampling.LANCZOS)
    return final_img


def create_nord_open_folder_window(w=396, h=646):
    scale = 2
    sw, sh = w * scale, h * scale
    pad = 14
    radius = int(46 * scale)
    
    img = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    
    # Outer subtle cyan glow
    glow = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.rounded_rectangle([pad - 6, pad - 6, sw - pad + 6, sh - pad + 6], radius=radius + 6, outline=(0, 229, 255, 40), width=8)
    glow = glow.filter(ImageFilter.GaussianBlur(radius=8))
    img = Image.alpha_composite(img, glow)
    
    # Base dark obsidian glass
    card = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(card)
    cdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, fill=(14, 18, 25, 225))
    
    # OnePlus Nord top accent banner (OxygenOS header ambient cyan illumination)
    header_glow = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(header_glow)
    header_height = int(150 * scale)
    for y in range(pad, pad + header_height):
        factor = 1.0 - ((y - pad) / header_height)
        alpha = int(45 * (factor ** 1.8))
        hdraw.line([pad + 4, y, sw - pad - 4, y], fill=(0, 229, 255, alpha))
        
    # Mask header glow to inside the card
    card_mask = Image.new('L', (sw, sh), 0)
    cmdraw = ImageDraw.Draw(card_mask)
    cmdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, fill=255)
    header_glow.putalpha(Image.composite(header_glow.split()[-1], Image.new('L', (sw, sh), 0), card_mask))
    card = Image.alpha_composite(card, header_glow)
    
    # Top specular reflection line
    spec = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    spdraw = ImageDraw.Draw(spec)
    spdraw.line([pad + radius, pad + 2, sw - pad - radius, pad + 2], fill=(255, 255, 255, 75), width=3)
    spec = spec.filter(ImageFilter.GaussianBlur(radius=1.5))
    card = Image.alpha_composite(card, spec)
    
    img = Image.alpha_composite(img, card)
    
    # Perimeter stroke
    stroke_layer = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stroke_layer)
    sdraw.rounded_rectangle([pad, pad, sw - pad, sh - pad], radius=radius, outline=(0, 229, 255, 110), width=4)
    
    img = Image.alpha_composite(img, stroke_layer)
    
    final_img = img.resize((w, h), Image.Resampling.LANCZOS)
    return final_img


def create_nord_folder_content_bg(w=200, h=200):
    # Frosted obsidian fill tile with subtle Nord cool tint
    img = Image.new('RGBA', (w, h), (14, 18, 25, 215))
    return img


def main():
    print("Generating OnePlus Nord folder assets...")
    
    # 1. Closed Folder Icons
    icon_folder_dark = create_nord_squircle_icon(257, 256, is_light=False)
    icon_folder_light = create_nord_squircle_icon(257, 256, is_light=True)
    
    p1 = os.path.join("icons", "res", "drawable-xxhdpi", "icon_folder.png")
    p2 = os.path.join("icons", "res", "drawable-xxhdpi", "icon_folder_light.png")
    icon_folder_dark.save(p1)
    icon_folder_light.save(p2)
    print(f"Updated: {p1}")
    print(f"Updated: {p2}")
    
    # 2. Enlarged 2x2 Big Folder Backgrounds
    bg_grid_dark = create_nord_enlarged_folder_bg(440, 440, is_light=False)
    bg_grid_light = create_nord_enlarged_folder_bg(440, 440, is_light=True)
    
    p3 = os.path.join("icons", "res", "drawable-xxhdpi", "folder_bg_grid_four_reserved.png")
    p4 = os.path.join("icons", "res", "drawable-xxhdpi", "folder_bg_grid_four_light_reserved.png")
    bg_grid_dark.save(p3)
    bg_grid_light.save(p4)
    print(f"Updated: {p3}")
    print(f"Updated: {p4}")
    
    # 3. Opened Folder Window (launcher and com.mi.android.globallauncher, day and nightmode)
    folder_bg = create_nord_open_folder_window(396, 646)
    folder_content = create_nord_folder_content_bg(200, 200)
    
    destinations = [
        os.path.join("launcher", "res", "drawable-xxhdpi"),
        os.path.join("launcher", "nightmode", "res", "drawable-xxhdpi"),
        os.path.join("com.mi.android.globallauncher", "res", "drawable-xxhdpi"),
        os.path.join("com.mi.android.globallauncher", "nightmode", "res", "drawable-xxhdpi")
    ]
    
    for d in destinations:
        os.makedirs(d, exist_ok=True)
        bg_path = os.path.join(d, "folder_background.png")
        content_path = os.path.join(d, "folder_content_bg_dark.png")
        folder_bg.save(bg_path)
        folder_content.save(content_path)
        print(f"Updated: {bg_path}")
        print(f"Updated: {content_path}")
        
    print("All OnePlus Nord folder assets generated successfully!")

if __name__ == "__main__":
    main()

