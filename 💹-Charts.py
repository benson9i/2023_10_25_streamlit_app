# cd /Users/bennson/Desktop/DataScienceJourney/Streamlit/streamlit_published_app/
# streamlit run 💹-Charts.py

import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from prophet import Prophet
from streamlit_lottie import st_lottie

st.set_page_config(layout="centered")
st.title(":chart_with_downwards_trend: My Interactive Financial Charts")
st.subheader("Visualizing Financial Data")
st.write("With this app, you can view interactive line charts of different financial types: index, crypto, and forex.")

# Load the data
data = pd.read_csv(
    "/Users/bennson/Desktop/DataScienceJourney/Streamlit/streamlit_published_app/data/data_for_app.csv")
data['date'] = pd.to_datetime(data['date'])

# ---- widget section ----


def load_lottiefil(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


lottie_coding = load_lottiefil(
    "/Users/bennson/Desktop/DataScienceJourney/Streamlit/streamlit_published_app/lottie/coding_lottie.json")

col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.write("")

with col2:
    st_lottie(
        lottie_coding,
        height=300,
        width=300
    )

with col3:
    st.write("")

st.sidebar.header("Settings")

# Date range slider with a more explanatory label
date_range = st.sidebar.date_input(
    "Select Date Range (Drag the sliders to adjust)",
    [data['date'].min(), data['date'].max()]
)
start_date, end_date = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

# Forecasting settings
forecast_days = st.sidebar.slider('Number of days to forecast', 1, 365, 30)

# Use sections for each type in the sidebar
forex_symbols = list(data[data['type'] == 'forex']['symbol'].unique())
selected_forex = st.sidebar.multiselect("Select Forex Symbols", forex_symbols)

index_symbols = list(data[data['type'] == 'index']['symbol'].unique())
selected_index = st.sidebar.multiselect("Select Index Symbols", index_symbols)

crypto_symbols = list(data[data['type'] == 'crypto']['symbol'].unique())
selected_crypto = st.sidebar.multiselect(
    "Select Crypto Symbols", crypto_symbols)


def add_divider():
    st.markdown("---")


def forecast_data(data_for_forecast, days):
    model = Prophet(daily_seasonality=True)
    model.fit(data_for_forecast)
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast


# Reset button
reset_button = st.sidebar.button("Reset")

if reset_button:
    selected_forex, selected_index, selected_crypto = [], [], []
    st.experimental_rerun()

elif st.sidebar.button("Show Plots"):
    with st.spinner('Generating Plots...'):

        def plot_chart(data_subset, title_text, forecast_days=None):
            fig = go.Figure()
            for symbol in data_subset['symbol'].unique():
                subset = data_subset[data_subset['symbol'] == symbol]

                if forecast_days:
                    df_for_prophet = subset.rename(
                        columns={"date": "ds", "closing_price": "y"})
                    forecast = forecast_data(df_for_prophet, forecast_days)
                    fig.add_trace(go.Scatter(
                        x=forecast['ds'], y=forecast['yhat'], mode='lines', name=f"{symbol} forecast", line=dict(dash='dot')))

                fig.add_trace(go.Scatter(
                    x=subset['date'], y=subset['closing_price'], mode='lines', name=symbol))

            fig.update_layout(
                # Title settings
                title={
                    'text': title_text,
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {
                        'size': 24,
                        'color': 'white'
                    }
                },
                # Legend settings
                legend={
                    'bgcolor': 'rgba(0, 0, 0, 0)',
                    'bordercolor': 'white',
                    'borderwidth': 0.5,
                    'font': {
                        'color': 'white',
                        'size': 12
                    },
                    'x': 1.05,
                    'y': 1.05,
                    'xanchor': 'left',
                    'yanchor': 'bottom'
                },
                # Margin settings
                margin=dict(t=120, r=20, b=60, l=80),
                # Axis and tick settings
                plot_bgcolor="black",
                paper_bgcolor="black",
                font=dict(color="white"),
                xaxis=dict(
                    title="Date",
                    color='white',
                    tickfont=dict(
                        color='white'
                    ),
                    titlefont=dict(
                        color='white'
                    ),
                    linecolor='white'
                ),
                yaxis=dict(
                    title="Closing Price",
                    color='white',
                    tickfont=dict(
                        color='white'
                    ),
                    titlefont=dict(
                        color='white'
                    ),
                    linecolor='white'
                )
            )
            st.plotly_chart(fig)

        # Forex Plot
        if selected_forex:
            forex_data = filtered_data[filtered_data['symbol'].isin(
                selected_forex)]
            plot_chart(forex_data, "Forex Analysis", forecast_days)
            add_divider()

        # Index Plot
        if selected_index:
            index_data = filtered_data[filtered_data['symbol'].isin(
                selected_index)]
            plot_chart(index_data, "Index Analysis", forecast_days)
            add_divider()

        # Crypto Plot
        if selected_crypto:
            crypto_data = filtered_data[filtered_data['symbol'].isin(
                selected_crypto)]
            plot_chart(crypto_data, "Crypto Analysis", forecast_days)

    st.success('Plotting Complete!')

else:
    st.write("Make your selections in the sidebar, then press 'Show Plots'!")


lottie_weird = load_lottiefil(
    "/Users/bennson/Desktop/DataScienceJourney/Streamlit/streamlit_published_app/lottie/weird_lottie.json")

col1, col2, col3 = st.columns([1,2,1], gap="small")
with col1:
    st.write("")

with col2:
    st_lottie(
        lottie_weird,
        height=300,
        width=300
    )

with col3:
    st.write("")
