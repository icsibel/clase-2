from ej09_09 import Navegador

navegador=Navegador()

while True:
    print("\n=== NAVEGADOR WEB (Pilas LIFO) ===")
    print("1) Visitar nueva página (push)")
    print("2) Retroceder (pop)")
    print("3) Ver historial (recorrido)")
    print("4) Ver página actual (peek)")
    print("5) Salir")
    opcion=input("seleccione la opcion que desea realizar: ")

    match opcion:
        case "1":
            url=input("ingrese url: ")
            titulo=input("ingrese titulo: ")
            fechaAcceso=input("ingrese la fecha de ingreso: ")
            navegador.visitar_pagina(url, titulo, fechaAcceso)
        case "2":
            navegador.retroceso()
        case "3":
            navegador.ver_historial()
        case "4":
            pagina_actual=navegador.peek()
            if pagina_actual is None:
                print ("no hay historial")
            else: 
                print(pagina_actual.titulo , pagina_actual.url)
        case "5":
            print("saliendo...")
            break
        case _:
            print("opcion invalida")
    

