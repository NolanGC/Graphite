from PIL import Image, ImageDraw, ImageFont
import glob, os

offset = (350, 100)
body = ""
with open('body.txt') as fin:
    ls = fin.readlines();
    for l in ls:
        body += l

image = Image.open('graph.jpg')
font_type = ImageFont.truetype('Graphite.ttf', 100)

draw = ImageDraw.Draw(image)
draw.text(xy=offset, text=body, fill = (14,17,17, 128), font=font_type)
image.save('sample.pdf')