import streamlit as st
import pandas as pd
import base64
from agents.traffic_agent import TrafficAgent
from simulation.traffic_generator import generate_traffic
from visualization.map_view import create_map
from streamlit_folium import folium_static


# ---------- BACKGROUND FUNCTION ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Headings black color */
    h1, h2, h3, h4, h5, h6 {{
        color: black !important;
    }}

    /* Text black color */
    p, div {{
        color: black !important;
    }}

    /* Optional: white box behind content for clarity */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)


# ---------- CALL BACKGROUND ----------
set_bg("background.jpg")


# ---------- YOUR ORIGINAL CODE ----------
st.title("Multi-Agent Traffic Management System")

st.write("AI based Smart Traffic Control Simulation")

traffic_data = generate_traffic()

agents = {}

df = pd.read_csv("data/traffic_data.csv")

print(df)

for key in traffic_data:
    agent = TrafficAgent(key)
    agent.vehicle_count = traffic_data[key]
    agent.decide_signal()
    agents[key] = agent

data = []

for key, agent in agents.items():
    data.append({
        "Intersection": key,
        "Vehicles": agent.vehicle_count,
        "Signal": agent.signal
    })

df = pd.DataFrame(data)

st.subheader("Traffic Status")

st.dataframe(df)

st.subheader("Traffic Map")

map = create_map(traffic_data)

folium_static(map)
