#Constructor, metodos y atributo de la clase Clientes

class Cliente:
        #Constructor de la clase Cliente
    def __init__(self, nombre, apellido, cedula, rif, correo_electronico, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.rif = rif
        self.correo = correo_electronico
        self.telefono = telefono
        
    def show_attr(self):
        print(f"""
              Nombre = {self.nombre + self.apellido}
              Cedula = {self.cedula or self.rif}
              Correo Electronico = {self.correo}
              Telefono = {self.telefono}
              """)
        
class Juridico(Cliente):
    def __init__(self, nombre, apellido, cedula, rif, correo_electronico, telefono):
        super().__init__(nombre, apellido, cedula, rif, correo_electronico, telefono)
