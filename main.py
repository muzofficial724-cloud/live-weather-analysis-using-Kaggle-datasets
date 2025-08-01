from load_data import prepare_dataset
from train_model import *
from api_fetch import fetch_weather
from predict import predict_temperature
from forecast_prophet import forecast_temperature
from datetime import datetime


if __name__ == '__main__':
    # Step 1: Load and preprocess data
    X, y = prepare_dataset('weather.csv')
    
    # Step 2: Train model
    train_and_save_model(X, y)

    # Step 3: Fetch live weather
    temp, humidity = fetch_weather()
    wind = 10  # estimated or use OpenWeatherMap API
    rain = 1   # manually set, or use 'Precip Type' logic

    # Predict tomorrow's temp
    tomorrow = datetime.now().timetuple().tm_yday + 1
    predict_temperature(tomorrow, humidity / 100, wind, rain)


    # Prophet forecast
    print("🧭 Prophet 7-Day Forecast:")
    forecast_temperature() 



