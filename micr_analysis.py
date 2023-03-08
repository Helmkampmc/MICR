import pandas as pd
import streamlit as st

#read crime data from MICR
data = pd.read_excel('agency_crime_statistics_report_2020.xlsx', skiprows=1)
data=data.fillna(method="ffill")
data = data.iloc[1: , :]

data['Agency'] = data['ORI - Agency'].str.split('-').str[1]
data['Criminal Offense'] = data['MICR Offense'].str.split('-').str[1]

old_cols = data.columns.values 
new_cols= ['Agency', "Crime Against", 'Criminal Offense', "Offenses", 'Incidents', '2020 Crimes', "2019 Crimes"]
data = data.reindex(columns=new_cols)

data = data[data['Criminal Offense'].str.contains("[Tt]otal") == False]
data = data[data["Crime Against"].str.contains("[Tt]otal") == False]
data = data[data["Agency"].str.contains("MSP") == False]
data = data[data["Agency"].str.contains("County") == False]

data['Agency'] = data['Agency'].str.lstrip()
data['Criminal Offense'] = data['Criminal Offense'].str.lstrip()
st.write(data)
