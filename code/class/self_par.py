#!/usr/bin/env python3
class Bird(object):
    def chirp(self, sound):
        print(sound)

    def chirp_repeat(self, sound, n):
        for i in range(0, n):
            self.chirp(sound)
summer = Bird()
summer.chirp_repeat('ji', 10)
