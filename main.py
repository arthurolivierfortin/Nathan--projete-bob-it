import random
import time
def bob_it(difficulté):
    x = random.randint(1,10)
    print(x)
    print(time)
    y = int(input('pèse sur le bouton'))
    if y == x:
        bob_it(difficulté)
    if y != x:
        return'tes pourris'
    
bob_it(1)