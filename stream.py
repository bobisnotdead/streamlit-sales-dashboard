from pdb import pm
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from gestionDB import get_chambre

st.set_page_config(page_title="Visualisation avancement", page_icon=":bar_chart:", layout="wide")
# ---- SIDEBAR ----
# with st.sidebar:
#     control_panel = st.header("faite votre selection ici:")
#     st.multiselect(
#         "Selection du type de document a vérifier",
#         options= 'c6',
#         options= 'foa'

# )
# customer_type = st.sidebar.multiselect(
#     "export import de document",
#     options= 'upload_photo',
#     default= 'upload_document'
# )
selected_sro = st.selectbox('liste des NRO', get_chambre.sro_list)
selected_pm = st.selectbox('liste des SRO', get_chambre.get_pm_by_sro(selected_sro))
# selected_art = st.selectbox('liste des Art', get_chambre.get_picture_by_art(selected_sro, pm))

#test

st.sidebar.markdown("## Controls")
st.sidebar.markdown("Selectionne le mode de vérification")
st.sidebar.selectbox( ['c6', 'foa', 'upload folder', 'mesure', 'frp' ])
seeked_pt = st.text_input('tape un numéro d\'apuie', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None)
st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)
