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
        if self.vacia():
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
            print("")

    def agregar_perrito(self):
        while True:
            print("\n=== Restaurante el perrito caliente ===")
            print("1) agregar pedido")
            print("2) eliminar pedido primer pedido")
            print("3) Ver pedidos")
            print("4) Ver pedido actual")
            print("5) Salir")
            opcion=input("seleccione la opcion que desea realizar: ")

            match opcion:
                case "1":
                    print("")
                    cliente=input("ingrese nombre del cliente: ")

                    tipo = input("ingrese el tipo de comida: \n 1.hamburguesita \n 2.perro \n 3.papas \n")
                    match tipo:
                        case "1":
                            tipo= "hamburgesita"
                        case "2":
                            tipo="perro"
                        case "3":
                            tipo="papas"
                        case _:
                            print("no hay ese tipo de comida")
                    
                    print("")
                    tamano=input("ingrese tamaño \n 1.grande \n 2.mediano \n 3.pequeño \n")
                    match tamano:
                        case "1":
                            tamano= "grande"
                        case "2":
                            tamano="mediano"
                        case "3":
                            tamano="pequeño"
                        case _:
                            print("tamaño invalido")

                    precio = 0
                    if tipo == "hamburgesita":
                        if tamano == "grande":
                            precio = 20000
                        elif tamano == "mediano":
                            precio = 13000
                        elif tamano == "pequeño":
                            precio = 10000

                    elif tipo == "perro":
                        if tamano == "grande":
                            precio = 15000
                        elif tamano == "mediano":
                            precio = 10000
                        elif tamano == "pequeño":
                            precio = 7000

                    elif tipo == "papas":
                        if tamano == "grande":
                            precio = 18000
                        elif tamano == "mediano":
                            precio = 10000
                        elif tamano == "pequeño":
                            precio = 7000
                    


                    perrito=PerritoCaliente(tamano, cliente, tipo, precio)
                    self.push(perrito)
                    print("pedido ingresado ")
                    
                case "2":
                    self.remove()
                    print("")
                    print("pedido liberado ")
                case "3":
                    self.mostrar_colita()
                case "4":
                    pedido_actual= self.peek()
                    if pedido_actual is None:
                        print("no hay pedidos")
                        print("")
                    else:
                        print("")
                        print (f" cliente: {pedido_actual.cliente}, tipo de comida: {pedido_actual.tipo}, precio: {pedido_actual.precio} , tamaño de producto: {pedido_actual.tamano}")
                case "5":
                    print("")
                    print("saliendo...")
                    break
                case _:
                    print("opcion invalida")

venta=Venta()
venta.agregar_perrito()


      