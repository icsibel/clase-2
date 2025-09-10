class PaginaWeb:
    def __init__(self,url, titulo, fechaAcceso):
        self.url= url
        self.titulo=titulo
        self.fechaAcceso=fechaAcceso


class Navegador:
    def __init__(self):
        self.pila=[]
    
    def push(self,pagina):
        self.pila.append(pagina)
    
    def vacia(self):
        v= len(self.pila) ==0
        return v
            
    
    def pop(self):
        if self.vacia():
            return None
        return self.pila.pop()

    
    def peek(self):
        if self.vacia():
            return None
        u= self.pila[-1]
        return u
    
    def visitar_pagina(self, url, titulo, fechaAcceso):
        pagina= PaginaWeb(url, titulo, fechaAcceso)
        self.push(pagina)
        print(f"pagina: {pagina.titulo} \n fecha de acceso: {pagina.fechaAcceso} \n url: {pagina.url} ")
    
    def retroceso(self):
        if self.vacia():
            print("la lista esta vacia")
            return 
        
        pagina_anterior= self.pop()
        print(pagina_anterior.titulo , pagina_anterior.url)
        pagina_actual=self.peek()
        if pagina_actual is None:
            print ("no hay historial")
        else: 
            print(pagina_actual.titulo , pagina_actual.url)
    
    def ver_historial(self):
        if self.vacia():
            print("no hay historial")
            return
        print("HISTORIAL")
        for x in self.pila:
            print(" ")
            print (x.titulo, x.fechaAcceso , x.url)







        

        

    