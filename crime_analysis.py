import streamlit as st
import pandas as pd

# Load data from GitHub

df = pd.read_csv("Michigan_crime_2021.csv")

# Create dropdown for selecting ORI - Agency
ori_list = df['ORI - Agency'].unique()
ori_selection = st.selectbox('Select an ORI - Agency:', ori_list)

# Filter data based on ORI - Agency selection
filtered_df = df[df['ORI - Agency'] == ori_selection]

# Display filtered data in Streamlit
st.write(f'### Michigan Crime Data (2021) - {ori_selection}')
st.write(filtered_df)

# Show summary statistics for filtered data
st.write(f'### Summary Statistics - {ori_selection}')
st.write(filtered_df.describe())

# Show bar chart of crime types for filtered data
st.write(f'### Crimes by Type - {ori_selection}')
crime_counts = filtered_df['Offense Category'].value_counts()
st.bar_chart(crime_counts)

