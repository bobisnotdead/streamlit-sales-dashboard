# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from gestionDB import get_chambre

st.set_page_config(page_title="Visualisation avancement", page_icon=":bar_chart:", layout="wide")
selected_sro = st.checkbox('liste des SRO', get_chambre.sro)
st.checkbox('liste des Artère', get_chambre.return_sro_art(selected_sro))

# ---- SIDEBAR ----

st.sidebar.header("faite votre selection ici:")
foa = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"],
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# df_selection = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender"
# )


