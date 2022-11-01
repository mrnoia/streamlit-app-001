import streamlit as st
import pandas as pd
import time
import numpy as np
from st_btn_select import st_btn_select

# initialize
df = None
# st configuration
st.set_page_config(
    page_title="Streamlit application",
    page_icon="👋",
    layout="wide",
)

# callback incrementing session
def file_callback():
    if "file upload callback" not in st.session_state:
        st.session_state["file upload callback"] = 1
    else:
        st.session_state["file upload callback"] += 1
    # st.write(st.session_state["file upload callback"])


# dataframe pagination
def paginate_dataframe(dataframe, page_size, page_num):
    page_size = page_size
    if page_size is None:
        return None
    offset = page_size * (page_num - 1)
    return dataframe[offset : offset + page_size]


# load CSV into df
@st.cache
def panda_read_csv(file_name):
    df = pd.read_csv(
        file_name,
        encoding="iso-8859-1"
        # nrows=1000
        # error_bad_lines=False,
    )
    return df


st.title("Playing with CSV files and Pandas")
# file uploader
with st.expander("File Upload"):
    file_name = st.file_uploader(
        "Choose a file",
        "csv",
        on_change=file_callback,
        args=None,
        label_visibility="collapsed",
    )
    if file_name is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = panda_read_csv(file_name)

if df is not None:
    with st.expander("Manipulate dataset"):
        st.write("")
        options = st.multiselect(
            "Drop cols",
            df.columns,
        )
        # st.write("You selected to remove:", options)
        for opt in options:
            # st.write(opt)
            df = df.drop(opt, axis=1)

if df is not None:
    st.write(paginate_dataframe(df, 10, 2))
    selection = st_btn_select(("1", "2", "3"))
