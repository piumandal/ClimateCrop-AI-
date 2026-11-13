# 🌱 ClimateCrop AI
### AI-Powered Crop Recommendation & Weather Intelligence System

**Smart Agriculture. Intelligent Decisions. Sustainable Growth.**

ClimateCrop AI is a machine learning-powered agricultural decision-support application designed to help farmers make smarter crop selection and irrigation decisions using soil parameters, environmental conditions, and live weather information.

The platform combines Machine Learning and real-time weather data to provide useful agricultural insights through an interactive web interface built with Streamlit.

---

## 🚀 Key Features

### 1. 🌾 AI-Based Crop Recommendation
- Recommends suitable crops based on agricultural input parameters.
- Uses a trained Random Forest Machine Learning model.
- Analyzes seven important parameters:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - Soil pH
  - Rainfall

### 2. 🌦️ Live Weather Intelligence
- Fetches current weather information using the Open-Meteo API.
- Provides weather forecasts for the upcoming seven days.
- Displays important weather parameters to support farming decisions.

### 3. 💧 Smart Irrigation Advisory
- Uses forecast rainfall information to provide basic irrigation guidance.
- Helps users understand upcoming rainfall conditions.
- Supports more informed water-management decisions.

### 4. 📊 Interactive Dashboard
- User-friendly Streamlit interface.
- Organized sections for crop recommendations and weather information.
- Visual presentation of weather and agricultural insights.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data processing |
| Scikit-learn | Machine Learning model |
| Random Forest | Crop prediction algorithm |
| Joblib | Model serialization and loading |
| Requests | API communication |
| Open-Meteo API | Live weather and forecast data |

---

## 🧠 Machine Learning Model

ClimateCrop AI uses a trained Random Forest Classifier for crop recommendation.

**Input Features:**
1. Nitrogen
2. Phosphorus
3. Potassium
4. Temperature
5. Humidity
6. pH
7. Rainfall

**Output:** Predicted suitable crop based on the provided input parameters.

The trained model and label encoder are stored as `.pkl` files and loaded by the application.

---

## 📂 Project Structure

```text
ClimateCropAI/
│
├── app.py
├── train_model.py
├── Crop_recommendation.csv
│
├── crop_model.pkl
├── label_encoder.pkl
├── feature_names.pkl
│
├── weather_test.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── venv/
```

*Note: The virtual environment (`venv/`) should not be uploaded to GitHub.*

---

## ⚙️ Installation & Setup

Follow these steps to run ClimateCrop AI locally.

### Step 1: Clone the repository

```bash
git clone https://github.com/piumandal/ClimateCrop-AI-.git
```

### Step 2: Navigate to the project folder

```bash
cd ClimateCrop-AI-
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

---

## 🌍 Weather Data Source

ClimateCrop AI uses the **Open-Meteo API** to retrieve weather information and forecasts.

Website: https://open-meteo.com/

---

## 🎯 Project Objective

The primary objective of ClimateCrop AI is to combine machine learning and live weather information to support smarter agricultural decisions.

By making crop recommendations and weather insights accessible through a simple interface, the project aims to contribute to technology-driven and sustainable agriculture.

---

## 🔮 Future Enhancements

- Soil health analysis and monitoring.
- More advanced irrigation recommendations.
- Crop disease detection using image processing.
- Fertilizer recommendation system.
- Multilingual support for farmers.
- Mobile-friendly agricultural assistance.

---

## 👨‍💻 Developer

**Piu Mandal**

GitHub: https://github.com/piumandal

---

### 🌱 ClimateCrop AI
**Smart Agriculture. Intelligent Decisions. Sustainable Growth.**
