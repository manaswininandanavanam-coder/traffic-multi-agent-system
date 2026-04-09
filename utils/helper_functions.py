import pandas as pd


# Load traffic dataset
def load_traffic_data(file_path):

    df = pd.read_csv(file_path)
    return df


# Determine congestion level
def calculate_congestion(vehicle_count):

    if vehicle_count > 40:
        return "High"

    elif vehicle_count > 20:
        return "Medium"

    else:
        return "Low"


# Decide signal based on traffic
def decide_signal(vehicle_count):

    if vehicle_count > 40:
        return "GREEN"

    elif vehicle_count > 20:
        return "YELLOW"

    else:
        return "RED"


# Convert dataframe to dictionary
def dataframe_to_dict(df):

    traffic_dict = {}

    for index, row in df.iterrows():

        traffic_dict[row["Intersection"]] = row["Vehicles"]

    return traffic_dict
