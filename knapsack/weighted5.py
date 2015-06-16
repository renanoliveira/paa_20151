#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys
import math
import numpy
import weighted_lib


# O(n)
def weighted_median(items, W):

    valorpeso_tmp = []
    nome_tmp = []
    peso_tmp = []
    valor_tmp = []
    for nome, peso, valor in items:
        valorpeso_tmp.append(valor/peso)
        nome_tmp.append(nome)
        peso_tmp.append(peso)
        valor_tmp.append(valor)
    #print(peso_tmp)
    #print(valor_tmp)
    
    mediana = weighted_lib.median(numpy.array(valor_tmp),numpy.array(peso_tmp))
    #print(mediana)
    
    if(len(items) == 0):
        return []
        #print(items)

    if (len(items) == 1):
        #print("===> Peso fracionario: {0}".format(peso_fracionario))
        peso_fracionario = W
        peso_kilo=items[0][2]/items[0][1]
        L1_fracionado = [(items[0][0], peso_fracionario, (peso_kilo*peso_fracionario))]
        return L1_fracionado
        
        L1 = [] # Itens com valor/peso < que a mediana
        L2 = [] # Itens com valor/peso = que a mediana
        L3 = [] # Itens com valor/peso > que a mediana 

        for item in items:
            #print(item)
            if item[2] > mediana:
                L1.append(item)
            elif item[2] ==  mediana:
                L2.append(item)
            else:
                L3.append(item)

        sum_L1 = sum(item[1] for item in L1)
        #print("Soma de pesos de L1: {0}".format(sum_L1))
        sum_L2 = sum(item[1] for item in L2)
        #print("Soma de pesos de L2: {0}".format(sum_L2))
        sum_L3 = sum(item[1] for item in L3)
        #print("Soma de pesos de L3: {0}".format(sum_L3))
        
   
        if sum_L1 < W and sum_L1 + sum_L2 >= W:
            #print("===> Adiciona frações")
            for item in L2:
                #if sum_L1 == W:
                 #   break
                if sum_L1 + item[2] > W:
                    peso_fracionario = W - sum_L1
                    item_fracionario = (item[0], item[1], peso_fracionario, item[0]*peso_fracionario)
                    L1.append(item_fracionario)
                    break
                else:
                    L1.append(item)
                    W = W - item[2]
            return L1
        if sum_L1 + sum_L2 < W:
            return L1 + L2 + (weighted_median(L3, W - (sum_L1 + sum_L2)))
        if sum_L1 > W:
            return weighted_median(L1, W)  
   
##################################################################################################

if __name__ == "__main__":

    knapsack_weight = 0.0
    items = []

    #Modo de teste com valores pré-definidos
    if sys.argv[1] == "test":
        print("===> Modo teste para validar alogritmo")
        
        items = [
            ("item1", 1.0, 2.0),
            ("item2", 1.0, 2.5),
            ("item3", 1.0, 3.0),
            ("item4", 1.0, 4.0),
            ("item5", 1.0, 1.0),
            ("item6", 1.0, 5.0)
        ]

        knapsack_weight = 3.5

    #Modo de teste com valores e pesos de items gerados aleatóriamente   
    elif len(sys.argv) == 3:

        knapsack_weight = float(sys.argv[1])
        item_size = int(sys.argv[2])

        print("===> Gerarando mochila com valorizes randomicos - ")
        print("===> {0} de peso e {1} items".format(knapsack_weight, item_size))
        items = generate_items(item_size)

    #Erro ao chamar linha de comando    
    else:
        print("==> Não encontrei um padrão")

    items_to_add = weighted_median(items, knapsack_weight);
    print("===> Capacidade da Mochila: {0}".format(knapsack_weight))
    print("===> Itens que ficam no mochila:")
   
    print(items_to_add)