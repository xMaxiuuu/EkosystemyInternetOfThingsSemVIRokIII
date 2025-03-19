from sense_emu import SenseHat
from http.server import BaseHTTPRequestHandler, HTTPServer

#Kolorki
green = (0,255,0)
white = (255,255,255)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        print(self.path[1:]) / 100
        value = 64*int(self.path[1:])/100
        pixels = [green if i < value else white for i in range(64)]
        sense.set_pixels(pixels)

sense = SenseHat()