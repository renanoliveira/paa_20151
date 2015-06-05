import os
import time
import greedy
import weighted
import pivot

if __name__ == "__main__":
	# Importar dados de instancias
	files = os.listdir("instancias")

	for filename in files:
		num_linha = 1
		qtd_items_instancia = 0
		items_instancia = []
		capacidade_mochila = 0
		f = open("instancias/" + filename,'r')
		for linha in f.readlines():
			print(linha)
			if num_linha == 1:
				qtd_items_instancia = int(linha.strip())
			elif num_linha < qtd_items_instancia + 2:
				item_data = linha.split()
				nome = item_data[0]
				peso = int(item_data[1].strip())
				valor = int(item_data[2].strip())
				item = (nome, peso, valor)
				items_instancia.append(item)
			else:
				capacidade_mochila = int(linha.strip())	
			num_linha = num_linha + 1

		print("===>Tamanho da Instância: {0}".format(qtd_items_instancia))
		print("===>Capacidade da mochila: {0}".format(capacidade_mochila))

		print("===>Usando algorítmo greed")
		t = time.process_time()
		greedy.greedy(items_instancia, capacidade_mochila)
		elapsed_time = time.process_time() - t

		print("===> Tempo inicial: {0}".format(t))
		print("===> Tempo de execução: {0}".format(elapsed_time))
		f.close()



