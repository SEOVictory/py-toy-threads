from time import sleep

from threading import Thread


class Whrrrler(object):
    play_on = False

    def play(self):
        while self.play_on:
            sleep(.5)
            print "Whrrrl!"
        pass
