#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
import time
import csv
from multi_n2 import multiply_polynomials_in_n2
from karatsuba import karatsuba
from fft import multi_fft

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
    return grau_do_polinomio, [int(i) for i in poly1], [int(i) for i in poly2]

def csv_multi_n2():
	files = os.listdir("instancias")
	with open('multi_n2.csv', 'w') as csvfile:
		fieldnames = ['id', 'grau', 'tempo_execucao']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		for filename in files:
			print("\n===> Filename: {0}".format(filename))
			grau, poly1, poly2 = generate_polynomials(filename)

			print("===> Grau dos Polinomios: {0}".format(grau))

			counter = 1
			elapsed_time = 0
			t = time.clock()
			while elapsed_time < 5:
				multiply_polynomials_in_n2(poly1, poly2)
				elapsed_time = time.clock() - t
				counter = counter + 1

			print("===> Tempo de médio de execução: {0}".format(elapsed_time/counter))
			print("===> Quantidade de execuções: {0}".format(counter))
			writer.writerow({'id': filename, 'grau': grau, 'tempo_execucao': elapsed_time/counter})

def csv_karatsuba():
	files = os.listdir("instancias")
	with open('karatsuba.csv', 'w') as csvfile:
		fieldnames = ['id', 'grau', 'tempo_execucao']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		for filename in files:
			print("\n===> Filename: {0}".format(filename))
			grau, poly1, poly2 = generate_polynomials(filename)

			print("===> Grau dos Polinomios: {0}".format(grau))

			counter = 1
			elapsed_time = 0
			t = time.clock()
			while elapsed_time < 5:
				karatsuba(poly1, poly2)
				elapsed_time = time.clock() - t
				counter = counter + 1

			print("===> Tempo de médio de execução: {0}".format(elapsed_time/counter))
			print("===> Quantidade de execuções: {0}".format(counter))
			writer.writerow({'id': filename, 'grau': grau, 'tempo_execucao': elapsed_time/counter})

def csv_fft():
	files = os.listdir("instancias")
	with open('fft.csv', 'w') as csvfile:
		fieldnames = ['id', 'grau', 'tempo_execucao']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		for filename in files:
			print("\n===> Filename: {0}".format(filename))
			grau, poly1, poly2 = generate_polynomials(filename)

			print("===> Grau dos Polinomios: {0}".format(grau))

			counter = 1
			elapsed_time = 0
			t = time.clock()
			while elapsed_time < 5:
				multi_fft(poly1, poly2)
				elapsed_time = time.clock() - t
				counter = counter + 1

			print("===> Tempo de médio de execução: {0}".format(elapsed_time/counter))
			print("===> Quantidade de execuções: {0}".format(counter))
			writer.writerow({'id': filename, 'grau': grau, 'tempo_execucao': elapsed_time/counter})


if __name__ == "__main__":
	print("#### CSV MULTI N2 ####")
	csv_multi_n2()
	print("#### CSV KARATSUBA ####")
	csv_karatsuba()
	#print("#### CSV FFT ####")
	#csv_fft()
