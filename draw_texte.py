import textwrap
from PIL import Image, ImageDraw, ImageFont
import json

def justify_text(text, max_width):
    # Formater le texte en paragraphes de largeur fixe avec des espaces justifiés
    formatted_text = textwrap.fill(text, width=max_width)

    # Ajouter des espaces supplémentaires pour justifier le texte
    justified_text = ""
    for line in formatted_text.split('\n'):
        words = line.split()
        num_words = len(words)
        if num_words > 1:
            # Calculer le nombre total d'espaces à ajouter
            total_spaces = max_width - sum(len(word) for word in words)
            # Calculer le nombre d'espaces à ajouter entre chaque mot
            extra_spaces = total_spaces // (num_words - 1)
            # Calculer le nombre d'espaces supplémentaires à ajouter
            remaining_spaces = total_spaces % (num_words - 1)
            # Construire la ligne justifiée
            justified_line = ""
            for i, word in enumerate(words[:-1]):
                justified_line += word + ' ' * extra_spaces
                if i < remaining_spaces:
                    justified_line += ' '
            justified_line += words[-1]
        else:
            # Pour une seule mot dans la ligne, pas besoin de justifier
            justified_line = line
        # Ajouter la ligne justifiée au texte final
        justified_text += justified_line + '\n'

    return justified_text.rstrip()

def write_text(sign : str, text : str, max_width : int, font_size : int):

    text = text.upper()
    formatted_text = justify_text(text, max_width)
    
    len_lines = len(formatted_text.split("\n"))
    
    font = ImageFont.truetype("SimplyMono-Bold.ttf", font_size)
    
    img = Image.open("post/{}.png".format(sign))
    
    draw = ImageDraw.Draw(img)
    draw.text((170,220), formatted_text, fill="white", font=font,  align="left")
    #img.show()
    
    return len_lines, len(formatted_text), img


if __name__ == "__main__":
    
    with open('response.json', 'r', encoding="utf-8") as f:
        response = f.read()
        data = response
    
    data = json.loads(data)
    signs = data.keys()
    sign = list(signs)[0]
    
    #for sign in signs:
    len_lines = 100
    len_text = 0
    width = 26
    font_size = 47
    
    while len_lines > 13:
        len_lines, len_text, img = write_text(sign, data[sign], max_width=width, font_size=font_size)
        width += 1
        font_size -= 1
    img.show()
    print(len_lines, len_text, font_size)