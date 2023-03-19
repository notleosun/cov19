#import libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation',
		options = ['Data Cleaning','Exploratory Analysis'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['book', 'bar-chart'],
		default_index = 0,
		)
	
if selected=='Data Cleaning':
	st.title("The cleaning process: ")
	st.subheader("Cleaning the columns ")
	st.markdown("""	
def clean_col(col):
    col = col.strip()
    col = col.replace("Country/Region", "Country")
    return col

new_columns = []
for c in cov19.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)
    
cov19.columns = new_columns
	""")
