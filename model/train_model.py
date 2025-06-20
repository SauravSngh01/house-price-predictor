# model/train_model.py
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from utils import preprocess_data

# Load dataset
df = pd.read_csv("../data/housing_data.csv")

# Preprocess data
X, y = preprocess_data(df)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as house_price_model.pkl")
