from collections import deque 

class PerritoCaliente:
    def __init__(self, tamano, cliente, tipo, precio):
        self.tamano=tamano
        self.cliente=cliente
        self.tipo=tipo 
        self.precio=precio

class Venta:
    def __init__(self):
        self.cola= deque()

    def push(self, producto):
        self.cola.append(producto)
    
    def vacia(self):
        v= len(self.cola) ==0
        return v
    
    def remove(self):
        if self.vacia:
            return None
        self.cola.popleft()
    
    def peek(self):
        if self.vacia():
            return None
        u= self.cola[0]
        return u
    
    def mostrar_colita(self):
        if self.vacia():
            print("no hay pedidos")
            return
        print("HISTORIAL")
        for x in self.cola:
            print(" ")
            print (f" cliente: {x.cliente}, tipo de comida: {x.tipo}, precio: {x.precio} , tamaño de producto: {x.tamano}")

    def agregar_perrito(self):
        while True:
            print("\n=== Restaurante el perrito caliente ===")
            print("1) agregar pedido")
            print("2) eliminar pedido primer pedido")
            print("3) Ver pedidos)")
            print("4) Ver pedido actual")
            print("5) Salir")
            opcion=input("seleccione la opcion que desea realizar: ")

            match opcion:
                case "1":
                    cliente=input("ingrese nombre del cliente: ")
                    tipo =input("ingrese tipo de comida: ")
                    precio=input("ingrese pecio del producto: ")
                    tamano=input("ingrese tamaño ")
                    perrito=PerritoCaliente(tamano, cliente, tipo, precio)
                    self.push(perrito)
                    print("pedido ingresado ")
                    
                case "2":
                    self.remove()
                    print("pedido liberado ")
                case "3":
                    self.mostrar_colita()
                case "4":
                    pedido_actual= self.peek()
                    print (f" cliente: {pedido_actual.cliente}, tipo de comida: {pedido_actual.tipo}, precio: {pedido_actual.precio} , tamaño de producto: {pedido_actual.tamano}")
                case "5":
                    print("saliendo...")
                    break
                case _:
                    print("opcion invalida")

venta=Venta()
venta.agregar_perrito()

#menu de tamaños y de tipos
#revisar or que no elimina la cola 



      