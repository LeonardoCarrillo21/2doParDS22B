from cliente import cliente as cl
from OrdenDeCompra import OrdenDeCompra as OC


nuevoCliente = cl("leonardo","carrillo")
orden = OC(nuevoCliente)

orden.enviarMensaje()
orden.SolicitarPago()