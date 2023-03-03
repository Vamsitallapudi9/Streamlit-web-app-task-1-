import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Hey fellas, Check this out!!!", page_icon=":smiley:",layout="wide")


# Define function to display homepage content
def show_homepage():
    # Write a title and description of your app
    st.title(':ship: Welcome aboard the Titanic! :ship:')
        
    st.header(':wave: Ahoy there, mateys! I am :green[Vamsi Tallapudi], and this is my first-ever web application! :tada:')
    
    st.subheader("Hop on deck and explore the Titanic Dataset with us!")

    # Write a brief summary of what the app does
    st.write("**Ahoy there, explorers! This app will help you visualize and analyze the Titanic Dataset like never before. You can choose your desired X and Y axes and create all sorts of cool graphs!**")
    
    # Write instructions on how to get started
    st.write('But first, let\'s learn a bit about the Titanic Dataset.')
    st.write("**The Titanic Dataset is one of the most popular datasets used for understanding machine learning basics. It contains information about all the passengers aboard the RMS Titanic, which unfortunately sank after hitting an iceberg.**")

    st.caption(':anchor: Ready to dive in? Head on over to the next page to learn more about the dataset we\'re working with! :sunglasses:')
 
    
 
 

    
# Streamlit app
def main():
    show_homepage()

if __name__ == "__main__":
    main()


# Add LinkedIn and GitHub links
st.markdown("[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vamsi-tallapudi-2b99211bb/)](https://www.linkedin.com/in/vamsi-tallapudi-2b99211bb/)")
st.write("Looking forward to connecting with you and chatting about all things data science and AI!")
st.markdown("[![GitHub](https://img.shields.io/badge/-GitHub-black?style=for-the-badge&logo=github&link=https://github.com/Vamsitallapudi9)](https://github.com/Vamsitallapudi9)")
st.write("Feel free to browse my projects and repositories. If you find something interesting, don't hesitate to reach out and let me know!")

# Add a colorful thank you message
body = ":rainbow: Let me take a moment to thank :heart_eyes_cat: Kanav Bansal and :sparkles: Innomatics Research Labs :sparkles: for this amazing opportunity! :rocket:"
st.write(body)

# Add a link to Innomatics Research Labs
st.markdown(":star2: DO CHECK OUT Innomatics Research Labs TO LEARN AND GROW :star2:")
st.markdown("[![Innomatics Research Labs](https://www.innomatics.in/wp-content/uploads/2020/04/innomatics-research-labs-logo-squared.png)](https://www.innomatics.in/)")












