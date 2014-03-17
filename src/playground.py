from time import sleep

from toys.whrrrler import Whrrrler
from toys.spinner import Spinner


if __name__ == '__main__':

    spinner1 = Spinner(1, 'spin-1', 1)
    spinner1.start()
    sleep(2)
    spinner1.stop()

    whrrrler = Whrrrler()
