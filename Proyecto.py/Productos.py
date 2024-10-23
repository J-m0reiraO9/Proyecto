#Constructor, metodos y atributo de la clase Productos

class Producto:
    #Constructor de la clase Producto
    def __init__(self, nombre, descripción, precio, categoria, inventario):
        self.nombre = nombre
        self.descripción = descripción
        self.precio = precio
        self.categoria = categoria
        self.inventario = inventario
    
    def show_attr(self):
        print(f"""
              Nombre del Producto = {self.nombre}
              Descripción = {self.descripción}
              Precio = {self.precio}
              Categoria = {self.categoria}
              Inventario = {self.inventario}
              """)
        
class Buscar(Producto):
    def __init__(self, nombre, descripción, precio, categoria, inventario, disponibilidad):
        super().__init__(nombre, descripción, precio, categoria, inventario)
        self.disponibilidad = disponibilidad
