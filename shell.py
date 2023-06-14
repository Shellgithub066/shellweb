import streamlit as st
import pandas as pd 
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure
import altair as alt

st.set_page_config(
    page_title="Shell Veri uygulaması",

) 


st.title("Shell Veri Web sayfası")


st.title('Shell')
st.title('Kullanmadan önce aşşağıdaki uyarıları dikkate alınız.')


st.text('1. Adım  Verileri görelim .csv formatında ')
st.text('2. Adım  Verileri inceleyelim  Bu 2. sayfada olacak ')
st.text('3. Adım  Verileri Grafiklere bakalım  Bu 3. sayfada görünecektir. ')
st.text('4. Adım  Verilere ve Grafiklere bakarak bir kaç çıktı görelim.')

st.sidebar.success("Select a page above ")

st.header('Single File Upload')


uploaded_file = st.file_uploader('Upload a file')

df = pd.read_csv(uploaded_file)

    


st.write(df)
    

df = pd.read_csv(uploaded_file)

data = df(70)

    


 



