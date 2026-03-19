# 🏃 Speed vs. Pace Dashboard
An interactive dashboard that converts Speed (km/h or mph) into Pace (min/km or min/mile).

### 🔗 Live Demo
**Check out the app here:** [https://speed-pace-kozehfhn2ygguw7ay5fjpr.streamlit.app](https://speed-pace-kozehfhn2ygguw7ay5fjpr.streamlit.app)

### 🔍 Why this exists?
When driving, it is easy to push on the accelator thinking that adding 5 units of speed will help us save plenty of time, this isin fact, wrong. This tool visualizes the inverse relationship giving prominence to time rather then speed, helping users understand how changes in speed do not significantly mpact their per-unit time.

### 🛠️ Key Features
- **Dual Unit Support:** Seamlessly switch between Metric (km/h) and Imperial (mph).
- **Reference Table:** View a sidebar of paces for common speed increments.
- **Real-time Conversion:** Use the interactive slider to see instant pace results in `MM:SS` format.

### 🧮 The Logic
The app uses the reciprocal relationship between speed ($v$) and pace ($P$):
$$P = \frac{60}{v}$$
This highlights how small increases in speed at lower velocities result in much larger time savings compared to higher velocities.

### 🚀 How to run locally
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python -m streamlit run app.py`
