import argparse
import math
from playsound import playsound
from osc import OSCServer
from sys import exit

class RoboEmoOSCServer(OSCServer):

  def handle(self, address, message, time):
    if message.address == "/1/push1" and message.args[0] == 1.0:
        playsound('roboroar.wav')
        print(time, address, message.address, message.args)

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip",
            default="0.0.0.0", help="The ip to listen on")
        parser.add_argument("--port",
            type=int, default=5000, help="The port to listen on")
        args = parser.parse_args()

        server = RoboEmoOSCServer(args.ip, args.port)

        print("Serving on {}".format(server.server_address))
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)