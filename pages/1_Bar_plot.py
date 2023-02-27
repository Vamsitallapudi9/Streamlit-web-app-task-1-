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



# Bar plot example
st.title("Titanic Dataset - Bar Plot")
x_var = st.selectbox("Select x-axis variable", options=list(titanic_df.columns))
y_var = st.selectbox("Select y-axis variable", options=list(titanic_df.columns))
hue_var = st.selectbox("Select hue variable", options=list(titanic_df.columns))
fig, ax = plt.subplots()
sns.barplot(data=titanic_df, x=x_var, y=y_var, hue=hue_var)
st.pyplot(fig)