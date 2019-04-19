import numpy



our_array = numpy.array([input().split() for y in range(int(input().split()[0]))], int)
print(numpy.transpose(our_array), our_array.flatten(), sep="\n")