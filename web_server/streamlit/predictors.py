import streamlit as st
import requests
import pandas as pd
from urllib.error import HTTPError

import graph_plot as graph_plot

WEB_SERVER_URL = 'http://localhost:5001'

# Function to display the prediction result
def display_result(result):
    if 'price_result' in st.session_state and 'predicted_price' in result:
        st.title(f"Price Prediction Result for: {result['product_name']}")

        # Display predicted price if available
        if result.get('predicted_price') is not None:
            st.subheader(f"Predicted Price: ${result['predicted_price']}")
            st.write(f"At date: {result['optional_date']}")

        # Handle errors
        if result.get('error'):
            st.error(f"Error: {result['error']}")
        else:
            # Display the prediction Graph
            try:
                graph_data = pd.read_csv(result['data_path'])
                graph_plot.plot(graph_data, result["type"])
            except HTTPError:
                del st.session_state['price_result']
                st.error(f"The graph has been un-cached")

    if 'demand_result' in st.session_state and 'predicted_demand' in result:
        st.title(f"Demand Prediction Result for: {result['product_name']}")

        # Display predicted price if available
        if result.get('predicted_price') is not None:
            st.subheader(f"Predicted Demand: ${result['predicted_demand']}")
            st.write(f"At date: {result['optional_date']}")

        # Handle errors
        if result.get('error'):
            st.error(f"Error: {result['error']}")
        else:
            # Display the prediction Graph
            try:
                graph_data = pd.read_csv(result['data_path'])
                graph_plot.plot(graph_data, result["type"])
            except HTTPError:
                del st.session_state['demand_result']
                st.error(f"The graph has been un-cached")

def prediction_form(prediction_type):
    if prediction_type == 'Price':
        endpoint = 'price_prediction'
    elif prediction_type == 'Demand':
        endpoint = 'demand_prediction'
    else:
        raise ValueError(f'Unknown prediction type: {prediction_type}')

    # Title of the application
    st.title(f'Product {prediction_type} Prediction')

    # Get the list of products
    response = requests.get(f'{WEB_SERVER_URL}/get_products')
    products = response.json()

    # Dropdown for product selection
    product_names = [product['product_name'] for product in products]
    product_name = st.selectbox("Select a product", product_names, key=f'{prediction_type}_product_name')

    # Time period input
    time_period = st.number_input("Time Period (in days)", min_value=1, step=1, key=f'{prediction_type}_time_period')

    # Optional date input
    optional_date = st.date_input("Date (YYYY-MM-DD)", value=None, key=f'{prediction_type}_date')

    # Button to predict price/demand at a specific date
    if st.button(f'Predict {prediction_type} at Specific Date'):
        # Remove previous results if exist
        if 'price_result' in st.session_state:
            del st.session_state['price_result']
        if 'demand_result' in st.session_state:
            del st.session_state['demand_result']

        selected_product = next((p for p in products if p['product_name'] == product_name), None)
        if selected_product and optional_date:
            response = requests.post(f'{WEB_SERVER_URL}/{endpoint}', json={
                'product_id': selected_product['product_id'],
                'time_period': None,
                'optional_date': optional_date.isoformat()
            })
            if response.status_code == 200:
                if prediction_type == 'Price':
                    st.session_state.price_result = response.json()  # Store the result in session state
                elif prediction_type == 'Demand':
                    st.session_state.demand_result = response.json()  # Store the result in session state
                st.rerun()  # Rerun to display result in a new function
            else:
                st.error("Failed to get prediction")
        else:
            st.warning("Please select a product and provide a valid date.")

    # Button to predict price/demand for a future period
    if st.button(f'Predict {prediction_type} for Future Period'):
        selected_product = next((p for p in products if p['product_name'] == product_name), None)
        if selected_product and time_period:
            response = requests.post(f'{WEB_SERVER_URL}/{endpoint}', json={
                'product_id': selected_product['product_id'],
                'time_period': time_period,
                'optional_date': None
            })
            if response.status_code == 200:
                if prediction_type == 'Price':
                    st.session_state.price_result = response.json()  # Store the result in session state
                elif prediction_type == 'Demand':
                    st.session_state.demand_result = response.json()  # Store the result in session state
                st.rerun()  # Rerun to display result in a new function
            else:
                st.error("Failed to get prediction")
        else:
            st.warning("Please select a product and provide a time period.")

    # Display the result if it exists in session state
    if 'price_result' in st.session_state and prediction_type == 'Price':
        display_result(st.session_state.price_result)  # Call the display function

    if 'demand_result' in st.session_state  and prediction_type == 'Demand':
        display_result(st.session_state.demand_result)  # Call the display function
