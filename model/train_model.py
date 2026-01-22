import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train():
    print("Loading Titanic dataset...")
    # Fetch Titanic dataset (ID 40945 or name='titanic', val 1)
    try:
        titanic = fetch_openml('titanic', version=1, as_frame=True)
        df = titanic.frame
    except Exception as e:
        print(f"Error fetching dataset: {e}")
        return

    # Feature Selection
    features = ['pclass', 'sex', 'age', 'sibsp', 'fare']
    target = 'survived'
    
    print(f"Selected features: {features}")
    
    X = df[features].copy()
    y = df[target]
    
    print("Handling missing values & encoding...")
    # Impute Age and Fare
    X['age'] = X['age'].fillna(X['age'].median())
    X['fare'] = X['fare'].fillna(X['fare'].median())
    
    # Encode Sex (male=0, female=1 to match potential UI inputs)
    # Note: openml titanic often returns 'female', 'male' strings
    X['sex'] = X['sex'].map({'male': 0, 'female': 1})
    
    # Scaling
    print("Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Train
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save
    print("Saving model and scaler...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'titanic_survival_model.pkl')
    scaler_path = os.path.join(script_dir, 'scaler.pkl')
    
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Saved model to {model_path}")
    print(f"Saved scaler to {scaler_path}")
    
    # Verify
    print("Verifying reload...")
    loaded_model = joblib.load(model_path)
    if loaded_model:
        print("Model reload successful.")

if __name__ == "__main__":
    train()
