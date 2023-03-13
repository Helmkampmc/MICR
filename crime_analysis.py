import pandas as pd
import streamlit as st
import altair as alt

# Read in the crime data
url = 'https://www.michigan.gov/msp/-/media/Project/Websites/msp/micr-assets/2021/Agency-Crime-Stats_2021.xlsx'
df = pd.read_excel(url)

# Rename columns for easier access
df.columns = [col.replace(" ", "_") for col in df.columns]

# Create a sidebar with filtering options
st.sidebar.title('Filter Options')
filter_col = st.sidebar.selectbox('Select Column to Filter By', options=df.columns)

# Create a filter for the selected column
filter_val = st.sidebar.text_input(f'Select Value for {filter_col}', '')

# Filter the data by the selected column and value
if filter_val != '':
    filtered_df = df[df[filter_col].str.contains(filter_val, case=False)]
else:
    filtered_df = df

# Create a title for the app
st.title('Michigan Crime Data')

# Create a bar chart showing the number of incidents by agency type
st.title('Number of Incidents by Agency Type')
chart1 = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Agency_Type:N', sort=alt.EncodingSortField(field='Total_Incidents', order='descending')),
    y=alt.Y('Total_Incidents:Q', title='Number of Incidents'),
    tooltip=['Agency_Type', 'Total_Incidents']
).properties(
    width=700,
    height=500
)
st.altair_chart(chart1)

# Create a bar chart showing the number of arrests by agency type
st.title('Number of Arrests by Agency Type')
chart2 = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Agency_Type:N', sort=alt.EncodingSortField(field='Total_Arrests', order='descending')),
    y=alt.Y('Total_Arrests:Q', title='Number of Arrests'),
    tooltip=['Agency_Type', 'Total_Arrests']
).properties(
    width=700,
    height=500
)
st.altair_chart(chart2)

# Create a table showing the total incidents and arrests for each agency type
st.title('Total Incidents and Arrests by Agency Type')
sum_df = filtered_df.groupby('Agency_Type')[['Total_Incidents', 'Total_Arrests']].sum()
st.table(sum_df)
