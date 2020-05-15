import sqlite3

class database:
    def __init__(self, name):
        self.name = name
        self.connection = 0
        self.cursor = 0

    def init(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se crea la tabla categoria en caso de que no exista
        try:
            self.connection.execute('''
                CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(50) UNIQUE NOT NULL
                )
            ''')
        except sqlite3.OperationalError:
            print("Se ha accedido correctamente")
        else:
            print("Error desconocido")
            return -1

        # Se crea la tabla plantas en caso de que no exista
        try:
            self.connection.execute('''
                CREATE TABLE plantas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    categoria_id INTEGER NOT NULL,
                    posicion_x REAL,
                    posicion_y REAL,
                    DensidadFoliar REAL,
                    PetalosRadian REAL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id)
                )
            ''')
        except sqlite3.OperationalError:
            print("Se ha accedido correctamente")
        else:
            print("Error desconocido")
            self.connection.close()
            return -1

        # Se cierra la conexión
        self.connection.close()
        return 1

    def add_categoria(self, categoria):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se intenta agregar una categoria
        try:
            self.cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categoria))
        except sqlite3.IntegrityError:
            print("La categoria {} ya existe.".format(categoria))

        self.connection.commit()
        self.connection.close()
        return 1

    def add_planta(self, categoria, posicion_x=0, posicion_y=0, DensidadFoliar=0, PetalosRadian=0):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        val=False

        categorias = self.cursor.execute("SELECT * FROM categoria").fetchall()
        for cat in categorias:
            if categoria==cat[1]:
                val = True
                cat_id = cat[0]
                break

        if val==True:
            # Se agrega una planta
            try:
                self.cursor.execute("""
                INSERT INTO plantas VALUES (null,{},{},{},{},{})
                """.format(cat_id,posicion_x,posicion_y,DensidadFoliar,PetalosRadian))
            except sqlite3.IntegrityError:
                print("No se puede agregar esta planta a la base de datos.")
        else:
            print("La categoria no existe, no se ha introducido en la base de datos.")
            self.connection.commit()
            self.connection.close()
            return -1

        self.connection.commit()
        self.connection.close()
        return 1

    def getall_plant(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se devuelven todas las plantas recogidas en la bd
        try:
            self.cursor.execute("SELECT * FROM plantas")
            info=self.cursor.fetchall()
        except sqlite3.IntegrityError:
            print("No se pudo consultar la tabla")
            self.connection.close()
            return -1

        self.connection.close()
        return info

    def get_plant(self, id):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se devuelve una planta mediante su identificador
        try:
            self.cursor.execute('''
                SELECT * FROM plantas
                WHERE id = {}
                '''.format(id))
            info = self.cursor.fetchone()
        except sqlite3.IntegrityError:
            print("No se pudo consultar la tabla")
            self.connection.close()
            return -1

        self.connection.close()
        return info

    def getall_category(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se devuelven las categorias existentes
        try:
            self.cursor.execute("SELECT * FROM categoria")
            info = self.cursor.fetchall()
        except sqlite3.IntegrityError:
            print("No se pudo consultar la tabla")
            self.connection.close()
            return -1

        self.connection.commit()
        self.connection.close()
        return info

    def get_category(self, id):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se devuelve la categoria en funcion del Id
        try:
            self.cursor.execute("SELECT * FROM categoria WHERE id = {}".format(id))
            info = self.cursor.fetchone()
        except sqlite3.IntegrityError:
            print("No se pudo consultar la tabla")
            self.connection.close()
            return -1

        self.connection.commit()
        self.connection.close()
        return info

    def get_plantbyspecs(self, posicion_x=None, posicion_y=None, DensidadFoliar=None, PetalosRadian=None):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # En funcion de lo que se haya introducido se busca
        if DensidadFoliar==None:
            if PetalosRadian==None:
                if posicion_x==None and posicion_y==None:
                    # Devolver todas las plantas (sin condiciones)
                    self.cursor.execute("SELECT * FROM plantas")
                    info = self.cursor.fetchall()

                else:
                    # Devolver plantas con la condicion de posicion
                    self.cursor.execute('''
                        SELECT * FROM plantas WHERE
                        posicion_x = {} AND
                        posicion_y = {}
                    '''.format(posicion_x, posicion_y))
                    info = self.cursor.fetchall()

            else:
                if posicion_x==None and posicion_y==None:
                    # Devolver plantas con condicion de PetalosRadian
                    self.cursor.execute('''
                            SELECT * FROM plantas WHERE PetalosRadian = {}
                        '''.format(PetalosRadian))
                    info = self.cursor.fetchall()

                else:
                    # Devolver plantas con condicion de posicion y de PetalosRadian
                    self.cursor.execute('''
                        SELECT * FROM plantas WHERE
                        posicion_x = {} AND
                        posicion_y = {} AND
                        PetalosRadian = {}
                    '''.format(posicion_x, posicion_y, PetalosRadian))
                    info = self.cursor.fetchall()

        else:
            if PetalosRadian==None:
                if posicion_x==None and posicion_y==None:
                    # Devolver plantas con condicion de DensidadFoliar
                    self.cursor.execute('''
                        SELECT * FROM plantas WHERE DensidadFoliar = {}
                    '''.format(DensidadFoliar))
                    info = self.cursor.fetchall()

                else:
                    # Devolver plantas con condiciones de DensidadFoliar y posicion
                    self.cursor.execute('''
                        SELECT * FROM plantas WHERE
                        posicion_x = {} AND
                        posicion_y = {} AND
                        DensidadFoliar = {}
                    '''.format(posicion_x, posicion_y, DensidadFoliar))
                    info = self.cursor.fetchall()

            else:
                if posicion_x==None and posicion_y==None:
                    # Devolver plantas con condiciones de DensidadFoliar y PetalosRadian
                    self.cursor.execute('''
                        SELECT * FROM plantas WHERE DensidadFoliar = {} AND PetalosRadian = {}
                    '''.format(DensidadFoliar, PetalosRadian))
                    info = self.cursor.fetchall()

                else:
                    # Devolver plantas con condiciones de DensidadFoliar, PetalosRadian y posicion
                    self.cursor.execute('''
                        SELECT * FROM plantas WHERE
                        posicion_x = {} AND
                        posicion_y = {} AND
                        PetalosRadian = {} AND
                        DensidadFoliar = {}
                    '''.format(posicion_x, posicion_y, PetalosRadian, DensidadFoliar))
                    info = self.cursor.fetchall()

        self.connection.commit()
        self.connection.close()

        return info

    def get_plantbycategory(self,category):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se devuelve la categoria en funcion del Id
        try:
            self.cursor.execute("SELECT * FROM categoria WHERE nombre = '{}'".format(category))
            info = self.cursor.fetchone()
        except sqlite3.IntegrityError:
            print("No existe la categoria pedida")
            self.connection.close()
            return -1

        # Se devuelven las plantas que corresponden a dichas categorias
        try:
            self.cursor.execute("SELECT * FROM plantas WHERE categoria_id = {}".format(info[0]))
            plants = self.cursor.fetchall()
        except sqlite3.IntegrityError:
            print("No se ha podido acceder")
            self.connection.close()
            return -1

        self.connection.close()
        return plants

    def delete_plant(self,id):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se borra la planta deseada en funcion del ID
        try:
            self.cursor.execute("DELETE FROM plantas WHERE id = {}".format(id))
        except:
            print("No se ha podido borrar")
            self.connection.close()
            return -1
        else:
            print("Planta borrada con exito")

        self.connection.commit()
        self.connection.close()
        return 1

    def delete_category(self,id):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se borra la planta deseada en funcion del ID
        try:
            self.cursor.execute("DELETE FROM categoria WHERE id = {}".format(id))
        except:
            print("No se ha podido borrar")
            self.connection.close()
            return -1
        else:
            print("Categoria borrada con exito")

        self.connection.commit()
        self.connection.close()
        return 1

    def update_plant(self,id,posicion_x=None,posicion_y=None,DensidadFoliar=None,PetalosRadian=None):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        # Se actualizan los campo de la planta
        try:
            if posicion_x!=None:
                self.cursor.execute("UPDATE plantas SET posicion_x = {} WHERE id = {}".format(posicion_x,id))
                print("Se ha actualizado el campo posicion_x.")
            if posicion_y!=None:
                self.cursor.execute("UPDATE plantas SET posicion_y = {} WHERE id = {}".format(posicion_y,id))
                print("Se ha actualizado el campo posicion_y.")
            if DensidadFoliar!=None:
                self.cursor.execute("UPDATE plantas SET DensidadFoliar = {} WHERE id = {}".format(DensidadFoliar,id))
                print("Se ha actualizado el campo DensidadFoliar.")
            if PetalosRadian!=None:
                self.cursor.execute("UPDATE plantas SET PetalosRadian = {} WHERE id = {}".format(PetalosRadian,id))
                print("Se ha actualizado el campo PetalosRadian.")
        except:
            print("No se ha podido actualizar")
            self.connection.close()
            return -1

        self.connection.commit()
        self.connection.close()
        return 1
