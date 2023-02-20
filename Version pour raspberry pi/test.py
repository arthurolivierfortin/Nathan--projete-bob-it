import linecache

onepoint = open('1point.txt', 'r')
#for i in (1, 3777):

#    print(int(onepoint.readline(i)))
x = (onepoint.readlines())
#print(x[0][0:5])
byt_debut = 0
byt_fin = 5
for i in range(3776):
            #speaker.duty_u16(int(print(x[0][byt_debut:byt_fin])))
    print(int(x[0][byt_debut:byt_fin]))
    byt_debut += 5
    byt_fin += 5


