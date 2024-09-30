import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data: Extracted from the PDF
data = {
    "Facility Name": ["Icahn House", "House East", "Hope House", "Kenilworth", "Park Overlook Stabilization",
                      "Ellington", "Apollo", "Lenox", "Light House", "Comfort Inn", "Best Western", "Park West",
                      "Belnord", "Cauldwell", "Union Hall", "Union Hall Drop in"],
    "Total Units": [65, 192, 51, 200, 91, 83, 43, 41, 240, 101, 101, 113, 130, 66, 200, 40],
    "Available Units": [3, 1, 5, 0, 1, 4, 2, 0, 22, 1, 2, 4, 0, 1, 1, 0],
    "Reserved Units": [0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 6, 0],
    "Maintenance Units": [0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 1, 0, 0, 0, 0, 0],
    "Under Repair Units": [2, 1, 2, 2, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    "Long Term Repair Units": [1, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 3, 0, 0],
    "Other Units": [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    "Renovated Units": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0],
    "Unoccupied Units": [10, 8, 8, 2, 1, 5, 3, 0, 31, 6, 8, 8, 0, 6, 7, 0],
    "Occupied Units": [55, 184, 43, 198, 90, 78, 40, 41, 209, 95, 93, 105, 130, 60, 173, 37],
    "Occupancy Rate (%)": [85, 96, 84, 99, 99, 94, 93, 100, 87, 94, 92, 93, 100, 91, 87, 93]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Title for the app
st.title("CRF Vacancy Control Dashboard")

# Display the raw data as a table
st.write("### Facility Data Overview")
st.dataframe(df)

# Graph 1: Occupancy Rate Trend
st.write("### Occupancy Rate by Facility")
fig, ax = plt.subplots()
ax.barh(df['Facility Name'], df['Occupancy Rate (%)'])
ax.set_xlabel('Occupancy Rate (%)')
ax.set_title('Current Occupancy Rate by Facility')
st.pyplot(fig)

# Graph 2: Unoccupied Units Trend
st.write("### Unoccupied Units by Facility")
fig2, ax2 = plt.subplots()
ax2.barh(df['Facility Name'], df['Unoccupied Units'], color='orange')
ax2.set_xlabel('Unoccupied Units')
ax2.set_title('Unoccupied Units by Facility')
st.pyplot(fig2)

# Graph 3: Breakdown of Unit Status (Stacked Bar Chart)
st.write("### Unit Status Breakdown by Facility")
df_status = df[['Facility Name', 'Available Units', 'Reserved Units', 'Maintenance Units', 
                'Under Repair Units', 'Long Term Repair Units', 'Other Units']]

# Plot stacked bar chart
fig3, ax3 = plt.subplots()
df_status.set_index('Facility Name').plot(kind='bar', stacked=True, ax=ax3)
ax3.set_ylabel('Number of Units')
ax3.set_title('Breakdown of Unit Status by Facility')
st.pyplot(fig3)

# Download data option
st.write("### Download Data")
st.download_button(
    label="Download data as CSV",
    data=df.to_csv(index=False),
    file_name='CRF_Vacancy_Control_Data.csv',
    mime='text/csv'
)
