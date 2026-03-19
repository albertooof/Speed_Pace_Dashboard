import streamlit as st
import pandas as pd

# --- 1. SET UP CACHED FUNCTIONS ---
@st.cache_data
def get_reference_table(speed_label, pace_label):
    speeds = list(range(0, 210, 10))
    paces = []
    for s in speeds:
        if s == 0:
            paces.append("∞")
        else:
            p_dec = 60 / s
            m = int(p_dec)
            s_rem = int((p_dec - m) * 60)
            paces.append(f"{m}:{s_rem:02d}")
    
    return pd.DataFrame({
        f"Speed ({speed_label})": speeds,
        f"Pace ({pace_label})": paces
    })

# --- 2. APP CONFIG & UI ---
st.set_page_config(layout="wide") # Spread out the dashboard
st.title("🏃 Speed vs. Pace Converter")

# --- Layout: Main Area (Left) and Table Area (Right) ---
main_col, table_col = st.columns([2, 1])

with main_col:
    st.subheader("Interactive Tool")
    
    # 1. Unit Selection
    unit_system = st.radio("Select Units:", ["Metric (km)", "Imperial (miles)"], horizontal=True)
    
    if unit_system == "Metric (km)":
        dist_label, speed_label, pace_label = "km", "km/h", "min/km"
    else:
        dist_label, speed_label, pace_label = "miles", "mph", "min/mile"

    # 2. The Slider (Start at 0.5 to avoid error)
    speed = st.slider(f"Select Speed ({speed_label}):", min_value=0.0, max_value=200.0, value=50.0, step=2.0)

    # 3. Calculations
    pace_decimal = 60 / speed
    minutes = int(pace_decimal)
    seconds = int((pace_decimal - minutes) * 60)

    # 4. Display Results
    c1, c2 = st.columns(2)
    c1.metric(label=f"Speed ({speed_label})", value=f"{speed:.1f}")
    c2.metric(label=f"Pace ({pace_label})", value=f"{minutes}:{seconds:02d}")

    st.info(f"At {speed:.1f} {speed_label}, it takes you {minutes}:{seconds:02d} to cover 1 {dist_label}.")

with table_col:
    st.subheader("Reference Table")
    # --- 3. CALL THE CACHED FUNCTION ---
    df = get_reference_table(speed_label, pace_label)
    st.dataframe(df, height=600, use_container_width=True)