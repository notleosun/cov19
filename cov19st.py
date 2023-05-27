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
cov19['Month'] = cov19['ObservationDate'].dt.strftime('%B %Y')

ede = cov19["Month"].unique()

seasons_dict = {
  'January 2020': 'Winter 2019',
  'February 2020': 'Winter 2019',
  'March 2020': 'Spring 2020',
  'April 2020': 'Spring 2020',
  'May 2020': 'Spring 2020',
  'June 2020': 'Summer 2020',
  'July 2020': 'Summer 2020',
  'August 2020': 'Summer 2020',
  'September 2020': 'Autumn 2020',
  'October 2020': 'Autumn 2020',
  'November 2020': 'Autumn 2020',
  'December 2020': 'Winter 2020',
  'January 2021': 'Winter 2020',
  'February 2021': 'Winter 2020',
  'March 2021': 'Spring 2021',
  'April 2021': 'Spring 2021',
  'May 2021': 'Spring 2021',
}

cov19["Season"] = cov19["Month"].replace(seasons_dict)

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
reg_dict2 = {
    "Latin America and the Caribbean":"Latin America",
    "Australia and New Zealand":"ANZ"}
cov19["Region"] = cov19.Region.replace(reg_dict2)

eee = cov19["Country"].sort_values(ascending = True).unique()

population = {
    'Afghanistan': 38928341,
    'Albania': 2877797,
    'Algeria': 43851044,
    'Andorra': 77265,
    'Angola': 32866272,
    'Antigua and Barbuda': 97928,
    'Argentina': 45267449,
    'Armenia': 2963234,
    'Aruba': 106766,
    'Australia': 25788216,
    'Austria': 9006398,
    'Azerbaijan': 10139177,
    'Bahamas': 393244,
    'Bahrain': 1701575,
    'Bangladesh': 164689383,
    'Barbados': 287375,
    'Belarus': 9449323,
    'Belgium': 11555997,
    'Belize': 397628,
    'Benin': 12123198,
    'Bhutan': 771608,
    'Bolivia': 11673021,
    'Bosnia and Herzegovina': 3280815,
    'Botswana': 2351627,
    'Brazil': 213993437,
    'Brunei': 459500,
    'Bulgaria': 6948445,
    'Burkina Faso': 20903278,
    'Burma': 54817919,
    'Burundi': 11890784,
    'Cabo Verde': 555987,
    'Cambodia': 16718971,
    'Cameroon': 26545864,
    'Canada': 37742154,
    'Cape Verde': 555987,
    'Cayman Islands': 65722,
    'Central African Republic': 4829764,
    'Chad': 16425859,
    'Channel Islands': 173859,
    'Chile': 19116209,
    'China': 1444216105,
    'Colombia': 50882891,
    'Comoros': 869601,
    'Costa Rica': 5094118,
    'Croatia': 4105267,
    'Cuba': 11326616,
    'Curacao': 164093,
    'Cyprus': 1207359,
    'Czech Republic': 10708981,
    'Denmark': 5792202,
    'Diamond Princess': 3711,
    'Djibouti': 1009717,
    'Dominica': 71991,
    'Dominican Republic': 10847910,
    'East Timor': 1318442,
    'Ecuador': 17643054,
    'Egypt': 102334404,
    'El Salvador': 6486205,
    'Equatorial Guinea': 1402985,
    'Eritrea': 3546427,
    'Estonia': 1326535,
    'Eswatini': 1160164,
    'Ethiopia': 114963583,
    'Faroe Islands': 48863,
    'Fiji': 896444,
    'Finland': 5540718,
    'France': 65273511,
    'French Guiana': 309500,
    'Gabon': 2225734,
    'Gambia': 2416668,
    'Georgia': 3989167,
    'Germany': 83783942,
    'Ghana': 31072945,
    'Gibraltar': 33718,
    'Greece': 10423054,
    'Greenland': 56770,
    'Grenada': 113021,
    'Guadeloupe': 400127,
    'Guam': 168486,
    'Guatemala': 18504323,
    'Guernsey': 67052,
    'Guinea': 13398185,
    'Guinea Bissau': 2019629,
    'Guyana': 790326,
    'Haiti': 11402533,
    'Holy See': 802,
    'Honduras': 10170231,
    'Hong Kong': 7507523,
    'Hungary': 9660351,
    'Iceland': 343518,
    'India': 1393409038,
    'Indonesia': 276361783,
    'Iran': 84567666,
    'Iraq': 41925168,
    'Ireland': 4982902,
    'Israel': 9216900,
    'Italy': 60367481,
    'Ivory Coast': 28286022,
    'Jamaica': 2961161,
    'Japan': 125961625,
    'Jersey': 107800,
    'Jordan': 10203140,
    'Kazakhstan': 18991322,
    'Kenya': 54899873,
    'Kiribati': 121134,
    'Kosovo': 1810463,
    'Kuwait': 4270571,
    'Kyrgyzstan': 6622100,
    'Laos': 7375318,
    'Latvia': 1886202,
    'Lebanon': 6825445,
    'Lesotho': 2159654,
    'Liberia': 5260824,
    'Libya': 7018777,
    'Liechtenstein': 38210,
    'Lithuania': 2722289,
    'Luxembourg': 634730,
    'MS Zaandam': 0,
    'Macau': 649342,
    'Madagascar': 29125963,
    'Malawi': 19930812,
    'Malaysia': 32710179,
    'Maldives': 540544,
    'Mali': 20250834,
    'Malta': 514564,
    'Marshall Islands': 58791,
    'Martinique': 375265,
    'Mauritania': 4815928,
    'Mauritius': 1265740,
    'Mayotte': 279471,
    'Mexico': 131169000,
    'Micronesia': 115023,
    'Moldova': 2658825,
    'Monaco': 39244,
    'Mongolia': 3323920,
    'Montenegro': 628062,
    'Morocco': 37565147,
    'Mozambique': 32077672,
    'Namibia': 2587801,
    'Nepal': 29609623,
    'Netherlands': 17172924,
    'New Zealand': 5084300,
    'Nicaragua': 6624554,
    'Niger': 24894871,
    'Nigeria': 211400708,
    'North Ireland': 1893816,
    'North Macedonia': 2083374,
    'Norway': 5456300,
    'Oman': 5183889,
    'Others':0,
    'Pakistan': 225199937,
    'Palestine': 5152921,
    'Panama': 4302990,
    'Papua New Guinea': 9139599,
    'Paraguay': 7132538,
    'Peru': 33055432,
    'Philippines': 110471802,
    'Poland': 38379000,
    'Portugal': 10191409,
    'Puerto Rico': 2933408,
    'Qatar': 2889284,
    'Republic of Ireland': 4994724,
    'Republic of the Congo': 5518092,
    'Reunion': 895312,
    'Romania': 19241458,
    'Russia': 144498215,
    'Rwanda': 12952209,
    'Saint Barthelemy': 9877,
    'Saint Kitts and Nevis': 53192,
    'Saint Lucia': 184386,
    'Saint Vincent and the Grenadines': 111266,
    'Samoa': 199000,
    'San Marino': 33938,
    'Sao Tome and Principe': 219159,
    'Saudi Arabia': 34813871,
    'Senegal': 16743930,
    'Serbia': 6908224,
    'Seychelles': 99727,
    'Sierra Leone': 7901454,
    'Singapore': 5850342,
    'Slovakia': 5456362,
    'Slovenia': 2078938,
    'Solomon Islands': 669823,
    'Somalia': 15893219,
    'South Africa': 59622350,
    'South Korea': 51709098,
    'South Sudan': 11296356,
    'Spain': 46757980,
    'Sri Lanka': 21803000,
    'St. Martin': 38666,
    'Sudan': 43849269,
    'Suriname': 591919,
    'Sweden': 10302731,
    'Switzerland': 8654622,
    'Syria': 17500657,
    'Taiwan': 23783971,
    'Tajikistan': 9537645,
    'Tanzania': 61498421,
    'Thailand': 69950800,
    'Timor-Leste': 1328974,
    'Togo': 8278737,
    'Trinidad and Tobago': 1399491,
    'Tunisia': 11818619,
    'Turkey': 83429616,
    'UK': 68207116,
    'US': 332915073,
    'Uganda': 45711874,
    'Ukraine': 43733762,
    'United Arab Emirates': 9890402,
    'Uruguay': 3461734,
    'Uzbekistan': 33736356,
    'Vanuatu': 299882,
    'Vatican City': 801,
    'Venezuela': 28515829,
    'Vietnam': 97490000,
    'West Bank and Gaza': 4685306,
    'Yemen': 28498687,
    'Zambia': 18920657,
    'Zimbabwe': 15092171}

cov19["Population"] = cov19.Country.replace(population).astype(int)
cov19["ConfirmedPC"] = cov19["Confirmed"] / cov19["Population"]
cov19["DeathsPC"] = cov19["Deaths"] / cov19["Population"]
cov19["RecoveredPC"] = cov19["Recovered"] / cov19["Population"]

num_cols = ["Confirmed", "Deaths", "Recovered", "ConfirmedPC", "DeathsPC", "RecoveredPC"]
cat_cols = ['ObservationDate', "Province/State", "Country", "Region", "Continent", "Month"]

cov19_mean = cov19.groupby(['ObservationDate', "Country"])[num_cols].agg("mean").reset_index()
cov19_min = cov19.groupby(['ObservationDate', "Country"])[num_cols].agg("min").reset_index()
cov19_max = cov19.groupby(['ObservationDate', "Country"])[num_cols].agg("max").reset_index()
cov19_sum = cov19.groupby(['ObservationDate', "Country"])[num_cols].agg("sum").reset_index()

df_agg = {"Mean":cov19_mean, "Min":cov19_min, "Max":cov19_max, "Sum":cov19_sum}

cov_disp = cov19.copy().sort_values("Country", ascending = True)
cov_disp["D/R"] = cov_disp["Deaths"] / cov_disp["Recovered"]

with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation',
		options = ['Intro + Background','Data Cleaning','Exploratory Analysis', 'Data Analysis', 'Conclusion'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['triangle','book', 'bar-chart', 'boxes', 'square'],
		default_index = 0,
		)
    
if selected== "Intro + Background":
    st.title("Introduction")
    st.subheader("In this case study, I will try to analyse a dataset of entries for the development of the Covid-19 pandemic. The case study will also feature an exploratory analysis section, for the audience to experiment with graphs themselves to achieve desired charts.")
    st.title("Background")
    st.subheader("""
The Covid-19 pandemic started in Wuhan, China during December 2019. Over three years, it has around 700 million confirmed cases and 7 million deaths.

The coronavirus pandemic was not extremely lethal, with a mortality rate of around 1%. However, it had a high mortality rate among the elderly, so the average mortality rate for regions will also depend on the population distribution. The disease was highly contagious as it is spread through droplets in the air, which is very easy for others to inhale and become infected or transmit the virus.

Furthermore, the symptoms of Covid varies between individuals, with common symptoms being pheumonia, coughing and fevers. It has also been noted that Covid can cause long term effects, such as loss of smell and taste. Following the Omicron variant in 2021, the symptoms have became less severe.

The vaccines started being developed in 2020, mainly by Moderna, Pfizer and Sinovac. A Johnson & Johnson Janssen mRNA vaccine was also authorized for emergency use in 2021. Following successful development and application of the vaccine, border measures were gradually opened by countries and became less strict.""")

    st.subheader("The reason why this case study is made is to study the development of Covid and its variants, so it would be possible to learn from such a large-scale pandemic.")
	
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
        s1, e1 = col1.slider('Select a range of dates: ', value = (pd.datetime(2020,1,22), pd.datetime(2021,5,29)), format="DD/MM/YY")
        submitted=st.form_submit_button("Submit to generate a line chart: ")
        
        if submitted:
            dr1 = pd.date_range(start=s1, end=e1, freq='D')
            df1 = df_agg[agg_option]
            mask1 = df1['ObservationDate'].isin(dr1)
            df1 = df1[mask1]
            fig=px.scatter(df1[df1['Country']==country_option],x="ObservationDate",
            y=case_option,hover_name='ObservationDate', height = 800, width = 750, title = f"Line chart of {case_option} cases in {country_option}, aggregated using {agg_option}")
            col2.plotly_chart(fig)
    
    st.subheader("Interactive Comparison")        
    col3, col4 = st.columns([3,5])
    with st.form("Interactive Comparison"):
        country_option2=col3.multiselect('Select up to 5 countries',cov19['Country'].unique(),max_selections=5,default=['Afghanistan'])
        case_option2=col3.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=5)
        agg_option2 = col3.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 11)
        log_option2 = col3.checkbox('log() the y-axis?')
        s2, e2 = col3.slider('Select a range of dates: ', value = (pd.datetime(2020,1,22), pd.datetime(2021,5,29)), format="DD/MM/YY", key = 69)
        submitted2=st.form_submit_button("Submit to compare between countries: ")
        
        if submitted2:
            dr2 = pd.date_range(start=s2, end=e2, freq='D')
            df2 = df_agg[agg_option2]
            mask2= df2['ObservationDate'].isin(dr2)
            df2 = df2[mask2]
            fig2=px.scatter(df2[df2['Country'].isin(country_option2)],x="ObservationDate",
            y=case_option2,hover_name='ObservationDate', height = 800, width = 750, color='Country', log_y = log_option2, title = f"Comparative chart of {case_option2} cases in {country_option2}, aggregated using {agg_option2}")
            col4.plotly_chart(fig2)
            
    st.subheader("Interactive Bar Chart")
    col5, col6 = st.columns([3,5])
    with st.form("Interactive Bar Chart"):
        country_option3=col5.selectbox('Select a country:',np.sort(cov19['Country'].unique()), key = 3)
        case_option3=col5.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=6)
        agg_option3 = col5.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 12)
        s3, e3 = col5.slider('Select a range of dates: ', value = (pd.datetime(2020,1,22), pd.datetime(2021,5,29)), format="DD/MM/YY", key = 96)
        submitted3=st.form_submit_button("Submit to generate a bar chart: ")
        
        if submitted3:
            dr3 = pd.date_range(start=s3, end=e3, freq='D')
            df3 = df_agg[agg_option3]
            mask3= df3['ObservationDate'].isin(dr3)
            df3 = df3[mask3]
            fig3=px.bar(df3[df3['Country']==country_option3], x="ObservationDate",
            y=case_option3,hover_name='ObservationDate', height = 800, width = 750, title = f"Bar chart of {case_option3} cases in {country_option3}, aggregated using {agg_option3}")
            col6.plotly_chart(fig3)
            
    st.subheader("Interactive World Map")
    col7, col8 = st.columns([3,5])
    with st.form("Interactive World Map"):
        case_option4=col7.selectbox('Select cases:',['Confirmed','Deaths','Recovered'], key=7)
        agg_option4 = col7.selectbox('Select how to aggregate data for duplicate dates:',['Mean','Sum','Max', 'Min'], key = 13)
        s4, e4 = col7.slider('Select a range of dates: ', value = (pd.datetime(2020,1,22), pd.datetime(2021,5,29)), format="DD/MM/YY", key = 97)
        submitted4=st.form_submit_button("Submit to generate a world map: ")
        
        if submitted4:
            dr4 = pd.date_range(start=s4, end=e4, freq='D')
            df4 = df_agg[agg_option4]
            mask4= df4['ObservationDate'].isin(dr4)
            df4 = df4[mask4]
            fig4= px.choropleth(cov19.groupby("Country").sum().reset_index(), 
              locations = "Country", 
              locationmode = "country names", 
              color = case_option4, 
              scope = "world",
              title = f"World map of {case_option4} cases, aggregated using {agg_option4}"
             )
            col8.plotly_chart(fig4)
            
    st.subheader("Interactive Comparison Between Categorical and Numerical Variables")
    col9, col10 = st.columns([3,5])
    with st.form("Interactive Comparison Between Categorical and Numerical Variables"):
        case_option5=col9.selectbox('Select cases:', num_cols, key=8)
        cat_option=col9.selectbox('Select cases:', np.setdiff1d(cat_cols, ["ObservationDate"]), key=20)
        log_y_option = col9.checkbox("log() the y-axis? ")
        s5, e5 = col9.slider('Select a range of dates: ', value = (pd.datetime(2020,1,22), pd.datetime(2021,5,29)), format="DD/MM/YY", key = 70)
        submitted5=st.form_submit_button("Submit to generate a bar chart: ")
        if submitted5:
            dr5 = pd.date_range(start=s5, end=e5, freq='D')
            mask5= cov19['ObservationDate'].isin(dr5)
            df5 = cov19[mask5]
            fig5= px.histogram(df5, x = cat_option, y = case_option, color = cat_option, log_y = log_y_option, title = f"Comparative chart of {case_option5} cases between {cat_option}s, log_y is {log_y_option}", histfunc = 'avg')
            fig5.update_xaxes(tickangle=30)
            col10.plotly_chart(fig5)
            
    st.subheader("Interactive Box Plot")
    col11, col12 = st.columns([3,5])
    with st.form("Interactive Box Plot"):
        case_option2=col11.selectbox('Select cases:', num_cols, key=9)
        cat_option2=col11.selectbox('Select cases:', np.setdiff1d(cat_cols, ["ObservationDate"]), key=21)
        log_y_option2 = col11.checkbox("log() the y-axis? ", key = 8008135)
        s6, e6 = col11.slider('Select a range of dates: ', value = (pd.datetime(2020,1,22), pd.datetime(2021,5,29)), format="DD/MM/YY", key = 75)
        submitted6=st.form_submit_button("Submit to generate a bar chart: ")
        if submitted6:
            dr6 = pd.date_range(start=s6, end=e6, freq='D')
            mask6= cov19['ObservationDate'].isin(dr6)
            df6 = cov19[mask6]
            fig6= px.box(df6, x = cat_option2, y = case_option2, color = cat_option2, log_y = log_y_option2, title = f"Box plot of {case_option} cases between {cat_option2}s, log_y is {log_y_option2}")
            col12.plotly_chart(fig6)
            
    st.subheader("Month Comparison")
    col13, col14 = st.columns([3,5])
    with st.form("Month Comparison"):
        t_option = col13.multiselect('Select up to 5 consecutive months',cov19['Month'].unique(),max_selections=5,default=['January 2020'])
        case_option7=col13.selectbox('Select cases:', num_cols, key=17)
        log_y_option7 = col13.checkbox("log() the y-axis? ", key = 8008136)
        submitted7=st.form_submit_button("Submit to generate a bar chart: ")
        if submitted7:
            gb = cov19.groupby('Month')[num_cols].agg("sum").reset_index()
            mask7= gb['Month'].isin(t_option)
            df7 = gb[mask7]
            fig7= px.histogram(df7, x = t_option, y = case_option7, log_y = log_y_option7, title = f"Box plot of {case_option7} cases between {t_option[0]} and {t_option[-1]}, log_y is {log_y_option7}")
            col14.plotly_chart(fig7)
            
    st.subheader("Month Comparison (Box Plot)")
    col15, col16 = st.columns([3,5])
    with st.form("Month Comparison (Box Plot)"):
        t_option2 = col15.multiselect('Select up to 5 consecutive months',cov19['Month'].unique(),max_selections=5,default=['January 2020'], key = 8978757)
        case_option8=col15.selectbox('Select cases:', num_cols, key=18)
        log_y_option8 = col15.checkbox("log() the y-axis? ", key = 8008139)
        submitted8=st.form_submit_button("Submit to generate a box plot: ")
        if submitted8:
            mask8= cov19['Month'].isin(t_option2)
            df8 = cov19[mask8]
            fig8= px.box(df8, x = "Month", y = case_option8, log_y = log_y_option8, title = f"Box plot of {case_option8} cases between {t_option2[0]} and {t_option2[-1]}, log_y is {log_y_option8}")
            col16.plotly_chart(fig8)  
            
    st.subheader("Region Interactive")
    col17, col18 = st.columns([3,5])
    with st.form("Region Interactive"):
        cat_option9 = col17.selectbox('Select a region: ', cov19["Region"].unique(), key = 8976757)
        case_option9=col17.selectbox('Select cases:', num_cols, key=120)
        color_option9 = col17.selectbox("Select an optional additional grouping variable: ", [None, 'Season', 'Month'], key = 1231984)
        agg_option9 = col17.selectbox("Select the aggregation option", ['sum', 'avg'], key = 983798137)
        log_y_option9 = col17.checkbox("log() the y-axis? ", key = 8008132)
        submitted9=st.form_submit_button("Submit to generate a histogram: ")
        if submitted9:
            fig9= px.histogram(cov19[cov19["Region"] == cat_option9], x = "Country", y = case_option9, log_y = log_y_option9, title = f"Box plot of {case_option9} cases in {cat_option9}, log_y is {log_y_option9}", histfunc = agg_option9, color = color_option9, barmode = 'group')
            col18.plotly_chart(fig9)      
    
if selected=='Data Analysis':
    
    st.subheader("To begin, the collected data is from official sources from different countries. A problem that arrises with such methods of data collection is that local officials may, to their own benefits, manipulate the data. Therefore, it is important to identify which countries could have had the possibility of data manipulation.")
    dis1, dis2 = st.columns([5,5])
    dis1.title("Top countries in confirmed cases: ")
    countries = ['France', 'India', 'Turkey', 'UK', 'US', 'Argentina', 'Brazil', 'Iran', 'Poland', 'Indonesia', 'Czech Republic', 'South Africa', 'Philippines', 'Iraq', 'Russia', 'Romania']
    case_options2 = "Confirmed"
    figs2=px.histogram(cov19[cov19["Country"].isin(countries)],x="Country",
    y=case_options2,hover_name='ObservationDate', height = 700, width = 700, color='Country', histfunc = 'max', color_discrete_sequence=px.colors.qualitative.Light24)
    figs2.update_layout(xaxis={'categoryorder':'total descending'})
    dis1.plotly_chart(figs2)
    
    dis2.title("Death ratios: ")
    figs3=px.histogram(cov_disp[cov_disp["Country"].isin(countries)],x="Country",
    y="D/R",hover_name='ObservationDate', height =700, width = 700, color='Country', histfunc = 'avg', color_discrete_sequence=px.colors.qualitative.Light24)
    figs3.update_layout(xaxis={'categoryorder':'total descending'})
    dis2.plotly_chart(figs3)
    
    st.markdown("### The reason why the Indian death rate appears to be so low could have been due to the lack of appropriate data sources<sup>1</sup>. To begin, most Indian deaths due to the Coronavirus had occured at home, after patients received treatment at hospitals and had returned home. This meant that sourcing data became more difficult for officials, and data sourced from hospitals are not always correct. Furthermore, crematoriums in India during the pandemic were full due to the large influx of deaths and many had to be cremated in the countryside. This meant that collecting data from cremnatoriums was not a possible option either.", unsafe_allow_html=True)
    
    st.markdown("### On the other hand, the US D/R rate seems incredible high, with an average of 3.5 deaths per recovered individual. This could be due to the United States' initial response, when many weren't properly supplied with protective equipment, and quaratine laws varied in strictness. Furthermore, although the US was one of the first countries to obtain the COVID vaccine, it was not able to widely spread it among the general population, potentially due to misinformation about the vaccine spread online. In an interview with Dr Jennifer Luzzo<sup>2</sup>, an associate professor at the Johns Hopkins School of Public Health, she stated that 'for many people, [it is] much easier to find lies about the vaccines than the truth and to find information about the benefits of these vaccines.'", unsafe_allow_html=True)
    
    dis3, dis4 = st.columns([16,4])
    dis3.title("Confirmed cases of the top 5 most populous countries: ")
    country_optionss1 = ["China", "India", "US", "Indonesia", "Pakistan"]
    case_options1 = "Confirmed"
    figs1=px.scatter(cov19_sum[cov19_sum['Country'].isin(country_optionss1)],x="ObservationDate",
    y=case_options1,hover_name='ObservationDate', height = 700, width = 1000, color='Country')
    dis3.plotly_chart(figs1)
    
    dis4.subheader("As the US and India both have large populations and are hit severely by COVID, we could infer that there is some correlation between the size of a country, population wise, and how severe COVID would become in that country. However, a visible outlier is China. Being the most populous country in the world, it has a strikingly low number of cases. Here I will zoom in on China: ")
    st.title("Growth of confirmed cases in China: ")
    
    dis5, dis6 = st.columns([10, 8])
    figcn=px.scatter(cov19_sum[cov19_sum['Country']=="China"],x="ObservationDate",
    y="Confirmed",hover_name='ObservationDate', height = 700, width = 700)
    dis5.plotly_chart(figcn)
    figs6= px.box(cov19[cov19['Country']=="China"], x = "Month", y = "Confirmed", log_y = True, height = 700, width = 500)
    dis6.plotly_chart(figs6)
    
    st.subheader("It could be seen that China's confirmed cases originally rose sharply, as it is the first country to have a COVID outbreak, but by March it slows down to a more steady rate and eventually a plateau.")
    
    st.subheader("The per Capita index is useful in identifying how well a country reacted to COVID as the cases are divided by the population, showing what percentage of the population has actually got COVID.")
    cold, cole = st.columns([1,1])
    cold.title("Top 20 in CPC")
    pc_20 = cov19.groupby('Country').agg("mean").reset_index()
    fig_cpc = px.bar(pc_20.sort_values("ConfirmedPC", ascending = False).head(20), x = "Country", y = "ConfirmedPC", height = 700, width = 700)
    cole.title("Top 20 in DPC")
    fig_dpc = px.bar(pc_20.sort_values("DeathsPC", ascending = False).head(20), x = "Country", y = "DeathsPC", height = 700, width = 700)
    cold.plotly_chart(fig_cpc)
    cole.plotly_chart(fig_dpc)
    
    st.title("Confirmed Per Capita")
    dis7, dis8, dis9 = st.columns([5,5,5])
    
    fig_reg1 = px.histogram(cov_disp[cov_disp["Region"] == "Southern Asia"], x = "Country", y = "ConfirmedPC", log_y = True, title = "Confirmed (Per Capita) Cases in Southern Asia", histfunc = 'avg', width = 450)
    fig_reg2 = px.histogram(cov_disp[cov_disp["Region"] == "Eastern Asia"], x = "Country", y = "ConfirmedPC", log_y = True, title = "Confirmed (Per Capita) Cases in Eastern Asia", histfunc = 'avg', width = 450)
    fig_reg3 = px.histogram(cov_disp[cov_disp["Region"] == "South-eastern Asia"], x = "Country", y = "ConfirmedPC", log_y = True, title = "Confirmed (Per Capita) Cases in South-Eastern Asia", histfunc = 'avg', width = 450)
    
    dis7.plotly_chart(fig_reg1)
    dis8.plotly_chart(fig_reg2)
    dis9.plotly_chart(fig_reg3)
    
    st.title("Best Countries in Combatting COVID (Confirmed Per Capita): ")
    figs9 = px.histogram(cov_disp[cov_disp["Region"] == "Latin America"], x = "Country", y = "ConfirmedPC", log_y = True, height = 900, width = 1250, histfunc = 'avg')
    st.plotly_chart(figs9)
    st.subheader("Latin America had the lowest average of CpC cases. The countries that have the largest population, such as Columbia, Mexico, Peru and Venezuela, all had relatively low CpC cases. On the other hand, Argentina had a high CpC of 0.025. It could also be noticed in the first series of graphs that China and India both have a low CpC, which is potentially due to their large population counts.")
    
    st.subheader("The D/R ratio is useful in evaluating how well a country did to combat COVID, as it reflects the effectiveness of the country's medical strategies to combat COVID. Here are the countries that have the highest D/R ratios:")
    st.title("Death to Recovery Ratio")
    figs8 = px.histogram(cov_disp, x = "Region", y = "D/R", log_y = True, height = 900, width = 1250, histfunc = 'avg')
    st.plotly_chart(figs8)
    
    
    dis10, dis11, dis12 = st.columns([5,5,5])
    
    fig_reg4 = px.histogram(cov_disp[cov_disp["Region"] == "Southern Asia"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Southern Asia", histfunc = 'avg', width = 450)
    fig_reg5 = px.histogram(cov_disp[cov_disp["Region"] == "Eastern Asia"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Eastern Asia", histfunc = 'avg', width = 450)
    fig_reg6 = px.histogram(cov_disp[cov_disp["Region"] == "Central Asia"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Central Asia", histfunc = 'avg', width = 450)
    
    dis10.plotly_chart(fig_reg4)
    dis11.plotly_chart(fig_reg5)
    dis12.plotly_chart(fig_reg6)
    
    dis13, dis14 = st.columns([5,5])
    
    fig_reg7 = px.histogram(cov_disp[cov_disp["Region"] == "Northern America"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Northern America", histfunc = 'avg', width = 675)
    fig_reg8 = px.histogram(cov_disp[cov_disp["Region"] == "Northern Europe"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Northern Europe", histfunc = 'avg', width = 675)
    
    
    dis13.plotly_chart(fig_reg7)
    dis14.plotly_chart(fig_reg8)
    
    dis15, dis16 = st.columns([5,5])
    fig_reg9 = px.histogram(cov_disp[cov_disp["Region"] == "Southern Europe"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Southern Europe", histfunc = 'avg', width = 675)
    fig_reg10 = px.histogram(cov_disp[cov_disp["Region"] == "Western Europe"], x = "Country", y = "D/R", log_y = True, title = "Death to Recovered Ratio for Countries in Western Europe", histfunc = 'avg', width = 675)
    dis15.plotly_chart(fig_reg9)
    dis16.plotly_chart(fig_reg10)
    
    st.markdown("### Countries that have low D/R ratios often have two meanings -- the country's demographic or the medical conditions are very good (e.g. UK). A good medical service in the country will mean that vaccines will be able to be easily distributed, and people with minimal responses to COVID can be easily cured. On the other hand, a country's demographic play's an import role in how the country will react to COVID. Italy for example, has 'one of the oldest populations in the world with 23.3% over age 65', according to an Oxford University case study<sup>3</sup>. THe consequences of such a demographic is that many with relatively less healthy immune systems may respond to COVID in a severe manner. When compared to South Korea, with only 14% of the population over 65, Italy's predicted number of fatalities was 1.7 times greater than South Korea.", unsafe_allow_html=True)
    
if selected== "Conclusion":
    st.header("Conclusion")
    st.subheader("In conclusion, through multiple comparisons of diffferent indexes, I find China to be the country that reacted best to COVID. This could be due to its strict policies during the outbreak, or its involvement in the development and fast applications of COVID-related vaccines.")
                 
    st.subheader("Furthermore, it is important to note that the successfulness of a country's response to COVID can depend on multiple factors outside of simply government policies, such as a country's demographic, economic ability and healthcare services.")
    
    st.header("Bibliography\n")
    st.subheader("[1] Biswas, B. S. (2020, April 27). India coronavirus: The “mystery” of low Covid-19 death rates. BBC News. https://www.bbc.co.uk/news/world-asia-india-52435463 \n")
    st.subheader("[2] Why the U.S. COVID death rate rises above other nations. (2022, February 2). [Video]. PBS NewsHour. https://www.pbs.org/newshour/show/why-the-covid-death-rate-in-the-u-s-is-so-much-higher-than-other-wealthy-nations \n")
    st.subheader("[3] Covid-19 mortality highly influenced by age demographics | University. (2020, April 17). https://www.ox.ac.uk/news/2020-04-17-covid-19-mortality-highly-influenced-age-demographics")
    
    
    
    
    
    
    
    
