import random
import time
from threading import *

class bob_it(Thread):
    def run(self):
        chiffre = random.randint(1, 10) 
        print(chiffre)
        x = int(input("choisi le bon chiffre"))
        if x == chiffre:
            fct_timer = timer()
            fct_bob_it = bob_it()
    
            fct_timer.start()
            fct_bob_it.start()
        else:
            print("game over")
            return
        



class timer(Thread):
    def run(self):
        sec = 3
        for i in range(sec):
                time.sleep(2)
                sec -= 0,5 
                if sec == 0:
                    print('game over')
                    break
            
fct_timer = timer()
fct_bob_it = bob_it()
    
fct_timer.start()
fct_bob_it.start()