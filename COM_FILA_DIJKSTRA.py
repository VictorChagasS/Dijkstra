import heapq
import math

import matplotlib.pyplot as plt
import networkx as nx


class Voo:
    def __init__(self, partida, chegada):
        self.partida = partida
        self.chegada = chegada

class Vertice:
    def __init__(self, indice,rotulo,coordenada):
        self.indice = indice
        self.rotulo = rotulo
        self.tempo = float('inf')
        self.vizinhos = {}
        self.pai = None
        self.coordenadas=coordenada

    def addVizinho(self, vertice, custo):
        self.vizinhos[vertice] = custo 

class Grafo:
    def __init__(self):
        self.vertices = []
        self.listaAdj = []

    def caminho_minimo(self, v):
        caminho = []
        atual = v
        while atual is not None:
            caminho.append(atual)
            atual = self.vertices[atual].pai
        return caminho[::-1] 
    
    def adicionar_vertice(self,rotulo,coordenada):
        indice = len(self.vertices)
        vertice = Vertice(indice,rotulo,coordenada)
        self.vertices.append(vertice)
        self.listaAdj.append([])

    def adicionar_aresta(self, v1, v2, custo):
        self.listaAdj[v1].append(v2)
        if (v1 != v2):
            self.listaAdj[v2].append(v1)
        self.vertices[v1].addVizinho(v2, custo)
        self.vertices[v2].addVizinho(v1, custo)

    def calcular_distancia(self,ponto1, ponto2):
        x1, y1 = ponto1
        x2, y2 = ponto2
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia   
    
    def dijkstra(self, vertice_inicial, vertice_destino):
        self.vertices[vertice_inicial].tempo = 0
        fila_prioridade = [(0, vertice_inicial)]
        while fila_prioridade:
            tempo_atual, vertice_atual = heapq.heappop(fila_prioridade)
            if tempo_atual != self.vertices[vertice_atual].tempo:
                continue
            for vertice_adjacente, voo in self.vertices[vertice_atual].vizinhos.items():
                if voo.partida >= self.vertices[vertice_atual].tempo:
                    tempo_chegada = voo.chegada
                    if tempo_chegada < self.vertices[vertice_adjacente].tempo:
                        self.vertices[vertice_adjacente].tempo = tempo_chegada
                        self.vertices[vertice_adjacente].pai = vertice_atual
                        heapq.heappush(fila_prioridade, (tempo_chegada, vertice_adjacente))
        
        for v in self.vertices:
            distancia = 0
            if (vertice_destino == v.indice):
                caminhoVertice = self.caminho_minimo(v.indice)
                distanciaDada = 0
                for k in range(len(caminhoVertice)-1):
                    distanciaDada+=self.calcular_distancia(self.vertices[caminhoVertice[k]].coordenadas,self.vertices[caminhoVertice[k+1]].coordenadas)
            
            caminho = self.caminho_minimo(v.indice)
            caminho_rotulos = [self.vertices[i].rotulo for i in caminho]
            print(f"TEMPO: {v.tempo}, Rótulo:{v.rotulo} : {' -> '.join(map(str, caminho_rotulos))}")
            for k in range(len(caminho)-1):
                distancia+=self.calcular_distancia(self.vertices[caminho[k]].coordenadas,self.vertices[caminho[k+1]].coordenadas)
            print(f"Menor distancia: {distancia}")

        
        class GraphVisualization:
            def __init__(self,posicoes):
                self.visual = []
                self.posicoes = posicoes

            def addEdge(self, a, b, weight):
                temp = [a, b, weight]
                self.visual.append(temp)

            def visualize(self):
                G = nx.Graph()
                edge_labels = {}
                for edge in self.visual:
                    G.add_edge(edge[0], edge[1])
                    edge_labels[(edge[0], edge[1])] = edge[2]

                arestas = []
              
               
                for vertice in range(len(caminhoVertice)-1):
                    
                    arestas.append((caminhoVertice[vertice],caminhoVertice[vertice+1]))
                    arestas.append((caminhoVertice[vertice+1],caminhoVertice[vertice]))
                
              
                edge_colors = ['red' if edge in arestas else 'black' for edge in G.edges()]
             
                pos = self.posicoes
                
                fig, ax = plt.subplots()



                nx.draw_networkx(G, pos, edge_color=edge_colors)
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size=6)
                plt.grid(True)
        
                ax.set_xlim([0,100])
                ax.set_ylim([0,100])
                ax.set_xticks(range(0, 100, 20))
                ax.set_yticks(range(0,100, 20))
                ax.xaxis.set_tick_params(which='both', bottom=True, top=False, labelbottom=True)
                ax.yaxis.set_tick_params(which='both', left=True, right=False, labelleft=True)
                plt.title(f'Menor distância: {round(distanciaDada, 2)}')

             
        pos = {vertice.indice: (vertice.coordenadas) for vertice in self.vertices}
        G = GraphVisualization(pos)
        

        for i in range(len(self.listaAdj)):
            for j in self.listaAdj[i]:
                G.addEdge(i, j, f"(P:{self.vertices[i].vizinhos[j].partida},C:{self.vertices[i].vizinhos[j].chegada})")

        G.visualize()
        
        plt.show()

                

# grafo2 = Grafo()
# grafo2.adicionar_vertice('v1',(27,86))
# grafo2.adicionar_vertice('v2',(55,95))
# voo1 = Voo(0,2)
# grafo2.adicionar_aresta(0,1,voo1)
# grafo2.dijkstra(0,1)
grafo1 = Grafo()
grafo1.adicionar_vertice('v0',(2,38))
grafo1.adicionar_vertice('v1',(20,55))
grafo1.adicionar_vertice('v2',(36,50))
grafo1.adicionar_vertice('v3',(18,35))
# grafo1.adicionar_vertice('v4',(30,80))
# grafo1.adicionar_vertice('v5',(46,50))
# grafo1.adicionar_vertice('v6',(50,40))
# grafo1.adicionar_vertice('v7',(60,60))
# grafo1.adicionar_vertice('v8',(80,10))

v1 = Voo(0,3)
v2 = Voo(7,9)
v3 = Voo(7,8)
v4 = Voo(10,12)
v5 = Voo(10,11)
v6 = Voo(18,19)
v7 = Voo(17,18)
v8 = Voo(21,23)
v9 = Voo(2,4)
v10 = Voo(3,4)
v11 = Voo(1,5)
v12 = Voo(1,2)
v13 = Voo(21,22)
v14 = Voo(5,6)

grafo1.adicionar_aresta(0,1,v1)
grafo1.adicionar_aresta(0,2,v2)
grafo1.adicionar_aresta(1,2,v3)
grafo1.adicionar_aresta(2,3,v13)

grafo1.dijkstra(0,3)

# grafo1 = Grafo()
# grafo1.adicionar_vertice('v1')
# grafo1.adicionar_vertice('v2')
# grafo1.adicionar_vertice('v3')
# grafo1.adicionar_vertice('v4')
# grafo1.adicionar_vertice('v5')
# grafo1.adicionar_aresta(0,1,4)
# grafo1.adicionar_aresta(0,2,3)
# grafo1.adicionar_aresta(1,2,5)
# grafo1.adicionar_aresta(1,3,2)
# grafo1.adicionar_aresta(2,3,1)
# grafo1.adicionar_aresta(2,4,3)
# grafo1.adicionar_aresta(3,4,4)

# # Executa o algoritmo de Dijkstra
# grafo1.dijkstra(0)

