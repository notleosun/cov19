#import libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from streamlit_option_menu import option_menu

cov19 = pd.read_csv("covid_19_data.csv")

def clean_col(col):
    	col = col.strip()
    	col = col.replace("Country/Region", "Country")
    	return col

new_columns = []
for c in cov19.columns:
    	clean_c = clean_col(c)
    	new_columns.append(clean_c)
cov19.columns = new_columns

countrycode = pd.read_csv("continents2.csv")
country_dict = {
                    " Azerbaijan":"Azerbaijan",
                    "Bahamas  The":"Bahamas",
                    "Congo (Brazzaville)":"Republic of the Congo",
                    "Congo (Kinshasa)":"Republic of the Congo",
                    "Gambia  The":"Gambia",
                    "Guinea-Bissau":"Guinea Bissau",
                    "Mainland China":"China",
                    "occupied Palestinian territory":"Palestine",
                    "('St. Martin' )":"St. Martin",
                    "The Bahamas":"Bahamas",
                    "The Gambia":"Gambia"
                   }
cov19["Country"] = cov19.Country.replace(country_dict)	

region_dict = {country:region for country, region in zip(countrycode["name"], countrycode["sub-region"])}
region_dict.update({
                    " Azerbaijan":"Western Asia",
                    "Bahamas  The":"Latin America and the Caribbean",
                    "Bosnia and Herzegovina":"Southern Europe",
                    "Brunei":"South-eastern Asia",
                    "Burma":"South-eastern Asia",
                    "Cape Verde":"Sub-Saharan Africa",
                    "Channel Islands":"Northern Europe",
                    "Congo (Brazzaville)":"Sub-Saharan Africa",
                    "Congo (Kinshasa)":"Sub-Saharan Africa",
                    "Curacao":"Latin America and the Caribbean",
                    "Diamond Princess":"Northern Europe",
                    "East Timor":"South-eastern Asia",
                    "Gambia  The":"Sub-Saharan Africa",
                    "Guinea-Bissau":"Sub-Saharan Africa",
                    "Ivory Coast":"Sub-Saharan Africa",
                    "Kosovo":"Southern Europe",
                    "Republic of the Congo":"Sub-Saharan Africa",
                    "Macau":"Eastern Asia",
                    "Mainland China":"Eastern Asia",
                    "MS Zaandam":"Western Europe",
                    "Northern Ireland":"Northern Europe",
                    "North Ireland":"Northern Europe",
                    "North Macedonia":"Southern Europe",
                    "occupied Palestinian territory":"Western Asia",
                    "Others":"Northern Europe",
                    "Palestine":"Western Asia",
                    "Republic of Ireland":"Northern Europe",
                    "Reunion":"Sub-Saharan Africa",
                    "Saint Barthelemy":"Latin America and the Caribbean",
                    "('St. Martin' )":"Latin America and the Caribbean",
                    "St. Martin":"Latin America and the Caribbean",  
                    "UK":"Northern Europe",
                    "US":"Northern America",
                    "The Bahamas":"Latin America and the Caribbean",
                    "The Gambia":"Sub-Saharan Africa",
                    "Vatican City":"Southern Europe",
                    "West Bank and Gaza":"Western Asia"
                   })
                   
cov19["Region"] = cov19.Country.replace(region_dict)

continent_dict = {}
continent_dict.update({
    'Eastern Asia':"Asia",
    'South-eastern Asia':"Asia",
    'Southern Asia':"Asia",
    'Western Asia':"Asia",
    'Central Asia':"Asia",
    'Western Europe':"Europe",
    'Northern Europe':"Europe",
    'Southern Europe':"Europe",
    'Eastern Europe':"Europe",
    'Northern America':"North America",
    'Northern Africa':"Africa",
    "Sub-Saharan Africa":"Africa",
    'Micronesia':"Oceania",
    "Melanesia":"Oceania",
    "Australia and New Zealand":'Oceania',
    "Polynesia":"Oceania",
    "Latin America and the Caribbean":"South America"
})
cov19["Continent"] = cov19.Region.replace(continent_dict)



with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation',
		options = ['Data Cleaning','Exploratory Analysis'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['book', 'bar-chart'],
		default_index = 0,
		)
	
if selected=='Data Cleaning':
	st.title("The Cleaning Process: ")
	
	st.subheader("The Original Dataset ")
	
	cov19
	
	st.subheader("Cleaning the columns ")
	st.code("""	
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
	
	st.code("""
countrycode = pd.read_csv("continents2.csv")
countrycode
	""")
	countrycode
	st.subheader("Cleaning Country Names ")
	st.code("""
country_dict = {
                    " Azerbaijan":"Azerbaijan",
                    "Bahamas  The":"Bahamas",
                    "Congo (Brazzaville)":"Republic of the Congo",
                    "Congo (Kinshasa)":"Republic of the Congo",
                    "Gambia  The":"Gambia",
                    "Guinea-Bissau":"Guinea Bissau",
                    "Mainland China":"China",
                    "occupied Palestinian territory":"Palestine",
                    "('St. Martin' )":"St. Martin",
                    "The Bahamas":"Bahamas",
                    "The Gambia":"Gambia"
                   }
cov19["Country"] = cov19.Country.replace(country_dict)	
	""")
	
	st.subheader("Assigning Regions ")
	st.code("""
region_dict = {country:region for country, region in zip(countrycode["name"], countrycode["sub-region"])}
region_dict.update({
                    " Azerbaijan":"Western Asia",
                    "Bahamas  The":"Latin America and the Caribbean",
                    "Bosnia and Herzegovina":"Southern Europe",
                    "Brunei":"South-eastern Asia",
                    "Burma":"South-eastern Asia",
                    "Cape Verde":"Sub-Saharan Africa",
                    "Channel Islands":"Northern Europe",
                    "Congo (Brazzaville)":"Sub-Saharan Africa",
                    "Congo (Kinshasa)":"Sub-Saharan Africa",
                    "Curacao":"Latin America and the Caribbean",
                    "Diamond Princess":"Northern Europe",
                    "East Timor":"South-eastern Asia",
                    "Gambia  The":"Sub-Saharan Africa",
                    "Guinea-Bissau":"Sub-Saharan Africa",
                    "Ivory Coast":"Sub-Saharan Africa",
                    "Kosovo":"Southern Europe",
                    "Republic of the Congo":"Sub-Saharan Africa",
                    "Macau":"Eastern Asia",
                    "Mainland China":"Eastern Asia",
                    "MS Zaandam":"Western Europe",
                    "Northern Ireland":"Northern Europe",
                    "North Ireland":"Northern Europe",
                    "North Macedonia":"Southern Europe",
                    "occupied Palestinian territory":"Western Asia",
                    "Others":"Northern Europe",
                    "Palestine":"Western Asia",
                    "Republic of Ireland":"Northern Europe",
                    "Reunion":"Sub-Saharan Africa",
                    "Saint Barthelemy":"Latin America and the Caribbean",
                    "('St. Martin' )":"Latin America and the Caribbean",
                    "St. Martin":"Latin America and the Caribbean",  
                    "UK":"Northern Europe",
                    "US":"Northern America",
                    "The Bahamas":"Latin America and the Caribbean",
                    "The Gambia":"Sub-Saharan Africa",
                    "Vatican City":"Southern Europe",
                    "West Bank and Gaza":"Western Asia"
                   })
                   
cov19["Region"] = cov19.Country.replace(region_dict)
	""")
	
	st.subheader("Assigning Continents ")
	st.code("""
continent_dict = {}
continent_dict.update({
    'Eastern Asia':"Asia",
    'South-eastern Asia':"Asia",
    'Southern Asia':"Asia",
    'Western Asia':"Asia",
    'Central Asia':"Asia",
    'Western Europe':"Europe",
    'Northern Europe':"Europe",
    'Southern Europe':"Europe",
    'Eastern Europe':"Europe",
    'Northern America':"North America",
    'Northern Africa':"Africa",
    "Sub-Saharan Africa":"Africa",
    'Micronesia':"Oceania",
    "Melanesia":"Oceania",
    "Australia and New Zealand":'Oceania',
    "Polynesia":"Oceania",
    "Latin America and the Caribbean":"South America"
})
cov19["Continent"] = cov19.Region.replace(continent_dict)
	""")
	

	st.subheader("Cleaned Data ")
	cov19

if selected=='Exploratory Analysis':
	st.title("Exploratory Analysis: ")
	country_option=st.selectbox('Select a country',np.sort(cov19['Country'].unique()))
	case_option=st.selectbox('Select cases',['Confirmed','Deaths','Recovered'])
	
	fig=px.scatter(cov19[cov19['Country']==country_option],x="ObservationDate",
            y=cov19.loc[cov19['Country']==country_option,case_option],hover_name='ObservationDate', height = 800, width = 750)
	st.plotly_chart(fig)
