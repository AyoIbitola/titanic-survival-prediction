from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load Model and Scaler
MODEL_PATH = os.path.join('model', 'titanic_survival_model.pkl')
SCALER_PATH = os.path.join('model', 'scaler.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and Scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model/scaler: {e}")
    model = None
    scaler = None

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ""
    result_class = ""
    
    if request.method == 'POST':
        if not model or not scaler:
            return render_template('index.html', prediction_text="Error: Model not loaded.", result_class="error")
        
        try:
            # Get values 
            # Features: pclass, sex, age, sibsp, fare
            pclass = float(request.form['pclass'])
            sex = float(request.form['sex']) # 0=Male, 1=Female
            age = float(request.form['age'])
            sibsp = float(request.form['sibsp'])
            fare = float(request.form['fare'])
            
            features = [pclass, sex, age, sibsp, fare]
            
            # Preprocess
            features_array = np.array([features])
            features_scaled = scaler.transform(features_array)
            
            # Predict
            prediction = model.predict(features_scaled)[0]
            
            if prediction == 1:
                prediction_text = "Prediction: Survived"
                result_class = "survived"
            else:
                prediction_text = "Prediction: Did Not Survive"
                result_class = "died"
            
        except ValueError:
            prediction_text = "Error: Please check your inputs."
            result_class = "error"
        except Exception as e:
            prediction_text = f"Error: {str(e)}"
            result_class = "error"

    return render_template('index.html', prediction_text=prediction_text, result_class=result_class)

if __name__ == '__main__':
    app.run(debug=True)
