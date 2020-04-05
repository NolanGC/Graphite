from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import glob, os
import random

# CONFIG - ALTER THESE VALUES
# -------------------------------------------------------------------------------------------------
offset = (350, 100) # location of top right corner of text
tilt_factor = 3 # increases random tilt
no_caps = ['h', 'q', 'z', 'w', 'v', 'l', 'u', 'k', 'y', 'x', 'w', 'l'] # font missing these capitals
rgba = (26,29,32, 230) # red, blue, green, alpha
font_name = 'GraphiteV.ttf'
background_name = 'graph.jpg'
output_name = 'sample.png'
double_space_prob = 2 # fraction (1/x) representing probability 
# -------------------------------------------------------------------------------------------------

body = ""
with open('body.txt') as fin:
    ls = fin.readlines()
    for l in ls:
        words = l.split(' ')
        for word in words:
            randomized = ''
            for c in word:
                up = random.randint(1,2) == 2
                if(up):
                    if(c not in no_caps):
                        randomized += str(c.upper())
                    else:
                        randomized += str(c.lower())
                else:
                    randomized += str(c.lower())
            double = random.randint(1,double_space_prob) == 1
            if(double):
                body += '  ' + randomized
            else:
                body += ' ' + randomized
                
image = Image.open(background_name).convert("RGBA")
text = Image.new('RGBA', image.size, (255,255,255,0))
font = ImageFont.truetype(font_name, 115)
d = ImageDraw.Draw(text)
d.text(xy=offset, text=body, fill = rgba, font=font)
tilt = random.random() * tilt_factor
slt = text.rotate(tilt, expand=1)
sx, sy = slt.size
image.paste(slt, (0,0, sx, sy), slt)
image.save(output_name)
