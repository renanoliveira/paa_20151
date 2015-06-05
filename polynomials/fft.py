import cmath
from numpy import real

def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def fft(x):
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
    print "implementar"

a = fft([1,2])
b = fft([1,2])
print fft([1,2])

C = []
for a, b in zip(a, b):
    C.append(a*b)
print C
