import streamlit as st

# Slider pour longitude
longitude = st.slider("Longitude", min_value=-124.0, max_value=-114.0, value=-122.0, step=0.1)

# Slider pour latitude
latitude = st.slider("Latitude", min_value=32.0, max_value=42.0, value=37.0, step=0.1)

# Slider pour housing_median_age
housing_median_age = st.slider("Housing Median Age", min_value=1.0, max_value=52.0, value=28.0, step=1.0)

# Slider pour total_rooms
total_rooms = st.slider("Total Rooms", min_value=2.0, max_value=39320.0, value=2000.0, step=10.0)

# Slider pour total_bedrooms
total_bedrooms = st.slider("Total Bedrooms", min_value=1.0, max_value=6445.0, value=1000.0, step=1.0)

# Slider pour population
population = st.slider("Population", min_value=3.0, max_value=35682.0, value=1000.0, step=10.0)

# Slider pour households
households = st.slider("Households", min_value=1.0, max_value=6082.0, value=500.0, step=1.0)

# Slider pour median_income
median_income = st.slider("Median Income", min_value=0.5, max_value=15.0, value=5.0, step=0.1)







