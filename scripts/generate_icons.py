import os
from PIL import Image, ImageOps, ImageFilter

os.makedirs('assets/costumes', exist_ok=True)

items = [
    ('hoodie', 'さかなパーカー.png'),
    ('hakama1', '袴１.png'),
    ('hakama2', '袴２.png'),
    ('black_t', '黒Tシャツ.png'),
    ('shodo', '書道.png'),
    ('sennin', '仙人.png'),
    ('ninja', '忍者.png'),
    ('samurai', '武士.png'),
]

for item_id, filename in items:
    img = Image.open(filename).convert('RGBA')
    # Crop to non-transparent bbox
    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
    else:
        cropped = img

    # Fit into 230x230 preserving aspect ratio
    w, h = cropped.size
    scale = min(230 / w, 230 / h)
    nw, nh = int(w * scale), int(h * scale)
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)

    # Place in center of 256x256 canvas
    icon = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    paste_x = (256 - nw) // 2
    paste_y = (256 - nh) // 2
    icon.paste(resized, (paste_x, paste_y), resized)

    out_path = f'assets/costumes/icon_{item_id}.png'
    icon.save(out_path)
    print(f'Generated {out_path}')

# Also generate icon_default using neko-men-icon.png or a pilot t-shirt
default_src = Image.open('assets/neko-men-icon.png').convert('RGBA')
def_icon = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
def_resized = default_src.resize((230, 230), Image.Resampling.LANCZOS)
def_icon.paste(def_resized, (13, 13), def_resized)
def_icon.save('assets/costumes/icon_default.png')
print('Generated assets/costumes/icon_default.png')
