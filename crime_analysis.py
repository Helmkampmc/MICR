import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from GitHub

df = pd.read_csv("mich_crime2021.csv")
df=df.dropna()
df['ORI - Agency'] = df['ORI - Agency'].str.replace('Total', '')
df = df[df['ORI - Agency'].str.contains("MSP") == False]

# Create dropdown for selecting ORI - Agency
ori_list = sorted(df['ORI - Agency'].unique())
ori_selection = st.selectbox('Select an ORI - Agency:', ori_list, index=0)

# Filter data based on ORI - Agency selection
filtered_df = df[df['ORI - Agency'] == ori_selection]
filtered_df=filtered_df.groupby('MICR Offense').sum()

# Display filtered data in Streamlit
st.write(f'### Michigan Crime Data (2021) - {ori_selection}')
st.write(filtered_df.style.set_table_styles([{'selector': 'thead', 'props': [('background-color', '#393939'), ('color', 'white')]}, {'selector': 'tbody', 'props': [('border-color', '#393939')]}]), full_width=True)



# Show bar chart of crime types for filtered data
st.write(f'### Top 5 Crimes - {ori_selection}')
crime_counts = filtered_df.nlargest(5, "Offenses")
fig = px.pie(crime_counts, values='Offenses', names=crime_counts.index)
st.plotly_chart(fig)

st.write('All data displayed is current as of 2021 as that is the most up-to-date publicly available Michigan crime data. Additional crime data can be found here: https://www.michigan.gov/msp/divisions/cjic/micr/annual-reports')
