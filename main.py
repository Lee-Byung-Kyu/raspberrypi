import paho.mqtt.client as mqtt
import json
import Adafruit_DHT

# Raspi seosor setup
sensor = Adafruit_DHT.DHT11
pin = 2

# mqtt protocol setup
client = mqtt.Client()
client.connect('192.168.0.11', 1883)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin);
    if humidity is not None and temperature is not None:
        client.publish('/test', json.dumps({"temperature": temperature, "humidity": humidity}), 1)
        print("well published")
    else:
        print('Failed to get reading. Try again!')
        client.disconnect()
