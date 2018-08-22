#!/usr/bin/env python3

#create a bird class
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
#class attribute: chirp
    def chirp(self, sound):
        print(sound)

#object attribute: set_color
    def set_color(self, color):
        self.color = color



summer = Bird()
print(summer.way_of_reproduction)
summer.chirp('jijijiji')
summer.set_color('yellow')
print(summer.color)
