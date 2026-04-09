import time

class SignalController:

    def __init__(self):
        self.signals = {}

    # initialize signals for intersections
    def initialize_signals(self, intersections):

        for i in intersections:
            self.signals[i] = {
                "state": "RED",
                "duration": 10
            }

    # update signal based on traffic density
    def update_signal(self, intersection, vehicle_count):

        if vehicle_count > 40:
            state = "GREEN"
            duration = 30

        elif vehicle_count > 20:
            state = "YELLOW"
            duration = 15

        else:
            state = "RED"
            duration = 10

        self.signals[intersection]["state"] = state
        self.signals[intersection]["duration"] = duration

    # display signals
    def display_signals(self):

        for inter, signal in self.signals.items():

            print("Intersection:", inter)
            print("Signal:", signal["state"])
            print("Duration:", signal["duration"], "seconds")
            print("------------------------")

    # run signal cycle
    def run_cycle(self):

        for inter, signal in self.signals.items():

            print(f"{inter} signal {signal['state']} for {signal['duration']} seconds")

            time.sleep(1)
