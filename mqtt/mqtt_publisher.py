from sense_emu import SenseHat
from time import sleep
import paho.mqtt.client as mqtt
sense = SenseHat()

mqtt_broker_address = ('0.0.0.0', 1833)
client = mqtt.Client("pub1")
client.connect(mqtt_broker_address[0])

while True:
    humidity = round(sense.humidity)
    client.publish("humidity", str(humidity))
    sleep(0.2)
    