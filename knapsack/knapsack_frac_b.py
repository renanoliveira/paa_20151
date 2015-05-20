#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys
import math


# O(n)
def weighted_median(items, W):

    print("Peso Mochila: {0}".format(W))
    elements = []
    for name, weight, value in items: 
        item = (value/weight, weight, value, name)
        print(item)
        elements.append(item)

    print("Elementos para cálculo da mediana:")
    print(elements)
    elements_mediana = median(elements, math.ceil((len(elements)+1)/2))

    print("Mediana das Medianas: {0}".format(elements_mediana))

    L1 = [] # Itens com valor/peso <= que a mediana
    L2 = [] # Itens com valor/peso > que a mediana
    
    for item in items:
        if item[2]/item[1] <= elements_mediana[0]:
            L1.append(item)
        else:
            L2.append(item)

    print("Elementos menores ou iguais a mediana:")
    print(L1)
    print("Elementos maiores que a mediana:")
    print(L2)

    sum_L1 = sum(item[1] for item in L1)
    print("Soma de pesos de L1: {0}".format(sum_L1))
    sum_L2 = sum(item[1] for item in L2)
    print("Soma de pesos de L2: {0}".format(sum_L2))
   
    if sum_L1 + sum_L2 < W:
        return items
    if sum_L2 < W and (sum_L1 + sum_L2) > W:
        L2.extend(weighted_median(L1,W - (sum_L2))) 
        print(L2)
        return L2
    if sum_L2 > W:
        if len(L2) == 1:
            print("returning L2")
            print(L2)
            tmp = list(L2[0])
            tmp[2] = (tmp[2]/tmp[1])*W
            tmp[1] = W
            L2[0] = tuple(tmp)
            print(L2)
            return L2
        else:
            return weighted_median(L2, W)   

def median(L, j):
    if len(L) <= 5:
        L.sort(key = lambda L : L[0], reverse = True)
        print("Sorted Elements for median")
        print(L)
        print("Position to take median: {0}".format(j))
        return L[j - 1]
    S = []
    lIndex = 0
    while lIndex+5 < len(L):
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        print(len(subList))
        Meds.append(median(subList, math.ceil((len(subList)+1)/2)))
    return median(Meds, math.ceil((len(Meds)+1)/2))
    

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
        
    elif len(sys.argv) == 3:
        knapsack_weight = float(sys.argv[1])
        item_size = int(sys.argv[2])

        print("===> Gerar mochila com valorizes randomicos - ")
        print("===> {0} de peso e {1} items".format(knapsack_weight, item_size))

        items = generate_items(item_size)
    else:
        print("==> Não encontrei um padrão")

    items_to_add = weighted_median(items, knapsack_weight);
    print("Capacidade da Mochila: {0}".format(knapsack_weight))
    print("Itens que ficam no mochila")
    print(items_to_add)
    peso = 0
    valor = 0
    for item in items_to_add:
        print(item)
        peso += item[1]
        valor += item[2]
    print("Peso da mochila: {0}".format(peso))
    print("Valor da mochila: {0}".format(valor))
