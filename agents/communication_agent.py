class CommunicationAgent:

    def __init__(self):
        self.messages = []

    # send message to another agent
    def send_message(self, sender, receiver, data):

        message = {
            "from": sender,
            "to": receiver,
            "traffic_data": data
        }

        self.messages.append(message)

    # receive message
    def receive_messages(self, agent_name):

        received = []

        for msg in self.messages:
            if msg["to"] == agent_name:
                received.append(msg)

        return received

    # clear messages after reading
    def clear_messages(self):
        self.messages = []
