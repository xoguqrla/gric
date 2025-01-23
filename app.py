import streamlit as st
import plotly.graph_objects as go

# Header Section
st.markdown("""
# **DRUM**
### AI-Based Crop Growth Analysis and Quality Certification System
""", unsafe_allow_html=True)

# Farm Information Section
st.header("Farm Information")
st.write("""
- **Farm Name**: Sunny Valley Farms  
- **Variety**: Shine Tomatoes  
- **GAP Certification**: Certified  
- **Location**: California, USA
""")

# Nutrition Changes Table
st.header("Nutrition Changes Over 3 Months")
data = {
    "Date": [
        "2023-09-01", "2023-09-15", "2023-09-30", "2023-10-15",
        "2023-10-31", "2023-11-15", "2023-11-30", "2023-12-15"
    ],
    "Sweetness (Brix)": [5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.2, 8.5],
    "Acidity (pH)": [4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5],
    "Vitamin C (mg/100g)": [15, 17, 20, 22, 25, 28, 30, 32],
}
st.table(data)

# Nutritional Changes Graph
st.header("Nutritional Changes Graph")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data["Date"], y=data["Sweetness (Brix)"], mode='lines+markers', name='Sweetness (Brix)'))
fig.add_trace(go.Scatter(x=data["Date"], y=data["Acidity (pH)"], mode='lines+markers', name='Acidity (pH)'))
fig.add_trace(go.Scatter(x=data["Date"], y=data["Vitamin C (mg/100g)"], mode='lines+markers', name='Vitamin C (mg/100g)'))
fig.update_layout(title="Nutritional Changes Over 3 Months", xaxis_title="Date", yaxis_title="Values")
st.plotly_chart(fig)

# Interactive Section (Optional)
st.header("Explore Data Interactively")
selected_date = st.selectbox("Select a Date to View Details", data["Date"])
selected_index = data["Date"].index(selected_date)
st.write(f"**Sweetness (Brix)**: {data['Sweetness (Brix)'][selected_index]}") 
st.write(f"**Acidity (pH)**: {data['Acidity (pH)'][selected_index]}") 
st.write(f"**Vitamin C (mg/100g)**: {data['Vitamin C (mg/100g)'][selected_index]}") 

# Footer
st.markdown("""
---
© 2025 DRUM. All rights reserved.
""")
