import streamlit as st
from meme import Meme

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

#st.divider()
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
