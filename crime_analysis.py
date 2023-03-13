import pandas as pd
import streamlit as st
import altair as alt

# Read in the Michigan crime data
url = 'https://www.michigan.gov/documents/msp/Crime_in_Michigan_2021_745549_7.xlsx'
df = pd.read_excel(url, skiprows=2, sheet_name='Table 1', header=[0,1])

# Rename columns for easier access
df.columns = [f'{col[0]}_{col[1].replace(" ", "_")}' for col in df.columns]

# Create a sidebar with filtering options
st.sidebar.title('Filter Options')
offense = st.sidebar.selectbox('Select Offense', options=df.columns[1:])

# Filter the data by offense
filtered_df = df[['Offense_Category', offense]].dropna()

# Create a bar chart showing the number of offenses by offense category
st.title(f'{offense} Offenses')
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Offense_Category:N', sort=alt.EncodingSortField(field=offense, order='descending')),
    y=alt.Y(offense, title='Number of Offenses'),
    tooltip=[offense]
).properties(
    width=700,
    height=500
)
st.altair_chart(chart)

# Create a table showing the top 10 counties for the selected offense
st.title(f'Top 10 Counties for {offense} Offenses')
county_df = df[['County', offense]].dropna().sort_values(offense, ascending=False).head(10)
st.table(county_df)
