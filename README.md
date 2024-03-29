MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol that is widely used in the Internet of Things (IoT) and other applications where low bandwidth and high latency are common.

The Paho MQTT library is a popular choice for implementing MQTT in Python.

Here's an example of using Mosquitto as the MQTT broker and Python with the Paho library to publish and subscribe to MQTT topics.

Step 1: Install Mosquitto

Step 2: Start Mosquitto Broker
`mosquitto`

Step 3: Install Paho MQTT library
`pip install paho-mqtt`

Step 4: Run the Subscriber
- to subscribe to the MQTT topic and receive messages.

`python mqtt_subscriber.py`

Step 4: Run the Publisher
- publish messages to an MQTT topic.

`python mqtt_publisher.py`


## Run using docker pythong image
```
docker run -it --rm --name mqtt_subscriber -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python mqtt_subscriber.py
```

```
docker run -it --rm --name mqtt_publisher -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python mqtt_publisher.py
```

https://cedalo.com/blog/mosquitto-docker-configuration-ultimate-guide/

https://github.com/eclipse/mosquitto/issues/1580


```
docker-compose -f eclipse-mosquitto-docker-compose.yml up -d
```

```
docker ps

docker inspect CONTAINER_ID | grep "IPAddress"
```

```
services:
    ...
    networks:
      - mosquitto
networks:
    mosquitto:
        name: mosquitto
        driver: bridge
```

