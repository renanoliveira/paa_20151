import sys
import time

import DoubleLinkedList


class Vertex:
	# inicializa um vertice - O(1)
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Define dintancia infitinita para todos os nós
        self.distance = sys.maxsize
        # Coloca não visitado para para todos os nós       
        self.visited = False  
        # Definie que todo o Predecessor é nulo
        self.previous = None
        # Define em qual entrada está na priority queue
        self.queue_element = None

    def set_queue_element(self, queue_element):
        self.queue_element = queue_element

    def get_queue_element(self):
        return self.queue_element

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

	# Pega os vértices adjacentes ao nó self
    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id
		
	# Pega a distancia/custo da aresta entre o vértice self e o neighbor
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

	# Pega a disntacia atual (relaxada ou final) do vértice self
    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
	# o(1)
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.max_distance = 0
	
    def __iter__(self):
        return iter(self.vert_dict.values())

	# o(1)
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_num_vertices(self):
        return self.num_vertices

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost) # Comentar caso o grafo seja direcionado

        if self.max_distance < cost:
            self.max_distance = cost

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def get_max_distance(self):
        return self.max_distance

def shortest(v, path):
    #''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start):
    print("Dijkstra's shortest path")
    # Define como zero a distancia para o ponto inicial
    start.set_distance(0)


    unvisited_queue = []
    # Inicializa a pripority queu
    unvisited_queue = [DoubleLinkedList.DoubleLinkedList() for i in range(0,g.get_max_distance()*g.get_num_vertices()+2)]

    for v in aGraph:
        if v != start:
            v.set_queue_element(unvisited_queue[g.get_max_distance()*g.get_num_vertices()+1].append(v))
        else:
            v.set_queue_element(unvisited_queue[0].append(v))
    for i in range(0,13*g.get_num_vertices()+1): 
        while unvisited_queue[i].head != None: #Este loop será feito uma vez para cada vértice do Grafo - O(n)
            # Pega o vertice com a menor distancia da priority queu
		    # Pops a vertex with the smallest distance 
            # O(n) - percorre o vetor unvisited_queue inteiro por lista - O(n) no pior caso

            #print("elementos na queue: %i" %len(unvisited_queue))
            uv = []
            node = []
            node = unvisited_queue[i].remove_tail()
            if node == None:
                break
            uv = node.data
            if uv == None:
                break
            current = uv
            current.set_visited()

            modify = False
            #Para todo vértice na lista de adjacencia do vertice atual: - 
            for next in current.adjacent: # este for leva no máximo 
                # Pula caso já tenha sido visitado
                if next.visited:
                    continue
                new_dist = current.get_distance() + current.get_weight(next)
            
                if new_dist < next.get_distance(): 
                    if next.get_distance() != sys.maxsize:
                        unvisited_queue[next.get_distance()].remove(next)
                    else:
                        unvisited_queue[g.get_max_distance()*g.get_num_vertices()+1].remove(next)
                    next.set_queue_element(unvisited_queue[new_dist].append(next)) 
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    modify = True
  

    
if __name__ == '__main__':

    time_inicial = time.time() 
    timeout = time_inicial + 5   # 5 seconds from now
    test = 0
    while True:
        if time.time() > timeout:
            break
        test = test + 1
        print(test)

        g = Graph()

        f = open('C:\\Users\\TA\\Desktop\\ALUE\\ALUE\\alue7229.stp','r+')
        #print(f.read())
        f_words = f.read()
        f_words = f_words.split()
        f.close()
        Nodes = int(f_words[26])
        Edges = int(f_words[28])

        for v in range(1,Nodes+1) :
            g.add_vertex(v)

        for index in range(0, Edges):
            g.add_edge(int(f_words[30 + 4*index]),int(f_words[31 + 4*index]),int(f_words[32 + 4*index]))

        #print("Graph data:")
        #for v in g:
        #    print("vertice: %s" %v)
        #    for w in v.get_connections():
        #        vid = v.get_id()
        #        wid = w.get_id()
        #        print("( %s , %s, %3d)"  % ( vid, wid, v.get_weight(w)))

        print("Edges: %d" %Edges)
        print("Nodes :%d" %Nodes)

        dijkstra(g, g.get_vertex(1)) 

        # Retorna menor caminho entre source (g.get_vertex(1)) e target
        target = g.get_vertex(Nodes)
        path = [target.get_id()]
        shortest(target, path)
        print("The shortest path : %s" %(path[::-1]))
        print("Distancia total: %i" %target.get_distance())

    print("total de rodadas: %d" %test)
    tempo_medio = (time.time()-time_inicial)/test
    #print("tempo médio: %.2f" %tempo_medio)
    print("tempo medio: %.2f" %tempo_medio)