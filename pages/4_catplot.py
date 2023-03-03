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


st.title("Titanic Dataset - Cat Plot")
x_var = st.selectbox("Select x-axis variable", options=list(titanic_df.columns))
y_var = st.selectbox("Select y-axis variable", options=list(titanic_df.columns))
hue_var = st.selectbox("Select hue variable", options=list(titanic_df.columns))
kind_var = st.selectbox("Select plot type", options=['box', 'violin'])

fig = px.box(titanic_df, x=x_var, y=y_var, color=hue_var) if kind_var == 'box' else px.violin(titanic_df, x=x_var, y=y_var, color=hue_var)
fig.update_layout(title="Cat Plot of Titanic Dataset")

st.plotly_chart(fig)