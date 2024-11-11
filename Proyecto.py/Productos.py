#Constructor, metodos y atributo de la clase Productos
from dataclasses import dataclass
@dataclass
class Producto:
    #Constructor de la clase Producto
    
    nombre: str
    id: int
    descripción: str
    precio: float
    categoria: str
    inventario: str
    modelo_vehiculo: list[str]
    
    def __init__(self, nombre, id, descripción, precio, categoria, inventario, modelo_vehiculo):
        self.nombre = nombre
        self.id = id
        self.descripción = descripción
        self.precio = precio
        self.categoria = categoria
        self.inventario = inventario
        self.modelo_vehiculo = modelo_vehiculo
    
    def show_attr(self):
        #Muestra en la consola los datos del cliente
        print(f"""
              Nombre del Producto = {self.nombre}
              Id = {self.id}
              Descripción = {self.descripción}
              Precio = {self.precio}
              Categoria = {self.categoria}
              Inventario = {self.inventario}
              Modelo de Vehiculo = {self.modelo_vehiculo}
              """)
    
