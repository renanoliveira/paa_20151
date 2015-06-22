import sys
import time
import networkx as nx
import double_linked_list as dbl



def dijkstra(G, s):

    #Inicialização
    for node in G.nodes():
        G.node[node]['d'] = sys.maxsize
        G.node[node]['py'] = None
        G.node[node]['visited'] = False


    G.node[s]['d'] = 0
    
    S = [] #Guarda o caminho mais curto

    #Encontra aresta máxima
    max_weight = 0
    for edge in G.edges():
        if(G[edge[0], edge[1]]['weight'] > max_weight):
            max_weight = G[edge[0], edge[1]]['weight'] 

    #Inicializa vetor de buckets
    Q = [None] * (len(G.nodes())*max_weight)
    #Inicializa vertor de referência para saber em que bucket um vértice está
    V = [None] * G.nodes()

    #Coloca s no Bucket 0
    V[s] = 0
    
    u = s
    while u != None:
        G.node[u]['visited'] = True

        for v in G.neighbors(u):
            #Se ainda não foi marcado permanentemente ajusta distância no bucket correspondente
            if G.node[v]['visited'] = False:
                #Se já está em V, está em bucket, remove do bucket
                if not V[v] is None:
                    Q[G.node[v]['d']].remove(v)

                    #Se o bucket está vazio, remove bucket
                    if Q[G.node[v]['d']].head is None and Q[G.node[v]['d']].tail is None:
                        Q[G.node[v]['d']] = None
                
                #Calcula nova distância
                new_distance = G.node[u]['d'] + G.edge[u][v]['weight']
                
                #Se não existe bucket para nova distância, cria bucket
                if Q[new_distance] is None:
                    Q[new_distance] = dbl.DoubleLinkedList()

                #Aloca vértice no bucket correspondente a nova instância
                Q[new_distance].append(v)
                V[v] = new_distance

        #Seleciona novo vértice de distância mínima
        u = None

        for bucket in Q:
            if not bucket is None:
                u = bucket.remove_tail()
            break


    
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




