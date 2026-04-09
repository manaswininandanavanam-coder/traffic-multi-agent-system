import random

class TrafficAgent:

    def __init__(self, intersection):
        self.intersection = intersection
        self.vehicle_count = 0
        self.signal = "RED"

    def sense_traffic(self):
        self.vehicle_count = random.randint(0, 60)

    def decide_signal(self):

        if self.vehicle_count > 40:
            self.signal = "GREEN"

        elif self.vehicle_count > 20:
            self.signal = "YELLOW"

        else:
            self.signal = "RED"

        return self.signal
