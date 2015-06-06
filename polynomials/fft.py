import cmath
from numpy import real
from cmath import exp, pi

def roots_of_unity(period):
    return [exp(-1j*2.*pi*j/period) for j in xrange(period)]

def poly_eval(coefs, xs):
    p = [0 for x in xs]
    for k, x in enumerate(xs):
        for j, c in enumerate(coefs):
            p[k]+=(c*pow(x,j))
    return p

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

def dft(xs):
    print "dft"
    n = len(xs)
    return poly_eval(xs, roots_of_unity(n))

a = fft([1,2,3,4,5,6])
b = fft([1,2,3,4])

C = []
for a, b in zip(a, b):
    C.append(a*b)
print C
