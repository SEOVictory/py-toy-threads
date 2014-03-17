from time import sleep

from threading import Thread


class Spinner(Thread):
    play_on = True
    thread_id = None
    name = None
    counter = None

    def __init__(self, thread_id, name, counter):
        super(Spinner, self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting to play"

        while self.play_on:
            sleep(.5)
            print 'Spin!', self.thread_id, self.name, self.counter

    def stop(self):
        self.play_on = False
