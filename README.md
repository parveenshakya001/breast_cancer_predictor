# 🌾 AgriSense — Agricultural Market Price Predictor

> A machine-learning-powered web application for predicting the **modal price of agricultural commodities** using market, commodity, variety, grade, and historical price information.

### 🚀 Live Application

**[Launch AgriSense](https://agriculture-price-predictor.onrender.com)**

---

## 📌 About the Project

Agricultural commodity prices vary significantly across different states, districts, markets, varieties, and grades.

**AgriSense** is designed to simplify agricultural market price estimation by using a trained **XGBoost Regression model** to predict the expected **modal price** of a commodity.

Instead of requiring users to manually navigate through unrelated market options, the application provides a fully dependent selection flow:

**State → District → Market → Commodity → Variety → Grade**

The application also displays **historical minimum and maximum price guidance** for the selected combination before generating the final prediction.

---

## ✨ Key Features

- 🤖 **ML-Based Price Prediction**  
  Predicts the modal price using a trained XGBoost regression model.

- 📍 **Location-Aware Selection**  
  Districts are filtered according to the selected state, and markets according to the selected district.

- 🌾 **Market-Specific Commodity Selection**  
  Commodities, varieties, and grades are dynamically filtered based on the selected market.

- 🔍 **Searchable Dropdowns**  
  Large lists can be searched instead of manually scrolling through options.

- 🔤 **Alphabetically Sorted Options**  
  Dropdown values are displayed alphabetically for faster navigation.

- 📊 **Historical Price Guidance**  
  Displays historical minimum and maximum price ranges for the selected market combination.

- ♻️ **Form State Preservation**  
  User selections remain available after prediction instead of resetting the form.

- 💻 **Responsive User Interface**  
  Agriculture-inspired interface designed using HTML, CSS, and JavaScript.

- ☁️ **Cloud Deployment**  
  The complete Flask application is deployed on Render and accessible online.

---

## 🧠 Machine Learning Approach

The prediction system is built using:

### XGBoost Regressor

The model learns relationships between agricultural market characteristics and historical commodity prices to estimate the **Modal Price**.

### Input Features

| Feature | Description |
|---|---|
| State | State where the market is located |
| District | District within the selected state |
| Market | Agricultural market/APMC |
| Commodity | Agricultural commodity |
| Variety | Variety of the selected commodity |
| Grade | Commodity quality grade |
| Minimum Price | Minimum market price |
| Maximum Price | Maximum market price |

### Target Variable

**Modal Price** — the predicted representative market price of the selected commodity.

---

## 📈 Model Performance

The trained XGBoost regression model achieved an:

### **R² Score ≈ 0.998**

on the evaluated test dataset.

An R² value close to `1.0` indicates that the model explains a very high proportion of the variation in the target variable within the evaluated dataset.

> **Note:** An R² score of 0.998 should not be interpreted as “99.8% prediction accuracy” or as a guarantee of equivalent performance on future unseen market conditions.

---

## ⚙️ How AgriSense Works

```text
                 Agriculture Dataset
                         │
                         ▼
                  Data Preprocessing
                         │
                         ▼
              Categorical Encoding
                         │
                         ▼
                  Train / Test Split
                         │
                         ▼
                 XGBRegressor
                         │
                         ▼
                  Model Evaluation
                         │
                         ▼
              Saved XGBoost Model
                         │
                         ▼
                   Flask Backend
                         │
                         ▼
              AgriSense Web Interface
                         │
                         ▼
 State → District → Market → Commodity → Variety → Grade
                         │
                         ▼
          Minimum Price + Maximum Price
                         │
                         ▼
               XGBoost Prediction
                         │
                         ▼
              Predicted Modal Price
```

---

## 🔄 Application Workflow

1. Select the **State**
2. Select a valid **District**
3. Select a **Market** available in that district
4. Select a **Commodity** available in that market
5. Select the corresponding **Variety**
6. Select the available **Grade**
7. Review historical price guidance
8. Enter the **Minimum Price**
9. Enter the **Maximum Price**
10. Click **Predict Modal Price**
11. The trained XGBoost model generates the predicted modal price

---

## 🛠️ Technology Stack

### Machine Learning & Data Processing

- Python
- Pandas
- XGBoost
- Scikit-learn

### Backend

- Flask
- Gunicorn

### Frontend

- HTML5
- CSS3
- JavaScript
- Tom Select

### Development & Deployment

- Git
- GitHub
- Render

---

## 📂 Project Structure

```text
agriculture-price-predictor/
│
├── app.py
│
├── Agriculture.csv
│
├── agriculture_model.json
│
├── requirements.txt
│
├── .python-version
│
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 💻 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/SnehaVerma16/agriculture-price-predictor.git
```

### 2. Navigate to the Project

```bash
cd agriculture-price-predictor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🌐 Deployment

AgriSense is deployed on **Render** using a production Gunicorn server.

Production start command:

```bash
gunicorn app:app
```

### Live Demo

👉 **[https://agriculture-price-predictor.onrender.com](https://agriculture-price-predictor.onrender.com)**

---

## 🔮 Future Improvements

The current system can be extended with:

- Real-time agricultural market data integration
- Historical price trend graphs
- Time-series forecasting
- Weather and seasonal features
- Market-to-market commodity price comparison
- Commodity price history dashboard
- REST API for external applications
- Automated model retraining
- Model monitoring and drift detection
- Improved prediction explainability

---

## ⚠️ Disclaimer

AgriSense generates machine-learning-based estimates using historical agricultural market data.

Predictions should be treated as **analytical estimates rather than guaranteed future market prices**. Actual agricultural prices can be affected by weather, supply and demand, seasonality, transportation, government policies, and other market conditions.

---

## 👩‍💻 Developers

### Sneha Verma

**Roll Number:** 28240091  
**Branch:** B.Tech CSE (Core)

- LinkedIn: [Sneha Verma](https://www.linkedin.com/in/sneha-verma-071b04322)
- GitHub: [SnehaVerma16](https://github.com/SnehaVerma16)

---

## ⭐ Project Links

**Live Application:**  
https://agriculture-price-predictor.onrender.com

**GitHub Repository:**  
https://github.com/SnehaVerma16/agriculture-price-predictor
