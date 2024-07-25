import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("Picture")

with col2:

    st.markdown("<h1 style='margin-bottom: -35px;'>Leonhel V. Fortin</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='title-header'margin-bottom: -10px; style='color: #60b4ff;'>Artificial Intelligence Engineer</h3>", unsafe_allow_html=True)
    st.write("Leonhel V. Fortin is an accomplished Artificial Intelligence Engineer specializing in developing and implementing AI solutions. Leonhel is passionate about leveraging technology for smart city initiatives and fostering creative industry growth.", unsafe_allow_html=True)

with st.container():
   st.write("This is inside the container")

st.write("This is outside the container")

def page1():
    st.title("About Me")

def page2():
    st.title("Experience")

def page3():
    st.title("Skills")

def page4():
    st.title("Projects")

pg = st.navigation([
    st.Page(page1, title="About Me"),
    st.Page(page2, title="Experience"),
    st.Page(page3, title="Skills"),
    st.Page(page4, title="Projects"),
])

pg.run()
