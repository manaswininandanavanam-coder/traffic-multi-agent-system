import streamlit as st
import pandas as pd
from agents.traffic_agent import TrafficAgent
from simulation.traffic_generator import generate_traffic
from visualization.map_view import create_map
from streamlit_folium import folium_static

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

for key,agent in agents.items():
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
