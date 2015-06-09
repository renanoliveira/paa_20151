#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys
import os
import time

def multiply_polynomials_in_n2(poly1, poly2):
    polynomials_size = len(poly1)+len(poly2)
    buckets = [0]*(polynomials_size-1)
    for index1, value1 in enumerate(poly1): # O(n)
        for index2,value2 in enumerate(poly2): # O(n)
            buckets[index1+index2] += int(value1)*int(value2)
    return buckets

def generate_polynomials(line):
    f = open("instancias/" + line, 'r')
    num_linha = 1
    grau_do_polinomio = 0
    polinomio_1 = []
    polinomio_2 = []
    segunda_lista = False
    for linha in f.readlines():
        if num_linha == 1:
            grau_do_polinomio = int(linha.strip())
        else:
            if len(linha.split()) == 0:
                segunda_lista = True

            if not segunda_lista:
                polinomio_1.append(linha.split())
            else:
                polinomio_2.append(linha.split())
        num_linha = num_linha + 1


    poly1 = sum(polinomio_1, [])
    poly2 = sum(polinomio_2, [])

    f.close()
    return grau_do_polinomio, poly1, poly2


if __name__ == "__main__":
    files = os.listdir("instancias")
    for filename in files:
        grau, poly1, poly2 = generate_polynomials(filename)

        print("===> Grau dos Polinomios: {0}".format(grau))
        t = time.clock()

        multiply_polynomials_in_n2(poly1, poly2)

        elapsed_time = time.clock() - t
        print("===> Tempo de execução: {0}".format(elapsed_time))
