from prophet import Prophet
import pandas as pd

def forecast_temperature():
    df = pd.read_csv('weather.csv')
    df = df[df['Formatted Date'].notnull()]  # remove NaNs
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
    df['Formatted Date'] = df['Formatted Date'].dt.tz_convert(None)
    df = df.rename(columns={'Formatted Date': 'ds', 'Temperature (C)': 'y'})

    df['ds'] = pd.to_datetime(df['ds'], utc=True)
    df['ds'] = df['ds'].dt.tz_convert(None)

    model = Prophet()
    from datetime import datetime
    today = pd.DataFrame([{
    'ds': datetime.today().replace(hour=0, minute=0),
    'y': 28.65  # use live temp or mean temp
    }])
    df = pd.concat([df, today], ignore_index=True)

    model.fit(df)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    for row in forecast.tail(7).itertuples():
        print(f"{row.ds.strftime('%Y-%m-%d')} → {row.yhat:.2f}°C")

    return forecast