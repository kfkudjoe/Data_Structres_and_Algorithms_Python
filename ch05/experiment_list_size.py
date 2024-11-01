import sys

try:
    n = int(sys.argv[1])
except:
    n = 100

data = []

for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)     # actual size in bytes

    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)       # increae length by one
