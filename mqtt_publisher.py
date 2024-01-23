import paho.mqtt.publish as publish
import time

# MQTT broker details
broker_address = "localhost"
port = 1883
topic = "example/topic"

# Publish messages every 2 seconds
while True:
    message = "Hello, MQTT!"
    publish.single(topic, message, hostname=broker_address, port=port)
    print(f"Published: {message}", flush=True)
    time.sleep(2)

print("Terminated Publisher")
