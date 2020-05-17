import sqlite3
from database import *

# Se accede a la base de datos
db1 = database("base_de_prueba.db")

if db1.init()!=-1:
    print("Se ha accedido correctamente a la base de datos.")
    # Bucle del gestor
    while True:
        print('''
        #############################################################
                        GESTOR DE LA BASE DE DATOS
        #############################################################

        1.- Añadir categoria
        2.- Añadir planta
        3.- Obtener informacion de todas las plantas
        4.- Obtener informacion de una planta
        5.- Obtener categorias disponibles
        6.- Obtener informacion de una categoria
        7.- Obtener plantas pertenecientes a una categoria
        8.- Buscar una planta mediante sus caracteristicas en la db
        9.- Borrar una planta
        10.- Borrar una categoria
        11.- Actualizar una planta
        12.- Salir del gestor
        ''')

        elect=0
        while elect<1 or elect>12:
            elect = int(input(">>>  "))

        if elect==1:
            info = input(">>> Introducir el nombre de la nueva categoria:  ")
            db1.add_categoria(info)
        elif elect==2:
            cat = input(">>> Introducir la categoria de la nueva planta:  ")
            pos_x = float(input(">>> Introducir la posicion_x de la nueva planta:  "))
            pos_y = float(input(">>> Introducir la posicion_y de la nueva planta:  "))
            area = float(input(">>> Introducir el area (tamaño) de la nueva planta:  "))
            color = float(input(">>> Introducir el color (medio) de la nueva planta:  "))
            db1.add_planta(cat,pos_x,pos_y,area,color)
        elif elect==3:
            info = db1.getall_plant()
            for inf in info:
                print(inf)
        elif elect==4:
            id = input(">>> Introducir el id de una planta dentro de la base de datos:  ")
            info = db1.get_plant(id)
            print(info)
        elif elect==5:
            info = db1.getall_category()
            for inf in info:
                print(inf)
        elif elect==6:
            id = input(">>> Introducir el id de una categoria dentro de la base de datos:  ")
            info = db1.get_category(id)
            print(info)
        elif elect==7:
            cat = input(">>> Introducir el nombre de una categoria existente:  ")
            info = db1.get_plantbycategory(cat)
            print(info)
        elif elect==8:
            try:
                pos_x = float(input(">>> Introducir la posicion_x de la planta:  "))
            except:
                pos_x = None

            try:
                pos_y = float(input(">>> Introducir la posicion_y de la planta:  "))
            except:
                pos_y = None

            try:
                area = float(input(">>> Introducir el area de la planta:  "))
            except:
                area = None

            try:
                color = float(input(">>> Introducir el color de la planta:  "))
            except:
                color = None
            info = db1.get_plantbyspecs(pos_x, pos_y, area, color)
            print(info)
        elif elect==9:
            id = input(">>> Introducir el id de una planta dentro de la base de datos:  ")
            db1.delete_plant(id)
        elif elect==10:
            id = input(">>> Introducir el id de una categoria dentro de la base de datos:  ")
            db1.delete_category(id)
        elif elect==11:
            id = input(">>> Introducir el id de una planta dentro de la base de datos:  ")
            try:
                pos_x = float(input(">>> Introducir la posicion_x de la planta:  "))
            except:
                pos_x = None

            try:
                pos_y = float(input(">>> Introducir la posicion_y de la planta:  "))
            except:
                pos_y = None

            try:
                area = float(input(">>> Introducir el area de la planta:  "))
            except:
                area = None

            try:
                color = float(input(">>> Introducir el color de la planta:  "))
            except:
                color = None

            db1.update_plant(id,pos_x,pos_y,area,color)
        elif elect==12:
            break

    print("\nSe ha salido del gestor de la base de datos.")

else:
    print("\nError al acceder a la base de datos.")
