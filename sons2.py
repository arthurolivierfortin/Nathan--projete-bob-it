import wave

son = open("C:/Users/arthu/OneDrive/Projet bop-it/Sons/Glassbreaker SFX/8KHZ 8bit/1point.wav", "r", encoding="U8")

sonl = wave.Wave_read.readframes((wave.open("C:/Users/arthu/OneDrive/Projet bop-it/Sons/Glassbreaker SFX/8KHZ 8bit/1point.wav", 'r')), 3700)
print(type(sonl))
sonl = str(sonl)
sonl.replace('', '0xe6')
sonl = bytes(sonl, 'utf-8')
#print(sonl)
print(sonl.decode())
#open("1point.txt")