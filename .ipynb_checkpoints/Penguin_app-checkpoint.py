import streamlit as st
import pandas as pd
import numpy as np
import joblib
import seaborn as sns

st.title('Penguin Prediction App')
st.header('This is a header')
st.subheader('This is a subheader')

st.sidebar.title('Sidebar Title')
sidebar = st.sidebar
sidebar.subheader('Test')

side_button = st.sidebar.button('Press me!')
if side_button:
    sidebar.write('You pressed me!')
else:
    sidebar.write

col1, col2 = st.columns(2)
col1.subheader('Col1')
col2.subheader('Col2')

col21, col22, col23 = st.columns([3, 2, 1])
col21.write('Widest Column, testing 123, text should wrap, some more text')
col22.write('Medium column width, mic check, please wrap')
col23.write('Smallest column, success')

st.markdown('Markdown *syntax works')

'Just markdown text'

'## Magic'

st.write('<h2 style="text-align:center"> Text aligned with HTML </h2>', unsafe_allow_html=True)

check=st.checkbox('Check me out')
button_check = st.button('Is box checked?')
if button_check:
    if check:
        st.write('Box is checked')
    else:
        st.write('Box is not checked')

animal_options = ['Penguin', 'Dog', 'Cat', 'Horse']
fav_animal = st.radio('What is your favorite animal?', animal_options)
fav_button = st.button('Submit')
if fav_button:
    st.write(f'Your favorite animal is a {fav_animal}')

fav_animal2 = st.selectbox('What is your favorite animal?', animal_options)
fav_button2 = st.button('Submit2')
if fav_button2:
    st.write(f'Your favorite animal is a {fav_animal2}')

multi_animal = st.multiselect('What are your favorite animals?', animal_options)
multi_button = st.button('Submit3')
if multi_button:
    st.write(multi_animal)

num_pets = st.slider('How many pets do you have?', 0, 10, step=1)

in_text = st.text_input("What is your pet's name?", value=" I don't have a pet")
st.write("Pet's name is:", in_text)

in_num = st.number_input("What is your pet's age?", value=0.01, step=.01, min_value=.01)

#penguins = sns.load_dataset('penguins')
#data_expand = st.expander('Show penguins dataset')
#data_expand.table(penguins.head())
