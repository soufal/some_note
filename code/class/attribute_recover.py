#!/usr/bin/env python3
class Bird(object):
    def chirp(self):
         print("make sound")

class Chicken(Bird):
    def chirp(self):
        super().chirp()    #enpand father
        print("ji")

bird = Bird()
bird.chirp()

summer = Chicken()
summer.chirp()
