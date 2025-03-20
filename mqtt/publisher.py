# PUBLISHER
from sense_emu import SenseHat
from time import sleep
import paho.mqtt.client as mqtt

sense = SenseHat()

mqtt_broker_address = "localhost"
mqtt_port = 1883

client = mqtt.Client("pub1")

try:
    client.connect(mqtt_broker_address, mqtt_port)
    client.loop_start()

    while True:
        humidity = int(round(sense.humidity))
        print(f"Publikuję: {humidity}")
        client.publish("humidity", str(humidity))
        sleep(0.2)

except Exception as e:
    print(f"Błąd: {e}")

finally:
    print("Zamykanie klienta MQTT...")
    client.loop_stop()
    client.disconnect()
