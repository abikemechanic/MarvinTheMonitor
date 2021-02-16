import paho.mqtt.client as mqtt
import json
import os


class MQTTClient:
    def __init__(self):
        self.mqtt_client = mqtt.Client()

        self.create_endpoints()

    def create_endpoints(self):
        endpoints = os.listdir('/endpoints')
        for ep in endpoints:
            print(ep)


mq = MQTTClient()
