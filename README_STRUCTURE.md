# Dark HOS3 - reverse engineered structure
Author: @HyperOSsignals (designer Mydul Islam) | platform 17 (HyperOS/MIUI) | v1.0

Backup format: MIUI BACKUP header + Android backup (uncompressed tar). Each ".mrc" = one theme module (ZIP, or a plain JPEG for wallpaper/lockscreen); ".mrm" = JSON metadata.

| Folder | Controls | Notes |
|---|---|---|
| wallpaper / lockscreen | Home + lock wallpaper | plain JPEG 1080x2400 |
| icons | App icon pack | res/drawable-xxhdpi/<package>.png, icon_mask/border/pattern, transform_config.xml (GrayScale + Edges filter) |
| launcher, com.mi.android.globallauncher | Home screen | nightmode/res: search bar, folder bg, hotseat, recents buttons (9-patch .9.png) |
| statusbar | Status bar + control center toggles | res + nightmode |
| lockstyle | Lock screen style | advance/bg: bag_*.webp, bga_*.jpg, bge*.png |
| com.android.settings | Settings UI | theme_values.xml (colors), theme_fallback.xml (drawable mapping), framework-miui-res |
| com.android.incallui, com.android.phone, contact, mms | Call/contacts/messages UI | nightmode/res PNGs |
| clock_2x4 | Clock widget | bg/t_*.png, w_*.png + manifest.xml |
| com.miui.securitycenter | Security app icons | res/drawable-xxhdpi |
| theme_metadata.json | Title, author, hash, size | |

Key ideas: "nightmode/" = dark variants; theme_values.xml overrides color names; theme_fallback.xml maps default drawable -> theme drawable; .9.png = Android nine-patch stretchable images.
Repack: zip modules back (store method for icons) as .mrc / bundle into .mtz (zip with description.xml + module zips) for MIUI Theme Editor.
