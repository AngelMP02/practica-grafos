class Grafo:
    def __init__(self):
        self.ciudades = {}
        self.matriz_adyacencia = {}

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.ciudades:
            self.ciudades[ciudad] = len(self.ciudades)
            self.matriz_adyacencia[len(self.ciudades) - 1] = {}

    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        if ciudad1 in self.ciudades and ciudad2 in self.ciudades:
            idx1, idx2 = self.ciudades[ciudad1], self.ciudades[ciudad2]
            self.matriz_adyacencia[idx1][idx2] = distancia
            self.matriz_adyacencia[idx2][idx1] = distancia

    def mostrar_grafo(self):
        for ciudad, idx in self.ciudades.items():
            print(f"{ciudad}: {self.matriz_adyacencia[idx]}")

    def ruta_mas_corta(self, origen, destino):
        pass  # Implementar algoritmo de búsqueda de la ruta más corta

    def agregar_distancia_bst(self, distancia, ciudad1, ciudad2):
        pass  # Implementar inserción en el árbol binario de búsqueda

    def mostrar_registro_ordenado(self):
        pass  # Implementar recorrido inorden del árbol binario de búsqueda

    def arbol_recubrimiento_minimo(self):
        pass  # Implementar algoritmo de árbol de recubrimiento mínimo (Prim o Kruskal)


# Ejemplo de uso
grafo = Grafo()
grafo.agregar_ciudad("A")
grafo.agregar_ciudad("B")
grafo.agregar_ciudad("C")
grafo.agregar_ciudad("D")

grafo.agregar_conexion("A", "B", 2)
grafo.agregar_conexion("B", "C", 4)
grafo.agregar_conexion("C", "D", 1)
grafo.agregar_conexion("A", "D", 3)

grafo.mostrar_grafo()
