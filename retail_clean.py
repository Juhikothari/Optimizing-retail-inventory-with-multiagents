# Retail Streamlit App (cleaned and enhanced)
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Retail AI Dashboard", layout="wide")

# Sidebar
st.sidebar.title("Retail Dashboard Navigation")
section = st.sidebar.radio("Go to", ["📊 Sales Forecasting", "📦 Inventory Management", "💰 Pricing Optimization"])

# Load data with caching
@st.cache_data
def load_data():
    try:
        df_demand = pd.read_csv("demand_forecasting.csv")
        df_inventory = pd.read_csv("inventory_monitoring.csv")
        df_pricing = pd.read_csv("pricing_optimization.csv")
        return df_demand, df_inventory, df_pricing
    except FileNotFoundError:
        st.error("One or more required CSV files not found.")
        return None, None, None

df_demand, df_inventory, df_pricing = load_data()

# --- Section 1: Sales Forecasting ---
if section == "📊 Sales Forecasting":
    st.title("📊 Sales Forecasting")
    if df_demand is not None:
        st.write("### Sample Demand Data")
        st.dataframe(df_demand.head())
        # Future: Insert forecasting model here
    else:
        st.warning("No demand data available.")

# --- Section 2: Inventory Management ---
elif section == "📦 Inventory Management":
    st.title("📦 Inventory Monitoring & Redistribution")
    if df_inventory is not None:
        df_inventory.columns = df_inventory.columns.str.lower().str.strip()
        df_inventory = df_inventory.rename(columns={
            'product id': 'product',
            'store id': 'store',
            'stock levels': 'stock',
            'reorder point': 'threshold'
        })

        low_stock = df_inventory[df_inventory['stock'] < df_inventory['threshold']]
        high_stock = df_inventory[df_inventory['stock'] > df_inventory['threshold'] * 1.5]

        st.write("### Inventory Redistribution Plan")
        for _, low_row in low_stock.iterrows():
            matches = high_stock[(high_stock['product'] == low_row['product']) &
                                 (high_stock['store'] != low_row['store'])]
            if not matches.empty:
                match = matches.iloc[0]
                transfer_qty = int(min(
                    match['stock'] - match['threshold'],
                    low_row['threshold'] - low_row['stock']
                ))
                if transfer_qty > 0:
                    st.success(f"Transfer {transfer_qty} units of '{low_row['product']}'                         from Store {match['store']} ➡️ Store {low_row['store']}")
                else:
                    st.warning(f"'{low_row['product']}' can't be transferred due to low buffer.")
            else:
                st.error(f"No high-stock match found for '{low_row['product']}'")
    else:
        st.warning("No inventory data available.")

# --- Section 3: Pricing Optimization ---
elif section == "💰 Pricing Optimization":
    st.title("💰 Pricing Optimization")
    if df_pricing is not None:
        df_pricing = df_pricing.rename(columns={
            'Product ID': 'product',
            'Store ID': 'store',
            'Price': 'price',
            'Sales Volume': 'sales',
            'Storage Cost': 'storage'
        })

        X = df_pricing[['sales', 'storage']]
        y = df_pricing['price']

        @st.cache_resource
        def train_model(X, y):
            model = LinearRegression()
            model.fit(X, y)
            return model

        model = train_model(X, y)
        df_pricing['optimized_price'] = model.predict(X)
        df_pricing['price_change_%'] = ((df_pricing['optimized_price'] - df_pricing['price']) / df_pricing['price']) * 100

        st.write("### Optimized Pricing Suggestions")
        st.dataframe(df_pricing[['product', 'store', 'price', 'optimized_price', 'price_change_%']].round(2))
    else:
        st.warning("No pricing data available.")
