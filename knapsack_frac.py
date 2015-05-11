#!/usr/bin/env python
#-*- coding:utf-8 -*-

def greedy(sorted_items, k_weight, DEBUG=False):
    total_weight = 0
    total_value = 0
    pack = []

    for item_value, item_weight, item_name in sorted_items:
        fraction = min(k_weight - total_weight, item_weight)
        total_weight += fraction
        total_value += (fraction * item_value)

        pack  += [(item_name, fraction, total_value)]

        if(DEBUG):
            print("Adding => Item(Name: {0}, Fraction: {1}, Value {2})".format(item_name, fraction, (fraction * item_value)))

        if total_weight >= k_weight:
            break

    print("Total Weight = {0}".format(total_weight))
    print("Total Value = {0}".format(total_value))
    return pack


def order(items):
    return sorted(((value/weight, weight, name) for name, weight, value in items), reverse = True)

if __name__ == "__main__":
    # nome, peso e valor
    items = [
        ("item1", 1.0, 2.0),
        ("item2", 1.0, 2.5),
        ("item3", 1.0, 3.0),
        ("item4", 1.0, 4.0),
    ]

    knapsack_weight = 3.5
    sorted_items = order(items)

    print greedy(sorted_items, knapsack_weight, True)
