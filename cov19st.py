#import libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")

mypath = ""
cov19 = pd.read_csv(mypath + "covid_19_data.csv")

def clean_col(col):
    	col = col.strip()
    	col = col.replace("Country/Region", "Country")
    	return col

new_columns = []
for c in cov19.columns:
    	clean_c = clean_col(c)
    	new_columns.append(clean_c)
cov19.columns = new_columns

countrycode = pd.read_csv(mypath + "continents2.csv")
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

cov19["ObservationDate"] = pd.to_datetime(cov19["ObservationDate"])
cov19.sort_values(["ObservationDate"]).reset_index(drop = True)

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

num_cols = ["Confirmed", "Deaths", "Recovered"]
cat_cols = ['ObservationDate', "Province/State", "Country", "Region", "Continent"]

cov19_mean = cov19.groupby(['ObservationDate', "Country"])
cov19_mean[num_cols].agg("mean").reset_index()
cov19_min = cov19.groupby(['ObservationDate', "Country"])[num_cols].agg("min").reset_index()
cov19_max = cov19.groupby(['ObservationDate', "Country"])[num_cols].agg("max").reset_index()
cov19_sum = cov19.groupby(['ObservationDate', "Country"])
cov19_sum[num_cols].agg("sum").reset_index()

df_agg = {"Mean":cov19_mean, "Min":cov19_min, "Max":cov19_max, "Sum":cov19_sum}

with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation',
		options = ['Data Cleaning','Exploratory Analysis', 'Data Analysis'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['book', 'bar-chart', 'boxes'],
		default_index = 0,
		)
	
if selected=='Data Cleaning':
	st.title("The Cleaning Process: ")	
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
	st.dataframe(countrycode.head(10))
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
	st.dataframe(cov19.head(10))
    
if selected == 'Exploratory Analysis':
    st.title("Exploratory Analysis: ")
    st.subheader("Interactive Line Chart")
    col1, col2 = st.columns([3,5])
    with st.form("Interactive Line Chart"):
        country_option=col1.selectbox('Select a country:',np.sort(cov19['Country'].unique()), key = 2)
        case_option=col1.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=4)
        agg_option = col1.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 10)
        submitted=st.form_submit_button("Submit to generate a line chart: ")
        if submitted:
            df1 = df_agg[agg_option]
            fig=px.scatter(df1[df1['Country']==country_option],x="ObservationDate",
            y=case_option,hover_name='ObservationDate', height = 800, width = 750)
            col2.plotly_chart(fig)
    
    st.subheader("Interactive Comparison")        
    col3, col4 = st.columns([3,5])
    with st.form("Interactive Comparison"):
        country_option2=col3.multiselect('Select up to 5 countries',cov19['Country'].unique(),max_selections=5,default=['Afghanistan'])
        case_option2=col3.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=5)
        agg_option2 = col3.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 11)
        log_option2 = col3.checkbox('log() the y-axis?')
        submitted2=st.form_submit_button("Submit to compare between countries: ")
        if submitted2:
            df2 = df_agg[agg_option2]
            fig2=px.scatter(df2[df2['Country'].isin(country_option2)],x="ObservationDate",
            y=case_option2,hover_name='ObservationDate', height = 800, width = 750, color='Country', log_y = log_option2)
            col4.plotly_chart(fig2)
            
    st.subheader("Interactive Bar Chart")
    col5, col6 = st.columns([3,5])
    with st.form("Interactive Bar Chart"):
        country_option3=col5.selectbox('Select a country:',np.sort(cov19['Country'].unique()), key = 3)
        case_option3=col5.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=6)
        agg_option3 = col5.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 12)
        submitted3=st.form_submit_button("Submit to generate a bar chart: ")
        if submitted3:
            df3 = df_agg[agg_option3]
            fig3=px.bar(df3[df3['Country']==country_option3], x="ObservationDate",
            y=case_option3,hover_name='ObservationDate', height = 800, width = 750)
            col6.plotly_chart(fig3)
            
    st.subheader("Interactive World Map")
    col7, col8 = st.columns([3,5])
    with st.form("Interactive World Map"):
        case_option4=col7.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=7)
        agg_option4 = col7.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 13)
        submitted4=st.form_submit_button("Submit to generate a world map: ")
        if submitted4:
            df4 = df_agg[agg_option4]
            fig4= px.choropleth(cov19.groupby("Country").sum().reset_index(), 
              locations = "Country", 
              locationmode = "country names", 
              color = case_option4, 
              scope = "world",
             )
            col8.plotly_chart(fig4)
            
    st.subheader("Interactive Comparison Between Categorical and Numerical Variables")
    col9, col10 = st.columns([3,5])
    with st.form("Interactive Comparison Between Continents"):
        case_option5=col9.selectbox('Select cases:', num_cols, key=8)
        cat_option=col9.selectbox('Select cases:', cat_cols, key=8)
        submitted5=st.form_submit_button("Submit to generate a bar chart: ")
        if submitted5:
            fig5= px.line(cov19[cov19['Region']==region_option], x = "Region", y = case_option, color = "Region")
            col10.plotly_chart(fig5)
            
if selected=='Data Analysis':
    st.title("Top 3 countries in confirmed cases: ")
    country_optionss1 = ["US", "India", "France"]
    case_options1 = "Confirmed"
    figs1=px.scatter(cov19_sum[cov19_sum['Country'].isin(country_optionss1)],x="ObservationDate",
    y=case_options1,hover_name='ObservationDate', height = 800, width = 750, color='Country')
    st.plotly_chart(figs1)
    
    st.title("Growth of confirmed cases in China: ")
    figcn=px.scatter(cov19_sum[cov19_sum['Country']=="China"],x="ObservationDate",
    y="Confirmed",hover_name='ObservationDate', height = 800, width = 750)
    st.plotly_chart(figcn)
