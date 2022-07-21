import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from gestionDB import get_chambre

st.set_page_config(page_title="Visualisation avancement", page_icon=":bar_chart:", layout="wide")
selected_sro = st.selectbox('liste des SRO', get_chambre.sro)
st.selectbox('liste des Arte', get_chambre.return_sro_art(selected_sro))