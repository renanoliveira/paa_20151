import cmath
from numpy import real
from cmath import exp, pi

def omega(p, q):
   return exp((2.0 * pi * 1j * q) / p)

def fft(x):
   print "fft"
   n = len(x)
   if n == 1:
      return x
   elif n%2==1:
      return dft(x)
   else:
      even = fft(x[0::2])
      odd =  fft(x[1::2])

      bucket = [0] * n
      for m in xrange(n/2):
         bucket[m] = even[m] + omega(n, -m) * odd[m]
         bucket[m + n/2] = even[m] - omega(n, -m) * odd[m]

      return bucket

def dft(x):
    print "dft"
    n = len(x)

    b = [0+0j] * n
    for m in range(n): #O(n)
        for k in range(n): #O(n)
            b[m] += x[k]*omega(n, -k*m)
    return b


# for f in dft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]):
#     print abs(f)
#
# for f in fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]):
#     print abs(f)
#
a = fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])
b = fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])

C = []
for a, b in zip(a, b):
    C.append(a*b)
print C
