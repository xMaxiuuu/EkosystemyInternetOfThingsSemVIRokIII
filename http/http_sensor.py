from sense_emu import SenseHat
from time import sleep
import requests

sense = SenseHat()
remote_address = ('0.0.0.0', 4050)
while True:
    humidity = round(sense.humidity)
    requests.get('http://0.0.0.0:8080/',+str())
    sleep(0.1)