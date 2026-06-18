import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Characters to use
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Generate captcha text
cap = "".join(random.choice(chars) for _ in range(8))
print(cap)

# Image settings
width, height = 280, 80
background_color = (255, 255, 255)
text_color = (0, 0, 0)

# Create image
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load a font (change path if needed)
font = ImageFont.truetype("arial.ttf", 40)

# Draw text (centered)
bbox = draw.textbbox((0, 0), cap, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (width - text_width) // 2
y = (height - text_height) // 2
draw.text((x, y), cap, fill=text_color, font=font)

# Add noise lines
for _ in range(6):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    draw.line((x1, y1, x2, y2), fill=(150, 150, 150), width=2)

# Add noise dots
for _ in range(300):
    draw.point(
        (random.randint(0, width), random.randint(0, height)),
        fill=(0, 0, 0)
    )

# Blur slightly
image = image.filter(ImageFilter.GaussianBlur(1))

# Save image
image.save("captcha.png")
image.show()
