#!/usr/bin/python2.7

from pygame import mixer 

mixer.init() #start the mixer

mixer.music.load("Octave-Savage-Nist-256.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("press p to pause press r to resume")
    print("press e to exit")
    quary = input(">>>  ")
    if quary == 'p':
        mixer.music.pause()
    elif quary == 'r':
        mixer.music.unpause()
    elif quary == 'e':
        mixer.music.stop()
    break

