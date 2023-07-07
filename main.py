import streamlit as st
import pandas as pd
import requests
import numpy as np
import plotly.figure_factory as ff

api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)

st.title("Getting Started Streamlit")
st.write("This is introduction to streamlit")

st.markdown("## Code")
code = '''
def hello():
    print("Hello, Streamlit!")
'''

show_btn = st.button("Show code!")
if show_btn:
    st.code(code, language='python')

cols = st.columns(2)
with cols[0]:
    age_inp = st.number_input("Input your age")
    st.markdown(f"Your age is {round(age_inp, 2)}")


# st.markdown("# NLP Task")
with cols[1]:
    text_inp = st.text_input("Input your text")
    word_tokenize = "|".join(text_inp.split())
    st.markdown(f"{word_tokenize}")


df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 60, 90]
})
st.dataframe(df)
show_chart_btn = st.button("Show Chart!!")
if show_chart_btn:
    st.line_chart(df, x='first column', y='second column')

show_import_data = st.checkbox("Show imported data",key="sid")
container = st.empty()
with container:
    if show_import_data:
        response_df = pd.DataFrame(response.json())
        st.dataframe(response_df,hide_index=True)

