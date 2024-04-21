import streamlit as st
import json
import requests
from io import BytesIO
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

class Meme():
    def __init__(self):
        self.image_path = ""
        self.caption = ""

    def randomIndex(self):
        f = open('memes.json')
        data = json.load(f)
        lenData = len(data)
        index = random.randint(0, lenData-1)
        f.close()
        return index

    def randomMeme (self):
        f = open('memes.json')
        data = json.load(f)
        random_index = self.randomIndex()
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
        draw = ImageDraw.Draw(img)
        h = 55
        font = ImageFont.truetype("Jersey10-Regular.ttf", h)
        w_one = draw.textlength('w', font=font)

        max_chars = int(W / w_one) - 1
        lines = textwrap.wrap(self.caption, width=max_chars)
        y_text = h
        max_height = h * (len(lines) + 1)
        for line in lines:
            width = draw.textlength(line, font=font)
            draw.text(((W - width) / 2, H - max_height + y_text), line, font=font, stroke_width=2, stroke_fill=(0,0,0))
            y_text += h
        img.save(output)


def main():
    #store the meme in session
    if 'memeURL' not in st.session_state:
        meme = Meme()
        st.session_state['memeURL'] = meme.randomMeme()

    #appname
    st.set_page_config(page_title="meme online", page_icon="/workspaces/69429638/cs50pfinal/favicon.ico", layout="centered")

    # header and buttons
    header, download, reload = st.columns((8,0.75,1), gap="small")
    #header
    with header :
        st.subheader('ONLINE, WHAT DO YOU MEME?')

    # download button
    with download:
        download_button_container = download

    #reload button
    with reload:
        if st.button(label="🔁"):
            meme = Meme()
            st.session_state['memeURL'] = meme.randomMeme()

    #blank meme image
    imageContainer = st.empty()

    #caption card form, after submitting the caption it downloads the image and changes the st.image with captioned image
    with st.container(height=None, border=True):
        imageContainer.image(st.session_state['memeURL'])
        caption = st.text_area( label= "Caption", placeholder="Tell us your caption, what do you meme? (...)", )
        submitted = st.button(label="Submit")
        if submitted:
            meme = Meme()
            meme.caption = caption
            meme.export(st.session_state['memeURL'])
            imageContainer.image('./meme.png')
            with open('./meme.png', "rb") as file:
                download_button_container.download_button(
                    label="📥",
                    data=file,
                    mime="image/png"
                )

    #footer
    col1, footer, col2 = st.columns((3,7,1))

    with col1:
        st.write(' ')
    with footer:
        st.write('CS 50p Final Assignment by Gizem Demirhan ')
    with col2:
        st.write(' ')


if __name__ == "__main__":
    main()
