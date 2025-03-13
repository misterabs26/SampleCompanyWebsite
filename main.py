import streamlit as st
import pandas as pd
from streamlit_card import card


st.set_page_config(layout="wide")
cols = st.columns(3)

with open("assets/style.css","r") as css_file:
    custom_css = css_file.read()

st.markdown(
    f"""
    <style>{custom_css}</style>
    """,
    unsafe_allow_html=True
)
# header
header_msg = """Lorem ipsum odor amet, consectetuer adipiscing elit. 
Rutrum at malesuada at turpis conubia arcu sociosqu porttitor neque. 
Habitasse potenti consequat dictumst himenaeos est sem nisi. 
Sem lacinia fusce conubia rutrum nunc ex amet nulla. 
Dui dapibus ex etiam ad mauris? Lacus volutpat molestie maecenas taciti habitasse nisl lacinia. 
Natoque venenatis nam sagittis et; ante platea consectetur. 
Odio donec nullam nam proin dis convallis interdum feugiat. 
Ahabitasse nulla ad at nunc consequat mauris."""

with st.container():
    st.header("The Best Company")
    st.write(header_msg)


st.subheader("Our Team")
with open("assets/data.csv","r") as data:
    df = pd.read_csv(data)

print(df)
for i, row in df.iterrows():
    st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
    st.image(f"images/{row['image']}")
    st.write(row['role'])