import random

def generate_traffic():

    traffic_data = {
        "A": random.randint(0,60),
        "B": random.randint(0,60),
        "C": random.randint(0,60),
        "D": random.randint(0,60)
    }

    return traffic_data
