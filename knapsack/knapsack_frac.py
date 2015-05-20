#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys

def greedy(sorted_items, k_weight):
    total_weight = k_weight # O(1)
    total_value = 0 # O(1)

    for item_value, item_weight, item_name in sorted_items: # O(n)
        total_weight = total_weight - item_weight # O(1)
        if (total_weight) > 0.0: # O(1)
            print("Adding => Item(Name: {0}, Weight: {1}, Value {2})".format(item_name, item_weight, (item_weight * item_value)))
            total_value += item_value # O(1)
        else:
            particial_weight = item_weight+total_weight # O(1)
            total_value += (particial_weight * item_value) # O(1)

            print("Adding => Item(Name: {0}, Weight: {1}, Value {2})".format(item_name, particial_weight, (particial_weight * item_value)))
            break

    print("Total Value = {0}".format(total_value))



def order(items):
    elements = []
    for name, weight, value in items:  # O(n)
        item = (value/weight, weight, name)   # O(1)
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
        print "===> Modo teste para validar alogritmo"
        items = [
            ("item1", 1.0, 2.0),
            ("item2", 1.0, 2.5),
            ("item3", 1.0, 3.0),
            ("item4", 1.0, 4.0)
        ]

        knapsack_weight = 3.5
        sorted_items = order(items)
    elif len(sys.argv) == 3:
        knapsack_weight = float(sys.argv[1])
        item_size = int(sys.argv[2])

        print "===> Gerar mochila com valorizes randomicos - "
        print "===> {0} de peso e {1} items".format(knapsack_weight, item_size)

        sorted_items = order(generate_items(item_size))
    else:
        print "==> Não encontrei um padrão"

    greedy(sorted_items, knapsack_weight)
