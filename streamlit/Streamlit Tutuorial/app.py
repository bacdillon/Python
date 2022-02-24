import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Text/Title
st.title("Streamlit Tutorials")

# Images
from PIL import Image
img = Image.open("streamit.jpg")
st.image(img,width=300,caption="Stream Image")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successful")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error Danger!")
st.exception("NameError('name was not defined')")

# Get help info about Python
st.help(range)

# Writing Text
st.write("Here is the text with write")
st.write(range(10))

# Video
vid_file = open("Pexels Videos 1851190.mp4","rb").read()
st.video(vid_file)

# Audio
st.header("Music: Royalty Free Music from Bensound")
audio_file = open("bensound-anewbeginning.mp3","rb").read()
st.audio(audio_file,format='audio/mp3')

# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio buttons
status = st.radio("What is your status", ("Active","Inactive"))

if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","Data Scientist","Doctor","Business Man"])
st.write("You select this option",occupation)

# MultiSelect
location = st.multiselect("Where do you work?",("Raffles Place","Paya Lebar","Ayer Raja Crescent"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)

# Buttons
st.button("Click Me")
if st.button("About Streamlit"):
    st.text("Streamlit is Cool")

# Text Input
firstname = st.text_input("Enter your first name","Type Here...")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area("Enter your message", "Enter here...")
if st.button("submit"):
    result = message.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is ", datetime.datetime.now())

# Time
the_time = st.time_input("The time is ", datetime.time())

# Display  JSON
st.text("Display JSAON")
st.json({'name':"Dillon",'Gender':"Male"})

# Display Raw Code
st.text("Display Raw Code")
st.code("Import numpy as np")

# Display Raw Code
with st.echo():
    # This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
st.text("Progress Bar... 10%")
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Completed")

# Balloons
# st.balloons()

# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tutorial")

# DataFrames
st.dataframe(df)

# Tables
st.table(df)

# Functions
@st.cache
def run_function():
    return range(100)
st.write(run_function())

# Plot - Matplotlib with Streamlit
st.subheader("Matplotlib with Streamlit")
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)



