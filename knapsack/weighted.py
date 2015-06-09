#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import sys
import math


# O(n)
def weighted_median(items, W):

    #Se |items| == 0, não há items para adicionar a mochila
    if(len(items) == 0):
        return []

    #Se |items| == 1 e capacidade da < items[0].peso 
    if len(items) == 1 and items[0][2] > W:
        L = []
        print("===> Peso fracionario: {0}".format(peso_fracionario))
        peso_fracionario = W
        item_fracionario = (items[0][0], items[0][1], peso_fracionario, items[0][0]*peso_fracionario)
        L.append(item_fracionario)
        return L

    elements_mediana = median(items, math.ceil((len(items)+1)/2))
    #print("===> Mediana das Medianas: {0}".format(elements_mediana))
    
    L1 = [] # Itens com valor/peso < que a mediana
    L2 = [] # Itens com valor/peso = que a mediana
    L3 = [] # Itens com valor/peso > que a mediana   

    for item in items:
        if item[0] > elements_mediana[0]:
            L1.append(item)
        elif item[0] ==  elements_mediana[0]:
            L2.append(item)
        else:
            L3.append(item)


    print("===> Capacidade da Mochila")
    print(W)
    #print("===> Elementos maiores que a mediada:")
    #print(L1)
    #print("===> Elementos iguais a mediada:")
    #print(L2)
    #print("===> Elementos menores que a mediana:")
    #print(L3)

    sum_L1 = sum(item[2] for item in L1)
    print("Soma de pesos de L1: {0}".format(sum_L1))
    sum_L2 = sum(item[2] for item in L2)
    print("Soma de pesos de L2: {0}".format(sum_L2))
    sum_L3 = sum(item[2] for item in L3)
    print("Soma de pesos de L3: {0}".format(sum_L3))
   
    if sum_L1 < W and sum_L1 + sum_L2 >= W:
        print("===> Adiciona frações")
        for item in L2:
            print(item)
            print(sum_L1)
            print(W)
            if sum_L1 == W:
                break
            elif sum_L1 + item[2] > W:
                peso_fracionario = W - sum_L1
                print("===> Peso fracionario: {0}".format(peso_fracionario))
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

    #print("===> Seu algorítmo está mal projetado")
    

def median(L, j):

    if len(L) <= 5:
        #Ordena do maior para o menor lista de no máximo 5 elementos
        #Retorna elemento na posição j - 1
        L.sort(key = lambda L : L[0], reverse = True)
        return L[j - 1]

    #Particiona items em grupos de 5   
    S = []
    lIndex = 0
    while lIndex+5 < len(L):
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])

    Meds = []
    for subList in S:
        #Calcula mediana das medianas recursivamente a partir do agrupamento das medianas dos grupos de 5 items
        Meds.append(median(subList, math.ceil((len(subList)+1)/2)))
    return median(Meds, math.ceil((len(Meds)+1)/2))
    
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

    items_to_add = weighted_median(prepara_items(items), knapsack_weight);
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
