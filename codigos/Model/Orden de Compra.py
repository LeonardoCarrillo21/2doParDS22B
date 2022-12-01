from Mensaje import Mensaje as ms
from cliente import cliente as cl
from Medicamento import Medicamento

class OrdenDeCompra:
    def __init__(self,clien):
        self.idCompra = None
        self.fecha = None
        self.clien = clien
        self.mensaje = ms(self.clien)
        self.medicamentos = []
        self.medicamentos.append(Medicamento("ampicilina","Medicamento contra la infeccion"), Medicamento("Ambroxol","medicamento contra la Toz"))

    def enviarMensaje(self):
        print("enviando mensaje....")
        print(mensaje.toString(medicamentos))

    def SolicitarPago(self):
        print("solicitando Datos:")
        datos = self.clien.enviarDatos()
        print("recibiendo nombre:  " datos[0] )
        print("recibiendo apellido:  " datos[1] )

