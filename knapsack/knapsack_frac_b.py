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
    elements_mediana = median(elements, math.trunc((len(elements)+1)/2))

    print("Mediana das Medianas: {0}".format(elements_mediana))

    L1 = [] # Itens com valor/peso < que a mediana
    L2 = [] # Itens com valor/peso = que a mediana
    L3 = [] # Itens com valor/peso > que a mediana
    L1L2 = []
    
    for item in items:
        if item[2]/item[1] < elements_mediana[0]:
            L1.append(item)
        elif item[2]/item[1] == elements_mediana[0]:
            L2.append(item)
        else:
            L3.append(item)

    print("Elementos menores que a mediana:")
    print(L1)
    print("Elementos iguais a mediana:")
    print(L2)
    print("Elementos maiores que a mediana:")
    print(L3)        

    sum_L1 = sum(item[1] for item in L1)
    print("Soma de pesos de L1: {0}".format(sum_L1))
    sum_L2 = sum(item[1] for item in L2)
    print("Soma de pesos de L2: {0}".format(sum_L2))
    sum_L3 = sum(item[1] for item in L3)
    print("Soma de pesos de L3: {0}".format(sum_L3))
    
    if sum_L1 < W and W <= sum_L1 + sum_L2:
        return L1
    if  W > sum_L1 + sum_L2:
        L1L2.append(L1)
        L1L2.append(L2)
        return L1L2.append(weighted_median(L3,W - (sum_L1 + sum_L2)))
    if sum_L1 >= W:
        return weighted_median(L1, W)

def median(L, j):
    if len(L) <= 5:
        L.sort(key = lambda L : L[0])
        print("Sorted Elements for median")
        print(L)
        print("Position to take median: {0}".format(j))
        return L[j - 1]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(median(subList, math.trunc((len(subList)+1)/2)))
    return median(Meds, math.trunc((len(Meds)+1)/2))
    

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
            ("item6", 1.0, 5.0),
            ("item7", 2.0, 3.0)

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

    #greedy(order(items), knapsack_weight)
    items_to_add = weighted_median(items, knapsack_weight);
    print("Capacidade da Mochila: {0}".format(knapsack_weight))
    print("Itens que ficam no mochila")
    print(items_to_add)

