#Constructor, metodos y atributo de la clase Clientes

class Cliente:
        #Constructor de la clase Cliente
    def __init__(self, nombre, apellido, cedula, correo_electronico, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo_electronico
        self.telefono = telefono
        
    def show_attr(self):
        print(f"""
              Nombre = {self.nombre + self.apellido}
              Cedula = {self.cedula}
              Correo Electronico = {self.correo}
              Telefono = {self.telefono}
              """)
        
class Juridico(Cliente):
    def __init__(self, nombre, apellido, cedula, correo_electronico, telefono):
        super().__init__(nombre, apellido, cedula, correo_electronico, telefono)
