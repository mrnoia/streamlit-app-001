import streamlit as st
import pandas as pd
import time
import numpy as np

from st_btn_select import st_btn_select

# selection = st_btn_select(("option 1", "option 2", "option 3"))

# st configuration
st.set_page_config(
    page_title="Streamlit application",
    page_icon="👋",
    layout="wide",
)
# sidebar
st.title("Playing with CSV files and Pandas")
with st.spinner("Loading..."):
    time.sleep(1)
# upload as CSV file
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(
        uploaded_file,
        encoding="iso-8859-1",
        nrows=1000,
        error_bad_lines=False,
    )
    # st.success("file uploaded and converted to df!", icon="✅")
    st.write(df)

    def paginate_dataframe(dataframe, page_size, page_num):
        page_size = page_size
        if page_size is None:
            return None

        offset = page_size * (page_num - 1)
        return dataframe[offset : offset + page_size]

    st.write(paginate_dataframe(df, 10, 2))
    # p1, p2, p3, p4, p5, p6 = st.columns(6)
    # p1.button("1")
    selection = st_btn_select(("1", "2", "3"))
    st.write("selection")

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="large_df.csv",
        mime="text/csv",
    )
    with st.echo():
        st.write(df.head())
    # Returns the first five rows of the dataframe. It is possible to specify number of columns to be returned as a parameter inside the brackets.

    with st.echo():
        st.write(f"{df.shape} number of rows and columns respectively")
    # Does not need parentheses. Returns a tuple with number of rows and columns respectively.
    # df.describe()
    # Returns common statistics such as mean,standard deviation etc on every column.
    # df.columns
    # Returns the name of all the columns in a list
    # df.index
    # Returns the index of the dataframe

    # Shows how many missing values there are on each column.
    # df.dtypes

    # st.write(df.isna().sum())
    # Returns the types of each column. Common
    # types are: integer, float, string (listed as
    # Object), datetime.

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
if col1.button("Say hello"):
    col1.write("Hello there")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            border:1px solid red;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            border:1px solid blue;
            text-align: end;
        }         
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    """
    ## Column 1
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua. Volutpat sed cras ornare arcu dui vivamus.
    """
    mydataset1 = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
    myvar1 = pd.DataFrame(mydataset1)
    st.write(myvar1)

with col2:
    """
    ## Column 2
    Stuff aligned to the right
    """
    mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
    myvar = pd.DataFrame(mydataset)
    st.write(myvar)
    st.button("➡️")
with col3:
    """
    ## Column 3
    This column was untouched by our CSS
    """
    st.button("🐈")
