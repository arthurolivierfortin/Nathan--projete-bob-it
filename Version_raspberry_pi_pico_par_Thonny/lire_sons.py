speaker = PWM(machine.Pin(27))
speaker.freq(8000)


def readSound(son):
    if sons == "1point":
        onepoint = open('1point.txt', 'r')
        x = (onepoint.readlines())

        for i in range(3777):
            speaker.duty_u16(int(print(x[i][0:5])))
            #print(int(x[0][byt_debut:byt_fin]))
            
readSound("1point")          
