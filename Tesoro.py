"""
Descripción de problema:

Eres un intrépido buscador de tesoros en busca de una legendaria reliquia perdida en lo profundo de una antigua selva. 
Tienes un mapa rudimentario que indica una serie de puntos de referencia en la selva, pero no está claro cómo están conectados. 
Debes utilizar tu experiencia en programación y habilidades de resolución de problemas para crear un algoritmo que genere un 
árbol de búsqueda y encuentre el camino más corto hacia el tesoro perdido.
"""

class Mapa:
    """
    La clase Mapa se crea con el fin de facilitar la manipulacion del arbol usado para representar la zona de busqueda.
    """
    
    def __init__(self, n):
        self.n = n
        self.m = []

def CrearMapa(Caminos):
    """
    Se agregan las zonas por recorrer en nuestro mapa.
    """
    
    Zonas = {}  #Diccionario vacio donde se almacenan las zonas del mapa.
    
    for x, y in Caminos:
        if x not in Zonas:
            Zonas[x] = Mapa(x)
        if y not in Zonas:
            Zonas[y] = Mapa(y)
        Zonas[x].m.append(Zonas[y])
    
    return Zonas

def BusquedaTesoro(raiz, tesoro):
    """
    Se recorren las distintas zonas en busca del tesoro y va imprimiendo un registro de las zonas exploradas.
    """
    
    Lista = [(raiz, [])]  #Lista donde se almacenan las zonas.
    
    while Lista:
        ZonaActual, CaminoActual = Lista.pop(0)  #Elimina el registro y comienza desde el principio, solo si, no encuentra el tesoro.
        CaminoActual = CaminoActual + [ZonaActual.n]  #Se van agregando las zonas exploradas a medida del avance.
        print("\fExplorando la zona:", [ZonaActual.n], "\fCamino actual:", [CaminoActual])
        
        #El recorrido finaliza si se encuentra el tesoro en la zona actual.
        if ZonaActual.n == tesoro:
            return CaminoActual
        
        #Se aniaden las zonas exploradas a la lista de almacenamiento.
        Lista.extend((ms, CaminoActual) for ms in ZonaActual.m)
    
    return None

"""
Mapa del tesoro:

1
|          |-->6
|-->2-->5--|
|          |-->7-->[12]
|              |    ^
|       v------|    |
|-->3-->8           |
|       |           |
|       |--v        |
|      |-->9-->11---|
|-->4--|
       |-->10

Teniendo el mapa representado se crean las conexiones de estos con la variable "Caminos", la cual funciona como mapa en codigo.

Se declara el punto de partida en 1 (Puede ser elegido cualquier otra zona).

Se declara que el tesoro perdido se encuentra en el punto 12 (Puede ser elegido cualquier otra zona).
"""
Caminos = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 8), (4, 9), (4, 10), (5, 6), (5, 7), (8, 9), (9, 11), (7, 8), (7, 12), (11, 12)]
Inicio = 1
Tesoro = 12

mapa = CrearMapa(Caminos)  #Crea el mapa teniendo en cuenta las conexiones entre las zonas.
CaminoCorrecto = BusquedaTesoro(mapa[Inicio], Tesoro)  #Genera el camino mas corto en busca del tesoro.

print("\fBusqueda del tesoro:")
print("\fCamino más corto al tesoro:\f", " -> ".join(map(str, CaminoCorrecto)))  #Junta las cadenas de caracteres de la lista de caminos.
