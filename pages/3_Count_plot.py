import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import plotly.express as px

# Load the Titanic dataset from Seaborn
titanic_df = sns.load_dataset('titanic')

# Display dataframe
st.title("Titanic Dataste")
st.write(titanic_df)


# Count plot example
st.title("Titanic Dataset - Count Plot")
x_var = st.selectbox("Select x-axis variable", options=list(titanic_df.columns))
hue_var = st.selectbox("Select hue variable", options=list(titanic_df.columns))

fig = px.histogram(titanic_df, x=x_var, color=hue_var)
fig.update_layout(title="Count Plot of Titanic Dataset")

st.plotly_chart(fig)