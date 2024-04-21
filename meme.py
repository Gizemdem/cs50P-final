import json
import requests
from io import BytesIO
import random
from PIL import Image, ImageDraw, ImageFont


class Meme():
    def __init__(self):
        self.image_path = ""
        self.caption = ""

    def randomMeme (self):
        f = open('memes.json')
        data = json.load(f)
        lenData = len(data)
        random_index = random.randint(0, lenData-1)
        template = data[random_index]['template']
        response = requests.get(template)
        url = response.json()['blank']
        print (url)
        f.close()
        return url

    def export (self, template_path, output="./meme.png"):
        response = requests.get(template_path)
        image_data= BytesIO(response.content)
        img = Image.open(image_data)
        W,H = img.size
        I1 = ImageDraw.Draw(img)
        font = ImageFont.truetype("Jersey10-Regular.ttf", 55)
        w = I1.textlength(self.caption, font=font)
        location = ((W-w)/2, H-100)
        I1.multiline_text(location, self.caption, align="center", font=font, stroke_width=2, stroke_fill=(0,0,0))
        img.save(output)

if __name__ == "__main__":
    caption = input("Say your caption: ")
    meme = Meme()
    meme.caption=caption
    template_path = meme.randomMeme()
    meme.export(template_path)



