import streamlit as st
import pandas as pd

# Load data from GitHub

df = pd.read_csv("mich_crime2021.csv")
df=df.dropna()
df['ORI - Agency'] = df['ORI - Agency'].str.replace('Total', '')
df = df[df['ORI - Agency'].str.contains("MSP") == False]

# Create dropdown for selecting ORI - Agency
ori_list = df['ORI - Agency'].unique()
ori_selection = st.selectbox('Select an ORI - Agency:', ori_list)
ori_list = sorted(df['ORI - Agency'].unique())
ori_selection = st.selectbox('Select an ORI - Agency:', ori_list)

# Filter data based on ORI - Agency selection
filtered_df = df[df['ORI - Agency'] == ori_selection]
filtered_df=filtered_df.groupby('MICR Offense').sum()

# Display filtered data in Streamlit
st.write(f'### Michigan Crime Data (2021) - {ori_selection}')
st.write(filtered_df)


# Show bar chart of crime types for filtered data
st.write(f'### Crimes by Type - {ori_selection}')
crime_counts = filtered_df
crime_counts=crime_counts.nlargest(5, "Offenses")
st.bar_chart(crime_counts)


