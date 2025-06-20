# model/utils.py
import pandas as pd

def preprocess_data(df):
    # Basic cleanup (optional)
    df = df.dropna()

    # One-hot encode location
    location_dummies = pd.get_dummies(df["location"], prefix="location")
    df_encoded = pd.concat([df[["area", "bhk"]], location_dummies], axis=1)

    # Features and target
    X = df_encoded
    y = df["price"]

    return X, y
