from Matplotlib import numpy
data = numpy.memmap("C:/Users/arthur/OneDrive/Projet bob-it/Sons - pcm/1point.pcm", dtype='h', mode='r')
print ("VALUES:",data)