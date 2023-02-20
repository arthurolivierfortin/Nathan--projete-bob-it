#1point.txt  len = 3777


speaker = PWM(machine.Pin(27))
speaker.freq(1000)


def readSound(sons):
    if sons == "1point":
        byt_debut = 0
        byt_fin = 5
        onepoint = open('1point.txt', 'r')
        x = (onepoint.readlines())

        for i in range(3777):
            speaker.duty_u16(int(print(x[0][byt_debut:byt_fin])))
            #print(int(x[0][byt_debut:byt_fin]))
            byt_debut += 5
            byt_fin += 5
        


