#Constructor, metodos y atributos de la clase Indicadores de gestion
from dataclasses import dataclass
@dataclass
class Indicadores_de_gestion:
    #Constructor de la clase Indicadores de Gestion
    
    informes_ventas = str
    informes_pago = str
    informes_envio = str

    def __init__(self, informes_ventas, informes_pago, informe_envio):
        self.informes_ventas = informes_ventas
        self.informes_pago = informes_pago
        self.informes_envio = informe_envio
        
    def show_attr(self):
        print(f"""
              Informes de ventas = {self.informes_ventas}
              Informes de pago = {self.informes_pago}
              Informes de Envio {self.informes_envio}""")
        
