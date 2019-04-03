import argparse
import math
from playsound import playsound
from osc import OSCServer
from sys import exit
from random import randint

class RoboEmoOSCServer(OSCServer):

    def handle(self, address, message, time):
        emotion_num = 0
        dev_mode = True

        if(dev_mode):
            if(message.address == "/1/push1"):
                emotion_num = 1
            elif(message.address == "/1/push2"):
                emotion_num = 2
            elif(message.address == "/1/push3"):
                emotion_num = 3
            
            if(message.args[0] == 1 and emotion_num != 0):
                chooseSound(emotion_num)
        else:
            emotion_num = message.args[0]
            if(message.address == "/roboEmo"):
                chooseSound(emotion_num)
        
        # print(time, address, message.address, message.args)

def chooseSound(emotion):
    rand = randint(1, 100)
    sounds_dir = "sounds/"
    sound_name = ""

    if(emotion == 1):
        # Anger
        sound_num = rand % 2 + 1
        sound_name = sounds_dir + "anger" + str(sound_num) + ".wav"
    elif (emotion == 2):
        # Happy
        sound_num = rand % 1 + 1
        sound_name = sounds_dir + "happy" + str(sound_num) + ".wav"
    else:
        # Sad
        sound_num = rand % 2 + 1
        sound_name = sounds_dir + "sad" + str(sound_num) + ".wav"
    print(sound_name)
    playsound(sound_name)

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