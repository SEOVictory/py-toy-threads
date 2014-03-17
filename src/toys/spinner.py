from time import sleep


class Spinner(object):
    play_on = False

    def play(self):

        while self.play_on:
            sleep(.5)
            print 'Spin!'
