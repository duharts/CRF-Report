import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('CRF_Vacancy_Control_Dashboard.csv')

# Set up the Streamlit app
st.title('CRF Vacancy Control Dashboard')
st.write('This dashboard provides an overview of the current occupancy and unit status across CRF facilities.')

# Display the raw data
st.write("### Data Overview")
st.dataframe(df)

# Facility filter
facility_options = df['Facility Name'].unique()
selected_facility = st.selectbox('Select a Facility to view details:', facility_options)

# Filter data by selected facility
filtered_df = df[df['Facility Name'] == selected_facility]

# Display the selected facility's data
st.write(f"### Details for {selected_facility}")
st.write(filtered_df)

# Bar chart for Occupancy Rate
st.write("### Occupancy Rate across all facilities")
fig, ax = plt.subplots()
ax.bar(df['Facility Name'], df['Occupancy Rate (%)'])
ax.set_xlabel('Facility Name')
ax.set_ylabel('Occupancy Rate (%)')
ax.set_title('Current Occupancy Rate by Facility')
plt.xticks(rotation=90)
st.pyplot(fig)

# Display unoccupied units
st.write("### Unoccupied Units")
unoccupied_df = df[df['Unoccupied Units'] > 0]
st.dataframe(unoccupied_df[['Facility Name', 'Unoccupied Units', 'Available Units', 'Under Repair Units']])

# Download the filtered data as CSV
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name=f'{selected_facility}_data.csv',
    mime='text/csv',
)
