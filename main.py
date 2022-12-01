import random
import time
from threading import *


#class bob_it(Thread):
#    def run(difficulté):
#        x = random.randint(1,10)
#        print(f'==> {x}')
#        y = int(input('pèse sur le bouton'))
#        if y == x:
#            bob_it(difficulté)
#        if y != x:
#            print('tes pourris')


#class timer(Thread):
#    def run(self):
#       difficulté = int(input('choisi ta difficulté (1,2,3)'))
#        sec = 3
#        for i in range(sec):
#            if difficulté == 3:
#                print(f'{sec}')
#                time.sleep(0.5)
#                sec -= 1 
#                if sec == 0:
#                    print('game over')
#                    break
#            if difficulté == 2:
#                print(f'{sec}')
#                time.sleep(1)
#                sec -= 1 
#                if sec == 0:
#                    print('game over')
#                    break
#            if difficulté == 1:
#                print(f'{sec}')
#                time.sleep(1.5)
#                sec -= 1 
#                if sec == 0:
#                    print('game over')
#                    break
#fct_timer = timer()
#fct_bob_it = bob_it()
#    
#fct_timer.start()
#fct_bob_it.start()