import wave


son = wave.open("C:/Users/arthu/OneDrive/Projet bop-it/Sons/Glassbreaker SFX/8KHZ 8bit/1point.wav")
print(wave.Wave_read.getcomptype(son))
print(wave.Wave_read.getcompname(son))
print(wave.Wave_read.getsampwidth(son))
print(wave.Wave_read.getnframes(son))
print(wave.Wave_read.readframes(son, 3700))
wave.Wave_read.close(son)

