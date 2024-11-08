import random

salir = False

inventario = []

while salir == False:
    def menu_principal():
        print("------------------")
        print(f" [ 1 ] Agregar un producto")
        print(f" [ 2 ] modificar un producto existente")
        print(f" [ 3 ] eliminar un producto")
        print(f" [ 4 ] mostrar el inventario completo")
        print(f" [ 5 ] Buscar un producto espefico")
        print(f" [ 6 ] salir")
        print("------------------")
    menu_principal()
    
    def recoletar_entrada(entrada):
        if entrada == 1:
            nombre = input("Ingresa el nombre del producto: ").lower()
            descripcion = input("Ingresa la descripcion del producto: ").lower()
            precio_ = float(input("ingresa el precio: "))
            
            producto = { "nombre" : nombre,
                        "descripcion" : descripcion,
                        "precio" : precio_,
                        "id_producto" : random.randint(1000,9999)}
            
            print(f"Producto realizado con exito, ID: {producto['id_producto']}")
            inventario.append(producto)
        
        elif opcion == 2:
            try:
                print(f"No se encuentra disponible actualmente!")
            except ValueError:
                print("Error")
        elif opcion == 4:
            num = 0
            print(f"Inventario completo")
            print('-----------------------')
            for i in range(len(inventario)):
                num = i
                print(f"{inventario[num]["nombre"]} : {inventario[num]["descripcion"]} ")
            print('-----------------------')
        
        
        
        elif opcion == 3:
            num = 0
            lista_productos_existentes = [] 
            print('-----------------------')
            for i in range(len(inventario)):
                    num = i
                    print(f" [ {num} ] {inventario[num]["nombre"]}")
                    lista_productos_existentes.append(num)
                    print(lista_productos_existentes)
            print('-----------------------')
            ask_arg = int(input("Ingresa el numero del producto a eliminar: "))  
            inventario.remove(inventario[ask_arg])
     
        elif opcion == 5:
            ask_name = input("Ingresa el nombre del producto a buscar: ")
            for producto in inventario:
                if ask_name in producto["nombre"]:
                    print("El producto se encuentra disponible!")
                else:
                    print("El producto no se encuentra disponible actualmente!")
        elif opcion == 6:
            preguntar = input("Realmente deseas salir Y/N: ").lower()
            if preguntar == "y":
                print("Has salido!")
                salir = True
                exit()
            elif preguntar == "n":
                pass
            else:
                pass
    opcion = int(input("Seleccione: "))
    recoletar_entrada(opcion)
    