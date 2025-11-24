import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Accessing Materials',
    page_icon='📁'
)

local_css("css/style.css")

st.title("Accessing and opening Jupyter Notebooks")

st.markdown("""

### Download the Python for Accounting workshop materials

The DSL teaches Python using Jupyter Notebooks.

You can download the notebooks from below.

The notebooks will be combined into a single zip file. Mac-users can simple double click on the zip file to unpack the jupyter notebooks.
Window-users have to right-click on the zip file, select Extract All... and then click on Extract.
            
This should create a new folder named python-for-accounting which contains the different jupyter notebook files.
""")


with open("materials/python-for-accounting.zip", "rb") as f:
    btn = st.download_button(
        label = "Download Python materials",
        data = f,
        file_name = "python-for-accounting.zip",
        mime = "application/zip"
        )


st.markdown(
    """
### Next step

Go to the Opening Jupyter Notebooks section and follow
the instructions to open the Jupyter Notebooks and Python code in a Jupyter Notebook.
"""
)
