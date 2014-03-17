from time import sleep

from threading import Thread


class Spinner(object):
    play_on = False
    def play(self):

        while self.play_on:
            sleep(.5)
            print 'Spin!'

        pass
