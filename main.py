import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
header = st.container()
members_section = st.container()

with open("assets/style.css","r") as css_file:
    custom_css = css_file.read()

with open("assets/data.csv","r") as data:
    df = pd.read_csv(data)


st.markdown(f"<style>{custom_css}</style>",unsafe_allow_html=True)

# header
header_msg = """Lorem ipsum odor amet, consectetuer adipiscing elit. 
Rutrum at malesuada at turpis conubia arcu sociosqu porttitor neque. 
Habitasse potenti consequat dictumst himenaeos est sem nisi. 
Sem lacinia fusce conubia rutrum nunc ex amet nulla. 
Dui dapibus ex etiam ad mauris? Lacus volutpat molestie maecenas taciti habitasse nisl lacinia. 
Natoque venenatis nam sagittis et; ante platea consectetur. 
Odio donec nullam nam proin dis convallis interdum feugiat. 
Ahabitasse nulla ad at nunc consequat mauris."""

with header:
    st.header("The Best Company")
    st.write(header_msg)


with members_section:
    st.subheader("Our Team")
    cols = st.columns(3)
    for i, row in df.iterrows():
        col = cols[i % 3]
        with col:
            st.markdown(f"""
            <h3 style="text-align:center">
                {row['first name'].capitalize()} {row['last name'].capitalize()}
            </h3>
            """, unsafe_allow_html=True)

            st.image(f"images/{row['image']}",use_container_width=True,)

            st.markdown(f"""
                <p style="text-align:center">{row['role']}</p>
            """, unsafe_allow_html=True)


