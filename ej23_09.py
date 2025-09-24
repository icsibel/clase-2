from collections import deque
class Articulo:
    def __init__(self, idArticulos, nombre, precio):
        self.idArticulos= idArticulos
        self.nombre= nombre
        self.precio=precio
    
class Colita:
    def __init__(self):
        self.cola= deque()
    
    def push(self, articulo):
        self.cola.append(articulo)
    
    def vacia(self):
        v= len(self.cola) ==0
        return v
    
    def remove(self):
        if self.vacia():
            return None
        self.cola.popleft()
    
    def peek(self):
        if self.vacia():
            return None
        u= self.cola[0]
        return u
    
    #parctica con archivos, buscar 