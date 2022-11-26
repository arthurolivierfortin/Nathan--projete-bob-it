import time

def timer():
    difficulté = int(input('choisi ta difficulté (1,2,3)'))
    sec = 3
    for i in range(sec):
        if difficulté == 3:
            print(f'{sec}')
            time.sleep(0.5)
            sec -= 1 
            if sec == 0:
                print('game over')
                break
        if difficulté == 2:
            print(f'{sec}')
            time.sleep(1)
            sec -= 1 
            if sec == 0:
                print('game over')
                break
        if difficulté == 1:
            print(f'{sec}')
            time.sleep(1.5)
            sec -= 1 
            if sec == 0:
                print('game over')
                break
timer()