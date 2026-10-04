from PIL import Image

src = Image.open('書道.png').convert('RGBA')
shirt = src.crop((30, 245, 960, 610))

# Clean brush handle on upper right: x from 620 to 860, y from 0 to 180
# The brush handle is slanted. We can sample white fabric from left side or blend
w, h = shirt.size
cleaned = shirt.copy()

# Cover brush handle with clean white fabric and sumi splashes
patch = shirt.crop((120, 30, 340, 200)).transpose(Image.FLIP_LEFT_RIGHT)
# Alpha mask gradient to smoothly blend
mask = Image.new('L', patch.size, 0)
for px in range(patch.width):
    for py in range(patch.height):
        # radial or box fade
        dist = ((px - patch.width/2)**2 + (py - patch.height/2)**2)**0.5
        val = int(max(0, min(255, 255 - dist * 1.5)))
        mask.putpixel((px, py), val)

# Directly replace the brush handle area with realistic white linen + ink splashes
for x in range(580, 850):
    for y in range(0, 180):
        # sample symmetrical point from left side
        src_x = w - x
        src_y = y
        if src_x < w and src_y < h:
            pixel = shirt.getpixel((src_x, src_y))
            if pixel[3] > 0:
                cleaned.putpixel((x, y), pixel)

cleaned.save('assets/costumes/shodo_shirt_perfect.png')
print('Saved shodo_shirt_perfect')
