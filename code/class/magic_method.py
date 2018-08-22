#!/usr/bin/env python3

class Bird(object):
    def __init__(self, sound):
        self.sound = sound
        print("my sound is:", sound)
    def chirp(self):
        print(self.sound)

summer = Bird("ji")
summer.chirp()
