# 🩺 Insurance Estimator Web App
<p>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python" width="120"/>
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-2.0%2B-grey?style=flat-square&logo=flask" alt="Flask" width="120"/>
  </a>
  <a href="https://scikit-learn.org/">
    <img src="https://img.shields.io/badge/scikit--learn-1.6.1-green?style=flat-square&logo=scikit-learn" alt="scikit-learn" width="120"/>
  </a>
  <br>
  <a href="https://xgboost.ai/">
    <img src="https://img.shields.io/badge/XGBoost-2.0%2B-red?style=flat-square&logo=xgboost" alt="XGBoost" width="120"/>
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/pandas-1.5.3-blue?style=flat-square&logo=pandas" alt="pandas" width="120"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5">
    <img src="https://img.shields.io/badge/HTML5-E34F26-orange?style=flat-square&logo=html5" alt="HTML5" width="120"/>
  </a>
  <br>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://img.shields.io/badge/CSS3-1572B6-blue?style=flat-square&logo=css3" alt="CSS3" width="120"/>
  </a>
  <a href="https://fontawesome.com/">
    <img src="https://img.shields.io/badge/Font_Awesome-6.5.0-purple?style=flat-square&logo=fontawesome" alt="Font Awesome" width="120"/>
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License" width="120"/>
  </a>
</p>


A Flask-based machine learning web application that predicts  health insurance charges based on user inputs like age, sex, BMI, number of children, and smoking status.

![Screenshot 1](screenshot1.png)  


---

## 🚀 Features

- Clean and responsive UI built with HTML, CSS, and Bootstrap Icons  
- Backend logic powered by Flask  
- Predicts medical insurance costs using machine learning  
- Uses trained models with **XGBoost** and **Scikit-learn** with an accuracy of 86%

---

## 🧠 Models and Tools Used

### 🔸 XGBoost
- A high-performance gradient boosting algorithm  
- Handles both categorical and continuous features well  
- Robust to overfitting with built-in regularization

### 🔸 Scikit-learn
- Used for data preprocessing, evaluation, and model comparison  
- Includes tools like `train_test_split`, `StandardScaler`, and various metrics

### 🔸 Pandas & NumPy
- For data manipulation and numerical operations

### 🔸 Flask
- Lightweight Python framework for web apps  
- Handles form inputs, routing, and template rendering

---

## 🛠 How It Works

1. User fills out a form with age, sex, BMI, children, and smoking status  
2. The form is submitted to the Flask server via POST  
3. The backend processes the data and passes it to a trained ML model  
4. The model returns an insurance cost prediction  
5. The result is displayed back to the user

---

## 🎯 Impact and Importance

This project shows how machine learning can be integrated into a real-world application with an interactive front end. It’s designed to educate users about the factors that influence insurance pricing and the power of predictive analytics.

### Why it matters:
- Increases awareness of how personal factors affect insurance costs  
- Can be used as an educational tool for data science deployment  
- Demonstrates end-to-end ML integration from model to user interface

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/insurance_estimator.git
cd insurance_estimator
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Then open your browser and go to:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and share it with attribution.

---

## 📌 Generate `requirements.txt`

If you're setting this project up on your own machine and want to export the required dependencies, run:
```bash
pip freeze > requirements.txt
```

---

