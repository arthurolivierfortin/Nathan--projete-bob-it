import numpy
import 1point
data = numpy.memmap("1point.pcm", dtype='h', mode='r')
print ("VALUES:",data)