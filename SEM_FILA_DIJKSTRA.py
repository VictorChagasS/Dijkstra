import sys

import matplotlib.pyplot as plt
import networkx as nx


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.grau = 0
        self.distancia = sys.maxsize
        self.vizinhos = {}
        self.pai = None
        self.visitado = False

    def addVizinho(self,vertice,custo):
        self.vizinhos[vertice] = custo 

class Grafo:
    def __init__(self):
        self.vertices = []
        self.listaAdj = []

    def adicionar_vertice(self, rotulo):
        indice = len(self.vertices)
        vertice = Vertice(indice, rotulo)
        self.vertices.append(vertice)
        self.listaAdj.append([])

    def adicionar_aresta(self, v1, v2,peso):
  
        self.listaAdj[v1].append(v2)
        if (v1 != v2):
            self.listaAdj[v2].append(v1)
        self.vertices[v1].addVizinho(v2,peso)
        self.vertices[v2].addVizinho(v1,peso)
       
        

    def remover_aresta(self, v1, v2):
        if v2 in self.listaAdj[v1]:
            self.listaAdj[v1].remove(v1)
            self.listaAdj[v2].remove(v2)
            self.vertices[v1].grau -= 1
            self.vertices[v2].grau -= 1



    def haNaoVisitados(self):
        for vertice in self.vertices:
            if (vertice.visitado == False ):
               return True
           
        return False


    def minVertice(self):
        min = 9999999999
        verticeMin = None
        for vertice in self.vertices:
            if (vertice.distancia < min  and vertice.visitado == False):
                verticeMin = vertice
                min = vertice.distancia
        return verticeMin
    
    def dj(self,verticeInicial,verticeDestino):
       
        vertice =  self.vertices[verticeInicial]
        vertice.distancia = 0
      
        while (self.haNaoVisitados()):
      
            vertice.visitado = True

            for chave, valor in vertice.vizinhos.items():  
                if (self.vertices[chave].distancia > (valor + vertice.distancia) and self.vertices[chave].visitado == False ): 
                    self.vertices[chave].distancia = (valor + vertice.distancia)
                    self.vertices[chave].pai = vertice.indice
            vertice = self.minVertice()

      
        final = []
        for verticeMount in self.vertices:
            caminho = []
            if (verticeMount.indice == verticeDestino):
                analise = verticeMount.indice
                while analise != verticeInicial:

                    final.append(analise)
                    analise = self.vertices[analise].pai
                final.append(verticeInicial)

            analise = verticeMount.indice
            while analise != verticeInicial:
                caminho.append(analise)
                analise = self.vertices[analise].pai

            caminho.append(verticeInicial)
        
            print('\n',"ROTULO",verticeMount.rotulo, "CUSTO: ", verticeMount.distancia)
            for vert in reversed(caminho):
                print(self.vertices[vert].rotulo)
        
                


        class GraphVisualization:

            def __init__(self):
                self.visual = []

            def addEdge(self, a, b, weight):
                temp = [a, b, weight]
                self.visual.append(temp)

            def visualize(self):
                G = nx.Graph()
                for edge in self.visual:
                    G.add_edge(edge[0], edge[1], weight=edge[2])

                arestas = []
                for vertice in range(len(final)-1,0,-1):
                    arestas.append((final[vertice],final[vertice-1]))
                    arestas.append((final[vertice-1],final[vertice]))

                edge_colors = ['red' if edge in arestas else 'black' for edge in G.edges()]
                pos = nx.fruchterman_reingold_layout(G)

                nx.draw_networkx(G, pos, edge_color=edge_colors)
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        G = GraphVisualization()

        for i in range(len(self.listaAdj)):
            for j in self.listaAdj[i]:
                peso = self.vertices[i].vizinhos[j]
                G.addEdge(i, j, peso)

        G.visualize()
        plt.show()
      
   


    def imprimir_grafo(self): 
        n_vertices = len(self.vertices)
        n_arestas = sum(v.grau for v in self.vertices) // 2
        
        print(f"Vértices: {n_vertices}")
        print(f"Arestas: {n_arestas}")
        
        for i in range(n_vertices):
            for j in self.listaAdj[i]:
                if (i < j or i == j):
                    print(f"({i}, {j})")
                
        print(self.listaAdj)
      
        print("Graus dos vértices:")
        for v in self.vertices:
         
            print(v.distancia, v.pai)
        print("\n\n")
                

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

grafo1 = Grafo()

# Adicionando vértices
vertices = ["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"]
for vertice in vertices:
    grafo1.adicionar_vertice(vertice)

# Matriz de adjacência
graph =  [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

# Adicionando arestas
for i in range(len(graph)):
    for j in range(i+1,len(graph[i])):
        if graph[i][j] != 0:
            grafo1.adicionar_aresta(i,j, graph[i][j])

grafo1.dj(1,5)

