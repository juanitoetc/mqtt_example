# Simple python MQTT publisher/subscriber example

## Installation
`python3 -m pip install paho-mqtt`

## Extra information
There are two different developed scripts.  
`mqtt_publisher.py` shares information to the selected MQTT broker (pick between `mqtt.eclipseprojects.io` or `public.mqtthq.com`) using the defined topic.  
`mqtt_subscriber.py` connects also to the same MQTT broker, and subscribe to the topic to receive the published data.

## Run
In one terminal execute the subscriber which will listening to messages from publisher:
`python3 src/mqtt_subscriber.py`

In another terminal execute the publisher which will send messages to any subscriber listening:
`python3 src/mqtt_publisher.py`

## Close
Press `Ctrl + c` on each terminal