import cmath
from numpy import real
from cmath import exp, pi

"""
    Evaluates the polynomial p(x) of degree n-1 in the n nth roots of unity
    in O(n log n) time.

    It does so recursively by distributing the coefficients of p(x) over
    two polynomials of degree n/2-1. Suppose 2 divides n and let m = n / 2.
    Let
        p(x) = a_0 x^0 + a_1 x^1 + a_2 x^2 + ... + a_{2m-1} x^{2m-1}
    then define
        u(x) = a_0 x^0 + a_2 x^1 + a_4 x^2 + ... + a_{2m-2} x^{m-1}
    and
        v(x) = a_1 x^0 + a_3 x^1 + a_5 x^2 + ... + a_{2m-1} x^{m-1}.
    u(x) and v(x) are both of degree m-1 and p(x) = u(x^2) + x v(x^2).

    Suppose our algorithm works, then we are able to evaluate u(x) and v(x) in the m mth
    roots of unity. To each mth root of unity z corresponds two nth roots of unity
    sqrt(z) and -sqrt(z). Hence we can evaluate p(x) for all nth roots of unity by
    letting
        p(sqrt(z)) = u(z) + sqrt(z) v(z)
    and
        p(-sqrt(z)) = u(z) - sqrt(z) v(z).

    When n = 1, p(x) = a_0 and evaluating it for any x yields a_0.

    The recurrence relation is T(n) = 2 T(n/2) + O(n) and by the master
    theorem: T(n) = O(n log n).
"""

def omega(p, q):
   return exp((2.0 * pi * 1j * q) / p)

def fft(x):
   # print "fft"
   n = len(x)
   if n == 1:
      return x
   elif n%2==1:
      return dft(x)
   else:
      even = fft(x[0::2]) #2T(n/2)
      odd =  fft(x[1::2])

      bucket = [0] * n
      for m in xrange(n/2): #(n/2)
         bucket[m] = even[m] + omega(n, -m) * odd[m]
         bucket[m + n/2] = even[m] - omega(n, -m) * odd[m]

      return bucket

def dft(x):
    # print "dft"
    n = len(x)

    bucket = [0] * n
    for m in range(n): #O(n)
        for k in range(n): #O(n)
            bucket[m] += x[k] * omega(n, -k * m)
    return bucket


def multi_fft(a, b):
    a = fft(a)
    b = fft(b)

    C = []
    for a, b in zip(a, b):
        C.append(a*b)
    return C



# for f in dft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]):
#     print abs(f)
#
# for f in fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]):
#     print abs(f)
