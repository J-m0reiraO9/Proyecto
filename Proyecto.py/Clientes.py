#Constructor, metodos y atributo de la clase Clientes
from dataclasses import dataclass
@dataclass
class Cliente:
        #Constructor de la clase Cliente
    nombre : str 
    apellido: str 
    cedula: int
    correo: str 
    telefono : str 
       
    def __init__(self, nombre, apellido, cedula, correo_electronico, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo_electronico
        self.telefono = telefono
        
    def show_attr(self):
        print(f"""
              Nombre = {self.nombre}
              Apellido = {self.apellido}
              Cedula = {self.cedula}
              Correo Electronico = {self.correo}
              Telefono = {self.telefono}
              """)
        
@dataclass
class Juridico(Cliente):
    
    nombre_juridico: str
    rif: int
    
    def __init__(self, nombre_juridico, rif, correo_electronico, telefono):
        super().__init__("", "", "", correo_electronico, telefono)
        self.nombre_juridico = nombre_juridico
        self.rif = rif
