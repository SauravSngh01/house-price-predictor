<<<<<<< HEAD
house_price_prediction/
│
├── data/                    # Raw and processed datasets
│   ├── housing_data.csv     # Complete dataset with Indian cities
│   └── cleaned_data.csv     # Cleaned version if applicable
│
├── model/                   # Machine learning training & utilities
│   ├── train_model.py       # Script to train and save the model
│   ├── house_price_model.pkl# Trained model file
│   └── utils.py             # Helper functions (e.g., encoding)
│
├── streamlit_app/           # Streamlit app frontend
│   ├── app.py               # Main interface
│   ├── visuals.py           # Graph generation
│   └── inputs.py            # User input handling
│
├── assets/                  # Optional static assets (e.g., logo)
│   └── logo.png
│
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── .gitignore               # Exclude files like .pkl, __pycache__, etc.

🚀 How to Run
1. 🔧 Install Dependencies
     pip install -r requirements.txt
2. 🧠 Train the Model
    cd model
    python train_model.py
This will create a file: house_price_model.pkl

3. 🖥️ Run the Streamlit Web App
    cd ../streamlit_app
    streamlit run app.py
Open your browser and visit: http://localhost:8501

📊 Features
Predict house prices based on:

✅ Area (sq. ft)

✅ BHK (number of bedrooms)

✅ Location (across all Indian capital cities)

View interactive plots:

📈 Area vs Price

📊 BHK vs Price

Real-time ML model inference

Easily expandable with new data or models
