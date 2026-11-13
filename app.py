

import streamlit as st
import pandas as pd
import joblib
import requests

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ClimateCrop AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. PREMIUM UI DESIGN
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

:root {
    --green: #1c7548;
    --dark: #102d22;
    --lime: #b7ef65;
    --bg: #f5f8f3;
    --text: #17251b;
    --muted: #526458;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

/* MAIN HEADINGS */

h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    color: #142b1d !important;
    font-weight: 800 !important;
}

/* GENERAL TEXT */

.stMarkdown p,
.stMarkdown li {
    color: #26382c;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #e6f0e5;
}

[data-testid="stSidebar"] * {
    color: #142b1d !important;
}

[data-testid="stSidebar"] hr {
    border-color: #c6d9c5;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #102d22 !important;
}

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #405b47 !important;
}

/* HERO SECTION */

.hero {
    background:
        radial-gradient(circle at 85% 15%, rgba(183,239,101,0.18), transparent 30%),
        linear-gradient(115deg, #102d22, #174b32 65%, #246c43);
    border-radius: 24px;
    padding: 38px;
    margin-bottom: 28px;
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 15px 40px rgba(16,45,34,0.14);
}

.hero-tag {
    display: inline-block;
    background: rgba(183,239,101,0.15);
    color: #c9f58e !important;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 43px !important;
    font-weight: 800 !important;
    margin: 17px 0 8px 0;
}

.hero p {
    color: #e4eee6 !important;
    font-size: 15px;
    max-width: 620px;
    line-height: 1.8;
}

.hero-highlight {
    color: #c6f58b !important;
}

/* SECTION HEADINGS */

.section-label {
    color: #1c7548 !important;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.section-title {
    font-family: 'Outfit', sans-serif;
    color: #142b1d !important;
    font-size: 27px;
    font-weight: 800;
    margin-bottom: 4px;
}

.section-desc {
    color: #526458 !important;
    font-size: 14px;
    margin-bottom: 20px;
}

/* FEATURE CARDS */

.feature-card {
    background: #ffffff;
    border: 1px solid #e3ebe1;
    border-radius: 19px;
    padding: 23px;
    min-height: 155px;
    box-shadow: 0 6px 20px rgba(24,65,40,0.035);
}

.feature-icon {
    background: #eaf6e8;
    display: inline-flex;
    width: 43px;
    height: 43px;
    border-radius: 13px;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    margin-bottom: 13px;
}

.feature-card h3 {
    color: #142b1d !important;
    font-size: 17px;
    margin: 0 0 7px 0;
}

.feature-card p {
    color: #526458 !important;
    font-size: 13px;
    line-height: 1.6;
    margin: 0;
}

/* METRIC CARDS */

div[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e3ebe1;
    border-radius: 17px;
    padding: 19px 20px;
    box-shadow: 0 5px 18px rgba(24,65,40,0.04);
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: #26382c !important;
    font-size: 13px;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    color: #1c7548 !important;
    font-family: 'Outfit', sans-serif;
    font-weight: 800 !important;
}

/* BUTTONS */

.stButton > button {
    background: #1c7548 !important;
    color: #ffffff !important;
    border: 1px solid #1c7548 !important;
    border-radius: 12px;
    min-height: 45px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button p,
.stButton > button span {
    color: #ffffff !important;
}

.stButton > button:hover {
    background: #145b36 !important;
    color: #ffffff !important;
    border-color: #145b36 !important;
    transform: translateY(-2px);
}

/* INPUT FIELDS */

.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stSlider label,
.stDateInput label {
    color: #142b1d !important;
    font-weight: 700 !important;
}

.stTextInput input,
.stNumberInput input,
.stDateInput input {
    background: #ffffff !important;
    color: #142b1d !important;
    border: 1px solid #cbdacb !important;
    border-radius: 11px;
}

.stTextInput input::placeholder {
    color: #68796c !important;
    opacity: 1;
}

/* DROPDOWNS */

[data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #142b1d !important;
    border-color: #cbdacb !important;
}

[data-baseweb="select"] span {
    color: #142b1d !important;
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #e4eee2;
    padding: 7px;
    border-radius: 14px;
}

.stTabs [data-baseweb="tab"],
.stTabs button[role="tab"] {
    background: transparent !important;
    border-radius: 10px;
    color: #000000 !important;
    font-weight: 800 !important;
    font-size: 15px !important;
    padding: 11px 18px;
}

.stTabs [data-baseweb="tab"] *,
.stTabs button[role="tab"] * {
    color: #000000 !important;
    fill: #000000 !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"],
.stTabs button[role="tab"][aria-selected="true"] {
    background: #ffffff !important;
    color: #000000 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-bottom: 3px solid #1c7548 !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] *,
.stTabs button[role="tab"][aria-selected="true"] * {
    color: #000000 !important;
}

/* RESULT PANEL */

.result-panel {
    background: linear-gradient(120deg, #123c2b, #1c7548);
    border-radius: 22px;
    padding: 30px;
    text-align: center;
    color: #ffffff !important;
    margin: 15px 0;
}

.result-panel .small {
    color: #e1f2e4 !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.result-panel h2 {
    color: #c7f58c !important;
    font-size: 37px;
    margin: 12px 0;
}

.result-panel p {
    color: #ffffff !important;
    font-size: 14px;
}

/* IRRIGATION ADVISORY */

.advisory {
    background: #ffffff;
    border: 1px solid #e2ebe1;
    border-left: 5px solid #86bd50;
    border-radius: 14px;
    padding: 19px;
    margin: 12px 0;
    color: #26382c !important;
    line-height: 1.7;
}

/* ALERTS */

[data-testid="stAlert"] p,
[data-testid="stAlert"] span {
    font-weight: 500;
}

/* DATA TABLE */

[data-testid="stDataFrame"] {
    color: #142b1d !important;
}

[data-testid="stDataFrame"] * {
    color: #142b1d !important;
}

/* FOOTER */

.footer {
    background: #102d22;
    border-radius: 17px;
    padding: 25px;
    text-align: center;
    color: #e2eee4 !important;
    font-size: 13px;
    line-height: 1.8;
    margin-top: 30px;
}

.footer h3 {
    color: #FFD700 !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 28px !important;
    font-weight: 800 !important;
    margin-bottom: 10px;
}

.footer-tagline {
    color: #e2eee4 !important;
    font-size: 14px;
    font-weight: 600;
    margin: 8px 0;
}

.footer-credit {
    color: #b7cbbb !important;
    font-size: 12px;
}

/* DIVIDERS */

hr {
    border-color: #dce8da !important;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. LOAD ML MODEL
# ==========================================

try:
    model = joblib.load("crop_model.pkl")
    encoder = joblib.load("label_encoder.pkl")
    feature_names = joblib.load("feature_names.pkl")
except FileNotFoundError as error:
    st.error(
        f"Required ML file not found: {error}. "
        "Keep all three pickle files in the same folder as app.py."
    )
    st.stop()


# ==========================================
# 4. SESSION STATE
# ==========================================

if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

if "weather_location" not in st.session_state:
    st.session_state.weather_location = None

if "crop_result" not in st.session_state:
    st.session_state.crop_result = None


# ==========================================
# 5. WEATHER FUNCTIONS
# ==========================================

@st.cache_data(ttl=3600)
def get_city_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 5,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    results = response.json().get("results", [])

    if not results:
        return None

    return results[0]


@st.cache_data(ttl=900)
def get_live_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "precipitation_probability_max",
            "weather_code"
        ],
        "forecast_days": 7,
        "timezone": "auto"
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    return response.json()


def weather_description(code):

    descriptions = {
        0: "Clear Sky ☀️",
        1: "Mainly Clear 🌤️",
        2: "Partly Cloudy ⛅",
        3: "Overcast ☁️",
        45: "Foggy 🌫️",
        48: "Depositing Rime Fog 🌫️",
        51: "Light Drizzle 🌦️",
        53: "Moderate Drizzle 🌦️",
        55: "Dense Drizzle 🌧️",
        61: "Slight Rain 🌧️",
        63: "Moderate Rain 🌧️",
        65: "Heavy Rain 🌧️",
        71: "Slight Snow ❄️",
        73: "Moderate Snow ❄️",
        75: "Heavy Snow ❄️",
        80: "Rain Showers 🌦️",
        81: "Moderate Rain Showers 🌧️",
        82: "Heavy Rain Showers 🌧️",
        95: "Thunderstorm ⛈️",
        96: "Thunderstorm with Hail ⛈️",
        99: "Heavy Thunderstorm ⛈️"
    }

    return descriptions.get(code, "Weather unavailable")


# ==========================================
# 6. SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🌿 ClimateCrop")

    st.caption("INTELLIGENT AGRICULTURE")

    st.divider()

    st.markdown("### YOUR PLATFORM")

    st.markdown("""
    **🌍 Climate Intelligence**

    Live weather and forecast analysis.

    **💧 Water Management**

    Weather-based irrigation guidance.

    **🌾 Crop Intelligence**

    Machine learning crop recommendations.
    """)

    st.divider()

    st.markdown("### TECHNOLOGY")

    st.caption("Python • Streamlit • Random Forest")
    st.caption("Open-Meteo API")

    st.divider()

    st.caption("Growing smarter, together. 🌱")


# ==========================================
# 7. HERO SECTION
# ==========================================

st.markdown(
    """
<div class="hero">
    <span class="hero-tag">✦ AI-POWERED AGRICULTURE</span>
    <h1>
        Grow Smarter.<br>
        <span class="hero-highlight">Farm Better.</span>
    </h1>
    <p>Welcome to ClimateCrop AI – your intelligent farming companion. Discover suitable crops, understand changing weather and make smarter irrigation decisions.</p>
</div>
""",
    unsafe_allow_html=True,
)


# ==========================================
# 8. MAIN TABS
# ==========================================

dashboard, weather_tab, crop_tab = st.tabs([
    "✦ Overview",
    "☀ Weather Intelligence",
    "🌱 Crop Advisor"
])


# ==========================================
# TAB 1 - OVERVIEW
# ==========================================

with dashboard:

    st.markdown(
        '<div class="section-label">YOUR CONTROL CENTER</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Agriculture Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-desc">Everything you need for smarter farming, in one place.</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌦️</div>
            <h3>Climate Intelligence</h3>
            <p>Monitor live temperature, humidity, rainfall
            and upcoming weather conditions.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💧</div>
            <h3>Smart Irrigation</h3>
            <p>Understand rainfall forecasts and make
            informed water-management decisions.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌾</div>
            <h3>AI Crop Advisor</h3>
            <p>Find suitable crops using soil nutrients
            and climate parameters.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🌍 Weather at a Glance")

    if st.session_state.weather_data is not None:

        current = st.session_state.weather_data["current"]
        location = st.session_state.weather_location

        st.success(f"Weather location: {location['name']}")

        x1, x2, x3, x4 = st.columns(4)

        x1.metric(
            "🌡️ Temperature",
            f"{current['temperature_2m']} °C"
        )

        x2.metric(
            "💧 Humidity",
            f"{current['relative_humidity_2m']}%"
        )

        x3.metric(
            "🌧️ Rainfall",
            f"{current['precipitation']} mm"
        )

        x4.metric(
            "💨 Wind Speed",
            f"{current['wind_speed_10m']} km/h"
        )

    else:

        st.info(
            "No weather data loaded yet. Visit Weather Intelligence "
            "to enter a city and fetch live conditions."
        )

    st.divider()

    st.markdown("### 🌱 Your Crop Recommendation")

    if st.session_state.crop_result:

        st.markdown(
            f"""
            <div class="result-panel">
                <div class="small">LATEST AI RECOMMENDATION</div>
                <h2>🌾 {st.session_state.crop_result.capitalize()}</h2>
                <p>Your crop recommendation is ready.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Your recommended crop will appear here after "
            "you use the Crop Advisor."
        )


# ==========================================
# TAB 2 - WEATHER INTELLIGENCE
# ==========================================

with weather_tab:

    st.markdown(
        '<div class="section-label">CLIMATE MONITORING</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Weather Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-desc">Real-time weather conditions and seven-day climate outlook.</div>',
        unsafe_allow_html=True
    )

    city = st.text_input(
        "📍 Enter your city",
        placeholder="Example: Ranchi",
        key="city_input"
    )

    if st.button("↗ Fetch Live Weather", use_container_width=True):

        if not city.strip():

            st.warning("Please enter your city name.")

        else:

            try:

                with st.spinner("Connecting to weather intelligence..."):

                    location = get_city_coordinates(city.strip())

                    if location is None:

                        st.error("City not found. Check the spelling.")

                    else:

                        data = get_live_weather(
                            location["latitude"],
                            location["longitude"]
                        )

                        st.session_state.weather_data = data
                        st.session_state.weather_location = location

                        st.success(
                            f"Weather successfully loaded for {location['name']}!"
                        )

            except requests.RequestException as error:

                st.error(f"Weather API error: {error}")

    if st.session_state.weather_data is not None:

        data = st.session_state.weather_data

        current = data["current"]
        daily = data["daily"]

        location = st.session_state.weather_location

        st.divider()

        st.markdown(
            f"### 📍 {location['name']}, {location.get('admin1', '')}"
        )

        st.info(weather_description(current["weather_code"]))

        x1, x2, x3, x4 = st.columns(4)

        x1.metric(
            "Temperature",
            f"{current['temperature_2m']} °C"
        )

        x2.metric(
            "Humidity",
            f"{current['relative_humidity_2m']}%"
        )

        x3.metric(
            "Precipitation",
            f"{current['precipitation']} mm"
        )

        x4.metric(
            "Wind Speed",
            f"{current['wind_speed_10m']} km/h"
        )

        st.caption(
            f"Observation time: {current.get('time', 'N/A')} | Open-Meteo"
        )

        # SEVEN-DAY FORECAST

        st.divider()

        st.markdown("### 📅 Seven-Day Forecast")

        forecast = pd.DataFrame({
            "Date": daily["time"],
            "Maximum Temperature": daily["temperature_2m_max"],
            "Minimum Temperature": daily["temperature_2m_min"],
            "Rainfall": daily["precipitation_sum"],
            "Rain Probability": daily["precipitation_probability_max"],
            "Weather": [
                weather_description(code)
                for code in daily["weather_code"]
            ]
        })

        st.markdown("#### 🌡️ Temperature Forecast")

        st.line_chart(
            forecast.set_index("Date")[
                ["Maximum Temperature", "Minimum Temperature"]
            ]
        )

        st.markdown("#### 🌧️ Rainfall Forecast")

        st.bar_chart(
            forecast.set_index("Date")[["Rainfall"]]
        )

        st.dataframe(
            forecast,
            use_container_width=True,
            hide_index=True
        )

        # SMART IRRIGATION

        st.divider()

        st.markdown("### 💧 Smart Irrigation Advisory")

        rain_2days = sum(daily["precipitation_sum"][:2])

        probability = max(
            daily["precipitation_probability_max"][:2]
        )

        rain_week = sum(daily["precipitation_sum"])

        x1, x2, x3 = st.columns(3)

        x1.metric("7-Day Rainfall", f"{rain_week:.1f} mm")
        x2.metric("Next 2 Days", f"{rain_2days:.1f} mm")
        x3.metric("Rain Probability", f"{probability}%")

        if rain_2days >= 5 or probability >= 60:

            st.warning(
                "🌧️ Rain is likely in the next two days. "
                "Consider postponing routine irrigation and "
                "check soil moisture before watering."
            )

        else:

            st.info(
                "☀️ No strong rainfall signal in the next two days. "
                "Check soil moisture before deciding to irrigate."
            )

        if rain_week >= 30:

            st.success(
                "Significant rainfall is forecast this week. "
                "Monitor drainage and avoid waterlogging."
            )

        else:

            st.info(
                "Weekly rainfall forecast is relatively low. "
                "Monitor soil moisture regularly."
            )

        st.caption(
            "This is a basic weather-based advisory. Actual irrigation "
            "needs depend on crop, soil moisture and growth stage."
        )

    else:

        st.info(
            "Enter your city above to unlock live weather, "
            "forecast charts and irrigation insights."
        )


# ==========================================
# TAB 3 - CROP ADVISOR
# ==========================================

with crop_tab:

    st.markdown(
        '<div class="section-label">MACHINE LEARNING ENGINE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Intelligent Crop Advisor</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-desc">Tell us about your soil and climate. Our trained ML model will suggest a suitable crop.</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🧪 Soil Nutrient Parameters")

    x1, x2, x3 = st.columns(3)

    with x1:

        nitrogen = st.number_input(
            "Nitrogen (N)",
            min_value=0.0,
            max_value=200.0,
            value=50.0
        )

    with x2:

        phosphorus = st.number_input(
            "Phosphorus (P)",
            min_value=0.0,
            max_value=200.0,
            value=50.0
        )

    with x3:

        potassium = st.number_input(
            "Potassium (K)",
            min_value=0.0,
            max_value=250.0,
            value=50.0
        )

    st.divider()

    st.markdown("### 🌤️ Climate Parameters")

    x1, x2 = st.columns(2)

    with x1:

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            max_value=60.0,
            value=25.0
        )

        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

    with x2:

        ph = st.number_input(
            "Soil pH",
            min_value=0.0,
            max_value=14.0,
            value=6.5
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=500.0,
            value=100.0
        )

    st.divider()

    if st.button(
        "✦ Generate AI Crop Recommendation",
        use_container_width=True
    ):

        try:

            input_data = pd.DataFrame(
                [[
                    nitrogen,
                    phosphorus,
                    potassium,
                    temperature,
                    humidity,
                    ph,
                    rainfall
                ]],
                columns=feature_names
            )

            prediction = model.predict(input_data)

            crop_name = encoder.inverse_transform(prediction)[0]

            st.session_state.crop_result = crop_name

            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="small">YOUR AI-POWERED CROP RESULT</div>
                    <h2>🌾 {crop_name.capitalize()}</h2>
                    <p>Recommended using your soil and climate parameters.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "Crop recommendation generated successfully!"
            )

            st.caption(
                "Powered by your trained Random Forest classifier. "
                "Validate results with local agricultural guidance."
            )

        except Exception as error:

            st.error(f"Prediction error: {error}")


# ==========================================
# 9. FOOTER
# ==========================================

# 9. FOOTER

st.markdown("---")

st.markdown(
    "<h1 style='text-align:center; color:#16A085;'>🌿 ClimateCrop AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Smart Agriculture. Intelligent Decisions. Sustainable Growth.</h4>",
    unsafe_allow_html=True
)

st.caption(
    "Built with Python • Machine Learning • Streamlit • Open-Meteo"
)

