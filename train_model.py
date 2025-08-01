from sklearn.linear_model import LinearRegression
import joblib

def train_and_save_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'weather_model.pkl')
    print("Training features:\n", X.head())

