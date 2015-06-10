#!/usr/bin/env python
#-*- coding:utf-8 -*-


import cmath
from cmath import exp, pi

def omega(p, q):
   return exp((2.0 * pi * 1j * q) / p)

def fft(x):
   n = len(x)
   if n == 1:
      return x
   else:
      even = fft(x[0::2])
      odd =  fft(x[1::2])

      bucket = [0] * n
      for m in xrange(n/2):
         bucket[m] = even[m] + omega(n, -m) * odd[m]
         bucket[m + n/2] = even[m] - omega(n, -m) * odd[m]

      return bucket

def dft(x):
    n = len(x)

    bucket = [0] * n
    for m in range(n): #O(n)
        for k in range(n): #O(n)
            bucket[m] += x[k] * omega(n, -k * m)
    return bucket


def multi_fft(a, b):
    fft_a = fft(a)
    fft_b = fft(b)

    result = []
    for a, b in zip(fft_a, fft_b):
        result.append(a*b)
    return result
