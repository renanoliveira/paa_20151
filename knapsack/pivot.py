#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys
import math


# O(n2)
def weighted_pivot(items, W):

    #Se |items| == 0, não há items para adicionar a mochila
    if(len(items) == 0):
        return []

    #Se |items| == 1 e capacidade da < items[0].peso 
    if len(items) == 1 and items[0][2] > W:
        L = []
        peso_fracionario = W
        item_fracionario = (items[0][0], items[0][1], peso_fracionario, items[0][0]*peso_fracionario)
        L.append(item_fracionario)
        return L

    elements_pivot = pivot(items) #O(n)
    
    L1 = [] # Itens com valor/peso < que o pivot
    L2 = [] # Itens com valor/peso = que o pivot
    L3 = [] # Itens com valor/peso > que o pivot   

    for item in items:
        if item[0] > elements_pivot:
            L1.append(item)
        elif item[0] ==  elements_pivot:
            L2.append(item)
        else:
            L3.append(item)

    sum_L1 = sum(item[2] for item in L1)
    sum_L2 = sum(item[2] for item in L2)
    sum_L3 = sum(item[2] for item in L3)
   
    if sum_L1 + sum_L2 + sum_L3 < W:
        return L1 + L2 + L3
        
    if sum_L1 <= W and sum_L1 + sum_L2 >= W:
        for item in L2:
            if sum_L1 == W:
                break
            elif sum_L1 + item[2] > W:
                peso_fracionario = W - sum_L1
                item_fracionario = (item[0], item[1], peso_fracionario, item[0]*peso_fracionario)
                L1.append(item_fracionario)
                break
            else:
                L1.append(item)
                W = W - item[2]
        return L1
    
    if sum_L1 + sum_L2 < W:
        return L1 + L2 + (weighted_pivot(L3, W - (sum_L1 + sum_L2)))
    if sum_L1 > W:
        return weighted_pivot(L1, W)  

    print("===> Seu algorítmo está mal projetado")
    

def pivot(L):
    comprimento_l = len(L)
    somatorio_vw = sum(item[0] for item in L)

    return somatorio_vw/comprimento_l
  
def prepara_items(items):
    items_tmp = []
    for nome, peso, valor in items:
        item_tmp = (valor/peso, nome, peso, valor)
        items_tmp.append(item_tmp)
    return items_tmp


def generate_items(size):
    items = []
    for i in range(size):
        random_name = "item {0}".format(i)
        random_weight = random.uniform(1.0, 5.0)
        random_value = random.uniform(1.0, 5.0)
        item = (random_name, random_weight, random_value)
        items.append(item)
    return items

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


    items_to_add = weighted_pivot(prepara_items(items), knapsack_weight);
    print("===> Capacidade da Mochila: {0}".format(knapsack_weight))
    print("===> Itens que ficam no mochila:")
    peso = 0
    valor = 0
    for item in items_to_add:
        print(item)
        peso += item[2]
        valor += item[3]

    print("===> Peso da mochila: {0}".format(peso))
    print("===> Valor da mochila: {0}".format(valor))
