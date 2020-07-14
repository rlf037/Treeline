import streamlit as st
from PIL import Image

@st.cache
def get_css():
    """
    Returns the css for markdown.
    """
    with open('style.css') as style:
        css = style.read()
    return f'<style>{css}</style>'

@st.cache
def get_image():
    image = Image.open('imgs/logo.png')
    return image

def main():
    """
    Main function for streamlit to use.
    """
    st.markdown(get_css(), unsafe_allow_html=True)

    st.image(get_image(), use_column_width=True)


if __name__ == '__main__':
    main()
