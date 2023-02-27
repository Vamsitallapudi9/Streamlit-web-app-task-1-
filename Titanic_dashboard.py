import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Welcome to My App", page_icon=":smiley:",layout="wide")



# Define function to display homepage content
def show_homepage():
    # Write a title and description of your app
    st.title(':red[Hello Everyone] :wave:')
        
    st.header( 'I am :green[Vamsi Tallapudi] and :blue[Welcome to my first web application]' )
        
       
    
    st.subheader("This is a Streamlit app for Data visualization and Analysis of the Titanic Dataset.")

    # Write a brief summary of what the app does
    st.write("**This app allows you to create different plots and to explore and analyze datasets using visualizations and the best part is you can choose your desired X_axis  and Y_axis.**")

    
    
    
    # Write instructions on how to get started
    st.write('Before diving in lets know what is titanic dataset')
    st.write("**Titanic Dataset - It is one of the most popular datasets used for understanding machine learning basics. It contains information of all the passengers aboard the RMS Titanic, which unfortunately was shipwrecked.**")



    st.caption('please navigate to the next page to find out the details of dataset, we are working on ')
    
    
    
 
 

    
# Streamlit app
def main():
    show_homepage()

if __name__ == "__main__":
    main()

# Create a hyperlink to your LinkedIn profile
st.markdown("[click here to Connect with me on LinkedIn!](https://www.linkedin.com/in/vamsi-tallapudi-2b99211bb/)")
st.write("Looking forward to connecting with you and chatting about all things data science and AI!")

# Create a hyperlink to your GitHub profile
st.markdown("[click here to Check out my GitHub profile!](https://github.com/Vamsitallapudi9)")
st.write("Feel free to browse my projects and repositories. If you find something interesting, don't hesitate to reach out and let me know!")



body='Let me take a moment to thank :red[Kanav Bansal] and :red[Innomatics Research Labs] for this oppurtunity'
st.write(body)
 
st.markdown("DO CHECK OUT THE INNOMATICS RESEARCH LABS TO LEARN AND GROW")
st.markdown("[Innomatics Research labs](https://www.innomatics.in/)")

image_url = "https://www.innomatics.in/wp-content/uploads/2020/04/innomatics-research-labs-logo-squared.png"
image = st.image(image_url, caption="Innomatics Research labs")
    










