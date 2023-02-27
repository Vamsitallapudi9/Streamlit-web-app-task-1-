import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import plotly.express as px

# Load the Titanic dataset from Seaborn
titanic_df = sns.load_dataset('titanic')

# Display dataframe
st.header('About the dataset:')
st.text('Titanic Dataset - It is one of the most popular datasets used for understanding machine learning basics. It contains information of all the passengers aboard the RMS Titanic, which unfortunately was shipwrecked.')
st.subheader('Find the dataset below and take time to explore ')
st.title("Titanic Dataset")
st.write(titanic_df)

st.subheader('Please navigate to the next following pages to find different plots which will help you to understand the dataset')

