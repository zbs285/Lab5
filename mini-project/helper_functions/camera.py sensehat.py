from sense_hat import SenseHat
from time import sleep

def get_sensehat():
    sense = SenseHat()
    return sense
    
def alarm(sense, flash_time):

    for i in range(0,flash_time):
        sense.clear((255, 0, 0))
        sleep(1)
        sense.clear()
        sleep(1)
