import pandas as pd
import joblib

def predict_temperature(day, humidity, wind, rain):
    model = joblib.load('weather_model.pkl')
    
    input_df = pd.DataFrame([{
        'Day': day,
        'Humidity': humidity / 100,  # 🧠 Convert to scale 0-1
        'Wind': wind,
        'Rain': rain
    }])


    print("🔍 Input to model:\n", input_df)
    prediction = model.predict(input_df)
    print(f"📈 Predicted Temp: {prediction[0]:.2f}°C")
    return prediction[0]