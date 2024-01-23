import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "localhost"
port = 1883
topic = "example/topic"

# Callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}", flush=True)

# Create MQTT client
client = mqtt.Client()

# Set the callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port=port)

# Subscribe to the topic
client.subscribe(topic)

# Loop to listen for messages
client.loop_forever()
