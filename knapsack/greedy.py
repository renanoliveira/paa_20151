#!/usr/bin/env python
#-*- coding:utf-8 -*-


import random
import sys

def greedy(items, k_weight):
    #print(items)
    sorted_items = order(items) #O(nlogn)
    #print(sorted_items)
    items_knapsack = []
    total_weight = k_weight # O(1)

    for item in sorted_items: # O(n)
        total_weight = total_weight - item[2] # O(1)
        #print(total_weight)
        if (total_weight) > 0.0: # O(1)
            items_knapsack.append(item)
        else:
            #print("Appending partial_weight")
            partial_weight = item[2]+total_weight # O(1)
            #print(partial_weight)
            partial_item = ((item[3]/item[2]), item[1], partial_weight, (item[3]/item[2])*partial_weight)
            #print(partial_item)
            items_knapsack.append(partial_item)
            break

    return items_knapsack

def order(items):
    elements = []
    for name, weight, value in items:  # O(n)
        item = (value/weight, name, weight, value)   # O(1)
        elements.append(item)  # O(1)

    sort = sorted((elements), reverse = True) # TimSort (Melhor caso O(n); Pior caso O(n log n)) + O(n)
    return sort # O(n log n)

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
    sorted_items = []

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

   
    items_to_add =  greedy(items, knapsack_weight);
    print("===> Capacidade da Mochila: {0}".format(knapsack_weight))
    print("===> Itens que ficam no mochila:")
    
    peso = 0
    valor = 0
    for item in items_to_add:
        peso += item[2]
        valor += item[3]
        print(item)
        print(peso)

    print("===> Peso da mochila: {0}".format(peso))
    print("===> Valor da mochila: {0}".format(valor))
