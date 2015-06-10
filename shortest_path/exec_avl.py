import os
import csv
import time
import dijkstra_avl


if __name__ == "__main__":
	# Importar dados de instancias
	files = os.listdir("instancias/avl")

	with open('avl.csv', 'w') as csvfile:
		fieldnames = ['instancia', 'nodes', 'edges', 'tempo_execucao']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for filename in files:
			g = dijkstra_avl.Graph()

			f = open("instancias/avl/" + filename,'r')
			f_words = f.read()
			f_words = f_words.split()
			f.close()

			Nodes = int(f_words[26])
			Edges = int(f_words[28])
			contador = 0

			for v in range(1,Nodes+1) :
				g.add_vertex(v)

			for contador in range (0, Edges):
				g.add_edge(int(f_words[30 + 4*contador]),int(f_words[31 + 4*contador]),int(f_words[32 + 4*contador]))

			time_inicial = time.time() 
			timeout = time_inicial + 5   # 5 seconds from now
			execucoes = 0
			while True:
				if time.time() > timeout:
					break
				execucoes = execucoes + 1
				dijkstra_avl.dijkstra(g, g.get_vertex(1))
			tempo_medio = (time.time()-time_inicial)/execucoes
			print(execucoes)
			writer.writerow({'instancia': filename, 'nodes': Nodes, 'edges': Edges, 'tempo_execucao': tempo_medio})
		f.close()	

		



	



