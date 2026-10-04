from PIL import Image

src = Image.open('書道.png').convert('RGBA')
shirt = src.crop((30, 245, 960, 610))
w, h = shirt.size
cleaned = shirt.copy()

# Feathered copy from left side
left_side = shirt.crop((0, 0, w//2, h)).transpose(Image.FLIP_LEFT_RIGHT)

# For pixels where brush is (x > 580 and y < 220 and pixel isn't dark "書道")
for x in range(560, w):
    for y in range(0, min(240, h)):
        # Distance from right boundary
        # If the pixel has the brush handle color (brown/leather/wood/brass)
        p = shirt.getpixel((x, y))
        r, g, b, a = p
        # Check if brownish/golden or leather strap
        is_brush = (r > 100 and g > 60 and b < 100) or (r > 130 and g > 90 and b > 50 and (r - b) > 30) or (x > 620 and y < 160)
        if is_brush:
            src_x = w - 1 - x
            if 0 <= src_x < w:
                lp = shirt.getpixel((src_x, y))
                cleaned.putpixel((x, y), lp)

cleaned.save('assets/costumes/shodo_shirt_perfect2.png')
print('Saved shodo_shirt_perfect2')
