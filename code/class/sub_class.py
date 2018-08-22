#!/usr/bin/env python3
class Bird(object):
    feather = True
    reproduction = "egg"

    def chirp(self, sound):
        print(sound)

#define a subclass chicken
class Chicken(Bird):
    how_to_move = "walk"
    edible = True

#define a subclass swan
class Swan(Bird):
    how_to_move = "swim"
    edible = False

summer = Chicken()
print(summer.feather)
summer.chirp("ji")
print(summer.how_to_move)
