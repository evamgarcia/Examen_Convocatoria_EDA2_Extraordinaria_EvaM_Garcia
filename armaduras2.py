class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"Se ha creado la armadura {self.nombre} de rango {self.rango} con exito")

    def calificacion(self):
        codigo_legion = self.nombre
        id_ciherenta = self.rango // 1000
        id_siglo = (self.rango //100) % 10
        numero_armadura = (self.rango // 10)%10
        numero_escuadra = self.rango % 10
        return f"El código de la legión es {codigo_legion}, el id de la cohorte es {id_ciherenta}, el id del siglo es {id_siglo}, el número de armadura es {numero_armadura} y el número de escuadra es {numero_escuadra}"
       

            

armadura1 = Armadura("MK", 1234)
armadura2 = Armadura("RT", 1435)
armadura3 = Armadura("ET", 5436)
armadura4 = Armadura("PE", 6737)

ARMADURAS = [armadura1, armadura2, armadura3, armadura4]
calificaciones = [armadura.calificacion() for armadura in ARMADURAS]
    