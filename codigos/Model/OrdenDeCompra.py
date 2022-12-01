from Mensaje import Mensaje as ms
from cliente import cliente as cl
from Medicamento import Medicamento

class OrdenDeCompra:
    def __init__(self,clien):
        
        
        self.idCompra = None
        self.fecha = None
        self.clien = clien
        self.mensaje = ms(self.clien.nombre)
        self.medicamentos = []
        self.medicamentos.append(Medicamento("ampicilina","Medicamento contra la infeccion"))
        self.medicamentos.append(Medicamento("Ambroxol","medicamento contra la Toz"))

    def enviarMensaje(self):
        
        print("enviando mensaje....")
        print(self.mensaje.toString(self.medicamentos))

    def SolicitarPago(self):
        
        print("solicitando Pago:")
        nom,app = self.clien.solicitar()
        print("deudor nombre:  ", nom )
        print("deudor apellido:  ", app )

