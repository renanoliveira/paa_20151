import sys
import time


class Vertex:
	# inicializa um vertice - O(1)
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Define dintancia infitinita para todos os nós
        self.distance = sys.maxsize #800 #sys.maxint
        # Coloca não visitado para para todos os nós       
        self.visited = False  
        # Definie que todo o Predecessor é nulo
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

	# Pega os vértices adjacentes ao nó self
    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id
		
	# Pega a disntacia/custo da aresta entre o vértice self e o neighbor
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

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
	# o(1)
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
	
    def __iter__(self):
        return iter(self.vert_dict.values())

	# o(1)
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

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

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    #''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start, target):
    #print("Dijkstra's shortest path")
    # Define como zero a distancia para o ponto inicial
    start.set_distance(0)

    # Inicializa a pripority queu
    unvisited_queue = []
    #unvisited_queue.array([(v.get_distance(),v) for v in aGraph])
    #for v in aGraph: #O(v)
    unvisited_queue = [v for v in aGraph]
    #unvisite_queue = [(v.get_distance(),v) for v in aGraph]

#    unvisited_queue = []
#    for v in aGraph:
#        heapq.heappush(unvisited_queue,(v,v.get_distance()))
    #heapq.heapify(unvisited_queue)

    while len(unvisited_queue): #Este loop será feito uma vez para cada vértice do Grafo - O(n)
        # Pega o vertice com a menor distancia da priority queu
		# Pops a vertex with the smallest distance 
        # O(n) - percorre o vetor unvisited_queue inteiro por lista - O(n) no pior caso

        #print("elementos na queue: %i" %len(unvisited_queue))
        #uv = heapq.heappop(unvisited_queue)
        distancia_minima = sys.maxsize
        uv = []
        for element in unvisited_queue:
            distancia_atual = element.get_distance()
            if distancia_atual  < distancia_minima:
                distancia_minima = distancia_atual
                uv = element

        if uv == []:
            break
        current = uv
        current.set_visited()

        #Para todo vértice na lista de adjacencia do vertice atual: - 
        for next in current.adjacent: # este for leva no máximo 
            # Pula caso já tenha sido visitado
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                #print("updated : current = %s next = %s new_dist = %s"
                #        %(current.get_id(), next.get_id(), next.get_distance()))
            #else:
                #print("not updated : current = %s next = %s new_dist = %s"
                #        %(current.get_id(), next.get_id(), next.get_distance()))

        # Refaz a heap
       # while len(unvisited_queue):
           # heapq.heappop(unvisited_queue)
        index = unvisited_queue.index(uv)
        unvisited_queue.pop(index)
        #print(len(unvisited_queue))

        # 2. Put all vertices not visited into the queue
        #unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        #heapq.heapify(unvisited_queue)
    
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

        f = open('instancias/array/dmxa0903.stp','r+')
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

        #print("Graph data:")
        #for v in g:
        #    print("vertice: %s" %v)
        #    for w in v.get_connections():
        #        vid = v.get_id()
        #        wid = w.get_id()
        #        print("( %s , %s, %3d)"  % ( vid, wid, v.get_weight(w)))

        print("Edges: %d" %Edges)
        print("Nodes :%d" %Nodes)

        dijkstra(g, g.get_vertex(1), g.get_vertex(Nodes)) 

        target = g.get_vertex(Nodes)
        #path = [target.get_id()]
        #shortest(target, path)
        #print("The shortest path : %s" %(path[::-1]))
        #print("Distancia total: %i" %target.get_distance())
    print("total de rodadas: %d" %test)
    tempo_medio = (time.time()-time_inicial)/test
    #print("tempo médio: %.2f" %tempo_medio)
    print("tempo medio: %.2f" %tempo_medio)