
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

# find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#--- Load assets ---
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_z2m65ck9.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# --- header section ----
# with st.container():
st.subheader("Hi, I am Dillon :wave: ")
st.title("A freelance web developer")
st.write("What I've been up to. Here's my recent work.")
st.write("[Learn more >](https://github.com/bacdillon)")

# with right_column:
st_lottie(lottie_coding, height=500, width=500, key="coding")



