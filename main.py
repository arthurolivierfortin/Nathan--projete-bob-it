import random
from microbit import *

def wait_for_button(bon_bouton, mauvais_button):
    bon_bouton = False
    mauvais_bouton = False

    started = running_time()
