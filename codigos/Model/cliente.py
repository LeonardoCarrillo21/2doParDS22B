

class cliente:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def enviarDatos(self):
        """
        funcion que devuelve le valor de cada uno de los datos de la clase
        Args:
        
        Returns:

            self.nombre (String): Nombre del cliente
            self.apellido (String): Apellido del cliente
        """
        return self.nombre,self.apellido

    def solicitar(self):
        """
        metodo que solicita lso datos de la clase

        Args:
        
        Returns:
            self.enviarDatos() (String): La funcion que devuelve en valor string los datos del cliente
        """
        print("solicitando")
        return self.enviarDatos()


    