#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math

def eh_impar(num):
	return num & 0x1

def karatsuba(A, B):

	degree = len(A) - 1
	if(eh_impar(degree)):
		N = degree +1
	else:
		N = degree

	if(degree == 0):
		return [A[0]*B[0]]

	split_at = math.ceil((degree+1)/2)
	#print("spliting at: {0}".format(split_at))
	Al = A[0:split_at]
	#print("Al:")
	#print(Al)
	Au = A[(split_at):(len(A))]
	#print("Au:")
	#print(Au)
	Bl = B[0:split_at]
	#print("Bl:")
	#print(Bl)
	Bu = B[(split_at):(len(A))]
	#print("Bu:")
	#print(Bu)

	#Ajusta tamanho das partes do polinômio para permitir soma de coeficiêntes
	if(len(Al) != len(Au)):
		Au.insert(0, 0)
		#print("Ajusta Au:")
		#print(Au)
	if(len(Bl) != len(Bu)):
		Bu.insert(0, 0)
		#print("Ajusta Bu:")
		#print(Bu)

	sum_Al_Au = [x + y for x, y in zip(Al, Au)]
	#print("Sum Al + Au")
	#print(sum_Al_Au) 
	sum_Bl_Bu = [x + y for x, y in zip(Bl, Bu)]
	#print("Sum Bl + Bu")
	#print(sum_Bl_Bu)

	z0 = karatsuba(Al,Bl)
	#print(z0)
	z1 = karatsuba(Au,Bu)
	#print(z1)
	z2 = karatsuba(sum_Al_Au, sum_Bl_Bu)
	#print(z2)
	sub_z2_z1 = [x - y for x, y in zip(z2, z1)]	
	z01 = [x - y for x, y in zip(sub_z2_z1, z0)]
	#print(z01)

	#Ajusta polinômios resultantes para soma
	#print(N)
	for x in range (0, N):
		z1.insert(0, 0)
		z0.append(0)

	for x in range (0, int(N/2)):
		z01.insert(0,0)
		z01.append(0)

	return [x + y + z for x, y, z in zip(z1, z01, z0)]	

#print(karatsuba([1, 4],[2, 6])) #[2, 14, 24]
#print(karatsuba([1, 2, 3],[1, 6, 2])) #[1, 8, 17, 22, 6]
#print(karatsuba([1, 1, 3, 2],[1, 2, 5, 1])) #[1, 3, 10, 14, 20, 13, 6]
#print(karatsuba([1, 1, 3, 1, 2],[1, 5, 2, 3, 1])) #[1, 6, 10, 21, 17, 22, 10, 7, 2]
#print(karatsuba([0, 0, 15, 0, 2, 0],[0, 0, 0, -1, 0, 5])) #[0, 0, 0, 0, 0, 15, 0, 73, 0, 10]
#print(karatsuba([0, -44, 0, 2], [0, 1, -50, -1])) #[0, 0, -44, 2200, 46, -100, -2]
#print(karatsuba([0, 0, 0, -1, 0, 5],[0, 0, -1, 0, 1, 0])) #[0, 0, 0, 0, 0, 1, 0, -6, 0, 5, 0]
