import sys
import time
import networkx as nx
import fibonacci_heap_mod as fb



def dijkstra(G, s):

    #Inicialização
    for node in G.nodes():
        G.node[node]['d'] = sys.maxsize
        G.node[node]['py'] = None
        G.node[node]['visited'] = False
        G.node[node]['heap_entry'] = False


    G.node[s]['d'] = 0
    
    S = [] #Guarda o caminho mais curto

    Q = fb.Fibonacci_heap()
    for node in G.nodes():
        G.node[node]['heap_entry'] = Q.enqueue(node,G.node[node]['d'])

    while Q.m_size != 0:
        fb_entry = Q.dequeue_min()
        u = fb_entry.m_elem
        G.node[u]['visited'] = True

        for v in G.neighbors(u):
            if G.node[v]['d'] > G.node[u]['d'] + G.edge[u][v]['weight']:
                new_distance = G.node[u]['d'] + G.edge[u][v]['weight']
                if(not G.node[v]['visited']):
                    Q.decrease_key(G.node[v]['heap_entry'], new_distance)
                G.node[v]['d'] = new_distance
                G.node[v]['py'] = u

    
if __name__ == '__main__':

    G = nx.DiGraph()

    f = open('instancias/avl/test1.stp','r+')


    for linha in f.readlines():

        started = False
        
        if "Section Graph" in linha:
            started = True

        if "End" in linha and started:
            break

        if linha.startswith("Nodes"):
            qtd_nodes = linha.split()[1]

        if linha.startswith("Edges"):
            qtd_edges = linha.split()[1]

        if linha.startswith("E "):
            item_data = linha.split()
            G.add_weighted_edges_from([(int(item_data[1]), int(item_data[2]), float(item_data[3]))])

    f.close()

    dijkstra(G, 1)


'''
    print("Grafo criado")
    nx.draw(G)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, alpha = 0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, alpha = 0.5)
    plt.show()

'''




