
class Mensaje:
    def __init__(self,destinatario):
        self.destinatario = destinatario
        self.cuerpoDelMensaje = "--------Su orden creada por farmacias----"

    def toString(self, medicamentos):
        """
        metodo que devuelve el valor del mesnaje en cadena
    
        Args:
        
            medicamentos (list): Los medicamentos que contiene la lista de compra, la cual tiene datos que deben pasarse a String
        Returns:

            cad (String): Cadena de caracteres con todo el mensaje y como se va a escribir

        """
        cad = "\tPara: " + self.destinatario
        cad += "\n\tcuerpo del mensaje: " + self.cuerpoDelMensaje
        for medicamento in medicamentos:
            cad += "\nmedicamento: " + medicamento.toString()
        cad +="\n\t----------------"
        return cad


    def equals(self,otro):
        pass

