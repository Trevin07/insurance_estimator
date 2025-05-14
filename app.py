from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')
features = joblib.load('model/features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        sex = 1 if request.form['sex'] == 'male' else 0
        smoker = 1 if request.form['smoker'] == 'yes' else 0

        data = [[age, bmi, children, sex, smoker]]
        full_data = np.zeros(len(features))
        for idx, feat in enumerate(features):
            if feat == 'age':
                full_data[idx] = age
            elif feat == 'bmi':
                full_data[idx] = bmi
            elif feat == 'children':
                full_data[idx] = children
            elif feat == 'sex_male':
                full_data[idx] = sex
            elif feat == 'smoker_yes':
                full_data[idx] = smoker

        scaled = scaler.transform([full_data])
        prediction = model.predict(scaled)[0]
        return render_template('index.html', prediction=f"${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
