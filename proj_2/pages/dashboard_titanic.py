import streamlit as st
from matplotlib import image
import os
import plotly.express as px
import pandas as pd

st.snow()
st.title("Dashboard of Titanic Data")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
df = df.dropna()
df['Age_bucket'] = [int(val/10) for val in df['age'].values ] 

species = st.selectbox("Select the town:", df['embark_town'].unique())


fig_1 = px.histogram(df[df['embark_town'] == species], x="Age_bucket")
st.plotly_chart(fig_1, use_container_width=True)


df['not_survived'] = [1 if val==0 else 0 for val in df['survived'].values ] 

