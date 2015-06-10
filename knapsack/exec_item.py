import os
import csv
import time
import greedy
import weighted
import pivot


if __name__ == "__main__":
	# Importar dados de instancias
	

	f = open("instancias/m50.in",'r')
	num_linha = 1
	qtd_items_instancia = 0
	items_instancia = []
	capacidade_mochila = 0
	for linha in f.readlines():
		if num_linha == 1:
			qtd_items_instancia = int(linha.strip())
		elif num_linha < qtd_items_instancia + 2:
			item_data = linha.split()
			nome = item_data[0]
			peso = int(item_data[2].strip())
			valor = int(item_data[1].strip())
			item = (nome, peso, valor)
			items_instancia.append(item)
		else:
			capacidade_mochila = int(linha.strip())	
		num_linha = num_linha + 1

	print("===>Tamanho da Instância: {0}".format(qtd_items_instancia))
	print("===>Capacidade da mochila: {0}".format(capacidade_mochila))

	counter = 1
	elapsed_time = 0
	t = time.process_time()
	#while elapsed_time < 5:
	items_to_add = weighted.weighted_median(weighted.prepara_items(items_instancia), capacidade_mochila)
	#elapsed_time = time.process_time() - t
	#counter = counter + 1
	peso = 0
	valor = 0
	for item in items_to_add:
		peso += item[2]
		valor += item[3]

	print("===> Peso: {0}".format(peso))
	print("===> Valor: {0}".format(valor))

	#print(items_to_add)


	f.close()	






