#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

def multiply_polynomials_in_n2(poly1, poly2):
    polynomials_size = len(poly1)+len(poly2)
    buckets = [0]*(polynomials_size-1)
    for index1, value1 in enumerate(poly1): # O(n)
        for index2,value2 in enumerate(poly2): # O(n)
            buckets[index1+index2] += value1*value2
    return buckets
