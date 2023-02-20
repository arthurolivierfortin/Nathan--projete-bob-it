#1point.txt  len = 3777


speaker = PWM(machine.Pin(27))
speaker.freq(1000)


def readSound(sons):
    if sons == "1point":
        onepoint = open('1point.txt', 'r')
        for i in range(3777):
            speaker.duty_u16(int(onpoint.readline(i)))
        


