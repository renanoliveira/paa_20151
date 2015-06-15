import sys
import time
import networkx as nx
import matplotlib.pyplot as plt


def extract_min(G, Q):
    if len(Q) == 0:
        return None

    d = sys.maxsize
    u = None
    for node in Q:
        if G.node[node]['d'] < d:
            u = node
            d = G.node[node]['d']
    if u == None:
        u = Q[0]
    Q.remove(u)
    return u


def dijkstra(G, s):

    #Inicialização
    for node in G.nodes():
        G.node[node]['d'] = sys.maxsize
        G.node[node]['py'] = None

    G.node[s]['d'] = 0
    
    S = [] #Guarda o caminho mais curto

    Q = G.nodes()

    while len(Q) != 0:
        u = extract_min(G, Q)
        print(u)
        S.append(u)

        for v in G.neighbors(u):
            if G.node[v]['d'] > G.node[u]['d'] + G.edge[u][v]['weight']:
                G.node[v]['d'] = G.node[u]['d'] + G.edge[u][v]['weight']
                G.node[v]['py'] = u
    return S
    
if __name__ == '__main__':

    G = nx.DiGraph()

    f = open('instancias/array/dmxa0903.stp','r+')


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




