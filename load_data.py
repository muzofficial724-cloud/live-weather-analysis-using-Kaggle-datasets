import pandas as pd

def prepare_dataset(filepath):
    df = pd.read_csv(filepath)
    
    # Use correct columns from your dataset
    df = df[['Formatted Date', 'Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Precip Type']]
    df.rename(columns={
    'Formatted Date': 'Date',
    'Temperature (C)': 'Temp',
    'Wind Speed (km/h)': 'Wind',
    'Precip Type': 'Rain'
}, inplace=True)
    
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    df.dropna(inplace=True)
    
    # Use day of year as numeric input
    df['Day'] = df['Date'].dt.dayofyear
    # Convert precipitation type to numerical
    df['Rain'] = df['Rain'].apply(lambda x: 1 if x == 'rain' else 0)
    X = df[['Day', 'Humidity', 'Wind', 'Rain']]      # Features
    y = df['Temp']          # Target variable
    return X, y



