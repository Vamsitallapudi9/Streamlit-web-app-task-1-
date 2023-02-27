import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import plotly.express as px

# Load the Titanic dataset from Seaborn
titanic_df = sns.load_dataset('titanic')

# Display dataframe
st.title("Titanic Dataset")
st.write(titanic_df)


# Cat plot example
st.title("Titanic Dataset - Cat Plot")
x_var = st.selectbox("Select x-axis variable", options=list(titanic_df.columns))
y_var = st.selectbox("Select y-axis variable", options=list(titanic_df.columns))
hue_var = st.selectbox("Select hue variable", options=list(titanic_df.columns))
kind_var = st.selectbox("Select plot type", options=['box', 'violin'])
fig = sns.catplot(data=titanic_df, x=x_var, y=y_var, kind=kind_var, hue=hue_var)
st.pyplot(fig)