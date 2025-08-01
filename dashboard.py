import streamlit as st
from forecast_prophet import forecast_temperature

st.title("🌦️ Gujranwala Weather Forecast")

forecast = forecast_temperature()
st.subheader("📅 7-Day Temperature Forecast")
st.line_chart(forecast[['ds', 'yhat']].set_index('ds'))