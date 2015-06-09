import os
import csv
import time
import greedy
import weighted
import pivot


if __name__ == "__main__":
	# Importar dados de instancias
	files = os.listdir("instancias")

	with open('weighted_pivot.csv', 'w') as csvfile:
		fieldnames = ['instancia', 'tempo_execucao', 'valor_mochila', 'peso_mochila', 'capacidade_mochila', 'peso_total']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for filename in files:
			num_linha = 1
			qtd_items_instancia = 0
			items_instancia = []
			capacidade_mochila = 0
			peso_total_items = 0
			f = open("instancias/" + filename,'r')
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
			#print("===>Capacidade da mochila: {0}".format(capacidade_mochila))

			peso_total_items = sum(item[1] for item in items_instancia)

			#print("===>Usando algorítmo com pivot")
			counter = 1
			elapsed_time = 0
			t = time.process_time()
			while elapsed_time < 5:
				items_to_add = pivot.weighted_pivot(pivot.prepara_items(items_instancia), capacidade_mochila)
				elapsed_time = time.process_time() - t
				counter = counter + 1
			
			peso = 0
			valor = 0
			for item in items_to_add:
				peso += item[2]
				valor += item[3]

			writer.writerow({'instancia': qtd_items_instancia, 'tempo_execucao': round(elapsed_time/counter, 10), 'valor_mochila': valor, 'peso_mochila': peso, 'capacidade_mochila': capacidade_mochila, 'peso_total': peso_total_items})

		print("===> Tempo inicial: {0}".format(t))
		print("===> Tempo de execução: {0}".format(elapsed_time))
		f.close()	



	with open('weighted_median.csv', 'w') as csvfile:
		fieldnames = ['instancia', 'tempo_execucao', 'valor_mochila', 'peso_mochila', 'capacidade_mochila', 'peso_total']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for filename in files:
			num_linha = 1
			qtd_items_instancia = 0
			items_instancia = []
			capacidade_mochila = 0
			peso_total_items = 0
			f = open("instancias/" + filename,'r')
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

			print("===>Usando algorítmo de weighted medians")
			counter = 1
			elapsed_time = 0
			t = time.process_time()
			while elapsed_time < 5:
				items_to_add = weighted.weighted_median(weighted.prepara_items(items_instancia), capacidade_mochila)
				elapsed_time = time.process_time() - t
				counter = counter + 1

			peso = 0
			valor = 0
			for item in items_to_add:
				peso += item[2]
				valor += item[3]

			writer.writerow({'instancia': qtd_items_instancia, 'tempo_execucao': round(elapsed_time/counter, 10), 'valor_mochila': valor, 'peso_mochila': peso, 'capacidade_mochila': capacidade_mochila, 'peso_total': peso_total_items})

		print("===> Tempo inicial: {0}".format(t))
		print("===> Tempo de execução: {0}".format(elapsed_time))
		f.close()


	with open('greedy.csv', 'w') as csvfile:
		fieldnames = ['instancia', 'tempo_execucao', 'valor_mochila', 'peso_mochila', 'capacidade_mochila', 'peso_total']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for filename in files:
			num_linha = 1
			qtd_items_instancia = 0
			items_instancia = []
			capacidade_mochila = 0
			peso_total_items = 0
			f = open("instancias/" + filename,'r')
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

			print("===>Usando algorítmo greed")
			counter = 1
			elapsed_time = 0
			t = time.process_time()
			while elapsed_time < 5:
				items_to_add = greedy.greedy(items_instancia, capacidade_mochila)
				elapsed_time = time.process_time() - t
				counter = counter + 1
			
			peso = 0
			valor = 0
			for item in items_to_add:
				peso += item[2]
				valor += item[3]
			writer.writerow({'instancia': qtd_items_instancia, 'tempo_execucao': round(elapsed_time/counter, 10), 'valor_mochila': valor, 'peso_mochila': peso, 'capacidade_mochila': capacidade_mochila, 'peso_total': peso_total_items})

		print("===> Tempo inicial: {0}".format(t))
		print("===> Tempo de execução: {0}".format(elapsed_time))
		f.close()



