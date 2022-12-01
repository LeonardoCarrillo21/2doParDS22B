
class Medicamento:

    def __init__(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def caducar(self, ):

        print("caducando")
        

    def toString(self, ):
        """
        devuelve los datos del medicamento
        Args:
        

        Returns:
            cad (String): Los valores de los datos en formato String organizados 1 por uno
        """
        cad = "\n\tNombre Medicamento: " + self.nombre
        cad += "\n\tdescripcion Medicamento: " + self.descripcion
        return cad

