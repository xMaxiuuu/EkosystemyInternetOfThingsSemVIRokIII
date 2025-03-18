from sense_emu import SenseHat
import socket
sense = SenseHat()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('100.101.5.175', 4050)
sock.bind(server_address)

green = (0,255,0)
white = (255,255,255)

while True:
    data, address = sock.recvfrom(4096)
    data = int(str(data, 'ascii'))
    print(str(data))
    value = 64 * data / 100
    pixels = [green if i < value else white for i in range(64)]
    sense.set_pixels(pixels)