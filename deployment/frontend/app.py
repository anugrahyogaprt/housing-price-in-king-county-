from multiprocessing.sharedctypes import Value
import streamlit as st
import numpy as np
import requests

st.set_page_config(
    page_title="FTDS Phase 1 Milestone 2 - Anugrah Yoga Pratama",
    page_icon="✌️",
    initial_sidebar_state="collapsed",
    layout='centered',
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://github.com/anugrahyogaprt",
        'About': 'This is my Milestone 1\'s assignment, Enjoy :)'
    }
)

st.title("House Sales Price Prediction in King County, USA")

col1, col2, col3 = st.columns([0.5, 5, 0.5])
col2.image('housing.jpg', use_column_width=True, caption='Housing in King County', width=500)

st.write('Here we will try to predict housing prices in King County USA. Please fill out the required forms below so that the system can calculate the appropriate price for your housing.')
# ----------------------------------------------------------------------
st.subheader('Bedrooms')
bedrooms = st.select_slider(
        label='Number of bedrooms', 
        options=np.arange(1, 31),
        value=4
).item()
# ----------------------------------------------------------------------
st.subheader('Bathrooms')
bathrooms = st.select_slider(
        label='Number of bathrooms', 
        options=np.arange(1, 9),
        value=2
).item()
# ----------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
        st.subheader('Living Space')
        sqft_living = st.number_input(
                label='Apartments interior living space (Square Feet)',
                min_value=200,
                max_value=14000,
                step=10,
                value=3000
        )
with col2:
        st.subheader('Land Space')
        sqft_lot = st.number_input(
                label='Land space (Square Feet)',
                min_value=500,
                max_value=1500000,
                step=10,
                value=10000
        )
# ----------------------------------------------------------------------
st.subheader('Floors')
floors = st.select_slider(
        label='Number of floors', 
        options=np.arange(1, 5),
        value=2
).item()
# ----------------------------------------------------------------------
st.subheader('Waterfront')
waterfront_key = {'Yes': 1, 'No': 0}
waterfront = waterfront_key[
        st.selectbox(
                label='Apartment facing the sea or not', 
                options=['Yes', 'No']
        )
]
# ----------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
        st.subheader('View')
        view_key = {
                'Poor': 0,
                'Bad': 1,
                'Good': 2,
                'Very Good': 3,
                'Excellent': 4
        }
        view = view_key[
                st.radio(
                        label='How good the view', 
                        options=['Poor', 'Bad', 'Good', 'Very Good', 'Excellent'],
                        index=2
                )
        ]
with col2:
        st.subheader('Condition')
        condition_key = {
                'Poor': 1,
                'Bad': 2,
                'Good': 3,
                'Very Good': 4,
                'Excellent': 5
        }
        condition = condition_key[
                st.radio(
                        label='Condition for apartment', 
                        options=['Poor', 'Bad', 'Good', 'Very Good', 'Excellent'],
                        index=2
                )
        ]
# ----------------------------------------------------------------------
st.subheader('Grade')
grade = st.select_slider(
        label='Quality of Construction and Design', 
        options=np.arange(1, 14),
        value=7
).item()
# ----------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
        st.subheader('Above Space')
        sqft_above = st.number_input(
                label='Interior housing space that is above ground level (Square Feet)',
                min_value=200,
                max_value=9000,
                step=10,
                value=1800
        )
with col2:
        st.subheader('Basement Space')
        sqft_basement = st.number_input(
                label='Interior housing space that is below ground level (Square Feet)',
                min_value=0,
                max_value=5000,
                step=10,
                value=800
        )
# ----------------------------------------------------------------------
st.subheader('Year Built')
yr_built = st.number_input(
                label='The year the house was initially built',
                min_value=1900,
                max_value=2016,
                value=1999
)
st.subheader('Year Renovated')
yr_renovated = st.number_input(
                label='The year of the house’s last renovation. 0: Never Renovated',
                min_value=0,
                max_value=2015,
                value=0
        )
# ----------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
        st.subheader('Latitude')
        latitude = st.number_input(
                label='North South Coordinate',
                min_value=47.1559,
                max_value=47.7760,
                step=0.00001,
                format='%4f',
                value=47.6132
)
with col2:
        st.subheader('Longitude')
        longitude = st.number_input(
                label='East West Coordinate',
                min_value=-122.5190,
                max_value=-121.3150,
                step=0.00001,
                format='%4f',
                value=-122.4821
)
# ----------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
        st.subheader('Nearest Living Space')
        sqft_living15 = st.number_input(
                label='Living space for the nearest 15 neighbors (Square Feet)',
                min_value=400,
                max_value=6200,
                step=10,
                value=3000
        )
with col2:
        st.subheader('Nearest Land Space')
        sqft_lot15 = st.number_input(
                label='Land lots space of the nearest 15 neighbors (Square Feet)',
                min_value=650,
                max_value=870000,
                step=10,
                value=10000
        )
# ----------------------------------------------------------------------

# inference
data_inf = {
    'bedrooms' : bedrooms,
    'bathrooms' : bathrooms,
    'sqft_living' : sqft_living,
    'sqft_lot' : sqft_lot,
    'floors' :  floors,
    'waterfront' : waterfront,
    'view' : view,
    'condition' : condition,
    'grade' : grade,
    'sqft_above' : sqft_above,
    'sqft_basement' : sqft_basement,
    'yr_built' : yr_built,
    'yr_renovated' : yr_renovated,
    'lat' : latitude,
    'long' : longitude,
    'sqft_living15' : sqft_living15,
    'sqft_lot15' : sqft_lot15
}

# komunikasi
URL = 'https://backend-ayp10-p1m2.herokuapp.com/housing'
r = requests.post(URL, json=data_inf)
st.write('\n'*20)
if st.button('Predict Housing Price'):
        st.write('Estimated Price: ')
        st.header('US$  ' + str(int(r.json()['prediction'])))
else:
        st.write('Click to Predict')