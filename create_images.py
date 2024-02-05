import json
from PIL import Image, ImageDraw, ImageFont
from get_parameters import get_parameters, justify_text
import datetime

def get_time():
    now = datetime.datetime.now()
    return str(now.year) + "_" + str(now.month) + "_" + str(now.day)

def generate_images():
    
    with open('horoscopes.json', 'r', encoding="utf-8") as f:
        response = f.read()
        data = response
    
    data = json.loads(data)
    signs = data.keys()
    
    for sign in signs:
        
        text = data[sign]
        text = text.upper()
        
        max_width, font_size = get_parameters(text)
        
        image = Image.open("templates/{}.png".format(sign))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("SimplyMono-Bold.ttf", font_size)
        
        justified_text = justify_text(text, max_width)
        draw.text((160,220), justified_text, fill="white", font=font,  align="left")

        path = "posts/{}_{}.png".format(get_time(), sign)
        image.save(path)
        
        print("Image saved: {}".format(path))
        #image.show()
        