from PIL import Image, ImageDraw, ImageFont
import numpy as np
from draw_texte import justify_text

import json

def is_empty(crop):
    return 255 not in np.asarray(crop)

def update(max_width, font_size, text : str):
    
    image = Image.new('RGB', (1080, 1080))
    draw = ImageDraw.Draw(image)

    draw.rectangle([160, 240, 920, 900], fill="purple")
    
    justified_text = justify_text(text, max_width)
    font = ImageFont.truetype("SimplyMono-Bold.ttf", font_size)
    draw.text((160,220), justified_text, fill="white", font=font,  align="left")
    
    # Crop the side to determine if there is text
    rigth_crop = image.crop((921, 240, 945, 900))
    down_crop = image.crop((130, 905, 920, 930))
        
    return rigth_crop, down_crop

def get_parameters(text : str):
    
    # Initial parameters
    max_width = 50
    font_size = 60
    
    # Create the image
    image = Image.new('RGB', (1080, 1080)) 
    draw = ImageDraw.Draw(image)

    # Draw a rectangle for defining the limit
    draw.rectangle([160, 240, 920, 900], fill="white")
    
    # Insert the text initialized
    justified_text = justify_text(text, max_width)
    font = ImageFont.truetype("SimplyMono-Bold.ttf", font_size)
    draw.text((160,220), justified_text, fill="white", font=font,  align="left")
    
    # Crop the side to determine if there is text
    right_crop = image.crop((921, 240, 945, 900))
    down_crop = image.crop((130, 900, 920, 930))
    
    while(not is_empty(right_crop) or not is_empty(down_crop)):
        
        if(not is_empty(right_crop)):
            #print("Updating max_width", max_width)
            print("#", end="")
            max_width -= 1
            right_crop, down_crop = update(max_width, font_size, text)
        
        if(not is_empty(down_crop)):
            #print("Updating font_size", font_size)
            print("#", end="")
            max_width += 1
            font_size -= 1
            right_crop, down_crop = update(max_width, font_size, text)  
    
    print("")
    return max_width, font_size

         


if __name__ == "__main__":
    
    with open('response.json', 'r', encoding="utf-8") as f:
        response = f.read()
        data = response
    
    data = json.loads(data)
    signs = data.keys()
    
    for sign in signs:
        
        text = data[sign]
        text = text.upper()
        
        max_width, font_size = get_parameters(text)
        
        image = Image.open("post/{}.png".format(sign))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("SimplyMono-Bold.ttf", font_size)
        
        justified_text = justify_text(text, max_width)
        draw.text((160,220), justified_text, fill="white", font=font,  align="left")

        image.show()