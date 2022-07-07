from sys import argv

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

def main():
    if len(argv) == 1 :
        print("tusic [file name] [number of replay(-1 to infinite replay,default -1)]")
    elif len(argv) > 1 :
        mixer.init()
        mixer.music.load(argv[1])
        mixer.music.set_volume(0.7)
        mixer.music.play(-1)
        
        while True:
            print("Press 'p' to pause, 'r' to resume")
            print("Press 'e' to exit the program")
            query = input(">")
            if query == 'p':
                mixer.music.pause()     
            elif query == 'r':
                mixer.music.unpause()
            elif query == 'e':
                mixer.music.stop()
                break