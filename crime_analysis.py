import pandas as pd
import streamlit as st

# Read in the Michigan crime data
df = pd.read_excel("Agency Crime Stats_2021.xlsx", skiprows=2, sheet_name='Table 7', header=[0,1,2])

# Rename columns for easier access
df.columns = [f'{col[0]}_{col[1].replace(" ", "_")}_{col[2].replace(" ", "_")}' for col in df.columns]

# Create a sidebar with filtering options
st.sidebar.title('Filter Options')
police_dept = st.sidebar.selectbox('Select Police Department', options=df['Agency_Name_County'].unique())

# Filter the data by police department
filtered_df = df[df['Agency_Name_County'] == police_dept]

# Create a table showing the top 5 crimes for the selected police department
st.title(f'Top 5 Crimes for {police_dept}')
crime_df = filtered_df[['Offense_Description', 'Total_Offenses']].dropna().sort_values('Total_Offenses', ascending=False).head(5)
st.table(crime_df)
