import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import plotly.express as px
import base64

# Load the Titanic dataset from Seaborn
titanic_df = sns.load_dataset('titanic')

# Display dataframe
st.header('About the dataset:')
st.text('Titanic Dataset - It is one of the most popular datasets used for understanding machine learning basics. It contains information of all the passengers aboard the RMS Titanic, which unfortunately was shipwrecked.')
st.subheader('Find the dataset below and take time to explore ')
# Add a download button for the dataset
def download_button(object_to_download, download_filename, button_text):
    """
    Generates a link to download the given object_to_download.
    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # Some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{button_text}</a>'
    return href

st.title("Titanic Dataset Analysis")

# Add a button to download the dataset
if st.button("Download Dataset"):
    href = download_button(titanic_df, "titanic.csv", "Click here to download the Titanic dataset!")
    st.markdown(href, unsafe_allow_html=True)
st.title("Titanic Dataset")
st.write(titanic_df)

st.subheader('Please navigate to the next following pages to find different plots which will help you to understand the dataset')

# Sidebar menu for selecting the analysis task
analysis_task = st.sidebar.selectbox("Select Analysis Task", ["Data Overview", "Data Cleaning", "Data Exploration"])

# Data Overview
if analysis_task == "Data Overview":
    st.write("### Data Overview")
    st.write("Select an option to view the corresponding data:")
    option = st.radio(
        "",
        ("Head", "Tail", "Sample", "Columns", "Shape", "Info", "Descriptive Statistics")
    )
    if option == "Head":
        st.write(titanic_df.head())
    if option == "Tail":
        st.write(titanic_df.tail())
    if option == "Sample":
        st.write(titanic_df.sample())
    if option == "Columns":
        st.write(titanic_df.columns)
    if option == "Shape":
        st.write(titanic_df.shape)
    if option == "Info":
        st.write(titanic_df.info())
    if option == "Descriptive Statistics":
        st.write(titanic_df.describe())


# Data Cleaning
# Data Cleaning
elif analysis_task == "Data Cleaning":
    st.write("### Data Cleaning")
    
    # Display original data and missing value counts
    st.write("Original Data:")
    st.write(titanic_df)
    st.write("Number of missing values in each column:")
    st.write(titanic_df.isnull().sum())
    
    # Select columns to drop or fill missing values
    st.write("Select columns to drop or fill missing values:")
    columns = st.multiselect("Columns", list(titanic_df.columns), default=list(titanic_df.columns))
    drop_columns = st.multiselect("Columns to drop", columns, default=[])
    fillna_columns = [col for col in columns if col not in drop_columns]
    
    # Choose fill method and fill missing values
    fillna_method = st.selectbox("Fill Method", ["Mean", "Median", "Mode"])
    if fillna_method == "Mean":
        fillna_values = titanic_df[fillna_columns].mean()
    elif fillna_method == "Median":
        fillna_values = titanic_df[fillna_columns].median()
    elif fillna_method == "Mode":
        fillna_values = titanic_df[fillna_columns].mode().iloc[0]
    titanic_df[fillna_columns] = titanic_df[fillna_columns].fillna(fillna_values)
    
    # Drop selected columns
    titanic_df = titanic_df.drop(drop_columns, axis=1)
    
    # Display cleaned data and missing value counts
    st.write("Cleaned Data:")
    st.write(titanic_df)
    st.write("Number of missing values in each column after cleaning:")
    st.write(titanic_df.isnull().sum())
    
    
    
