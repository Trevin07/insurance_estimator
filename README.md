# 🩺 Insurance Estimator Web App

A Flask-based machine learning web application that predicts  health insurance charges based on user inputs like age, sex, BMI, number of children, and smoking status.

![Screenshot 1](screenshot1.png)  


---

## 🚀 Features

- Clean and responsive UI built with HTML, CSS, and Bootstrap Icons  
- Backend logic powered by Flask  
- Predicts medical insurance costs using machine learning  
- Uses trained models with **XGBoost** and **Scikit-learn**

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

