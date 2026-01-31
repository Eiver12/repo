import sqlite3

class Basedatos():
    def __init__(self, nombre_bd="BASEDATOS.bd"):
        self.nombre_bd = nombre_bd
        self.conexion = None
        self.cursor = None
        
        self.conectar() #! conectar la base 
        self.crear_tablas() #! crear la base 
        
    def conectar(self):
        
        try:
            self.conexion = sqlite3.connect(self.nombre_bd)
            self.cursor = self.conexion.cursor()
            
        except sqlite3.Error as e:
            print(f"Error al crear la base de datos: {e}")
            
    def crear_tablas(self):
        script = ""
        
        try:
            self.cursor.executescript(script)
            self.conexion.commit()
            
        except sqlite3.Error as e:
            print(f"Error en la creacion de las tablas: {e}")
    
    def cerrar_conexion(self):
        
        if self.conexion:
            self.conexion.close()
            print(f"Base {self.nombre_bd} cerrada")
    

if __name__ == "__main__":
        base_datos = Basedatos()
        base_datos.cerrar_conexion()