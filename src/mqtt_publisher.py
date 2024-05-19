import paho.mqtt.client as mqtt
from paho.mqtt.enums import MQTTErrorCode
from random import randrange, uniform
from time import sleep

# Broker info
# Broker = "mqtt.eclipseprojects.io"
Broker = "public.mqtthq.com"
TCPPort = 1883
WebSocketPort = 8083
WebSocketPath ="/mqtt"

# MQTT Topic info
Topic = "mqtt-topic-1"
QoS = 0


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Successfully connected to: {}".format(Broker))
    else:
        print("Failed to connect code: {}.".format(reason_code))
        raise Exception


def on_publish(client, userdata, mid, reason_code, properties):
    # reason_code and properties will only be present in MQTTv5.
    # It's always unset in MQTTv3
    if reason_code == 0:
        pass
    else:
        print("Error detected: {}".format(reason_code))
    

unacked_publish = set()
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.on_connect = on_connect
publisher.on_publish = on_publish

# This will trigger the on_connect method
publisher.connect(Broker)
# Replace to a condition of connected successfully
sleep(2)
publisher.loop_start()

while True:

    randNumber = uniform(15.0, 25.0)
    print("Sending: {} ...".format(randNumber))
    (msg_info, mid) = publisher.publish(Topic, randNumber, qos=QoS)
    sleep(3)
    if msg_info != MQTTErrorCode.MQTT_ERR_SUCCESS:
        print("Error: {}".format(msg_info))
        unacked_publish.add(mid)
        print("mid not delivered to Broker:\n{}".format(unacked_publish))

publisher.loop_stop()
