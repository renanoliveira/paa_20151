#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys

def multiply_polynomials_in_n2(poly1, poly2):
    polynomials_size = len(poly1)+len(poly2)
    buckets = [0]*(polynomials_size-1)
    for index1, value1 in enumerate(poly1): # O(n)
        for index2,value2 in enumerate(poly2): # O(n)
            buckets[index1+index2] += value1*value2
            print("Buckets = {0}".format(buckets))

    print("Product of the polynomials = {0}".format(buckets))
    return buckets


def generate_polynomial(size):
    items = []
    for i in range(size):
        random_value = random.uniform(1.0, 100.0)
        items.append(random_value)

    return items


if __name__ == "__main__":

    poly1 = []
    poly2 = []

    if sys.argv[1] == "test":
        print "===> Modo teste para validar alogritmo"
        poly1 = [1,2,3]
        poly2 = [4,5,6]

    elif len(sys.argv) == 3:
        poly1 = generate_polynomial(int(sys.argv[1]))
        poly2 = generate_polynomial(int(sys.argv[2]))

        print "===> Gerar polinomios com valorizes randomicos - "
        print "===> Poly1 : {0} Poly2: {1}".format(poly1, poly2)
    else:
        print "==> Não encontrei um padrão"

    multiply_polynomials_in_n2(poly1, poly2)
