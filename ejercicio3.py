class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"Se ha creado la armadura {self.nombre} de rango {self.rango} con exito")

    def __str__(self) -> str:
        return f"La armadura {self.nombre} de rango {self.rango} "
 
    def calificacion(self):
        self.codigo_legion = self.nombre
        self.id_ciherenta = self.rango // 1000
        self.id_siglo = (self.rango //100) % 10
        self.numero_armadura = (self.rango // 10)%10
        self.numero_escuadra = self.rango % 10
        return f"El código de la legión es {self.codigo_legion}, el id de la cohorte es {self.id_ciherenta}, el id del siglo es {self.id_siglo}, el número de armadura es {self.numero_armadura} y el número de escuadra es {self.numero_escuadra}"


armadura1 = Armadura("MK", 1234)
armadura2 = Armadura("RT", 1435)
armadura3 = Armadura("ET", 5436)
armadura4 = Armadura("PE", 6737)
ARMADURAS = [armadura1, armadura2, armadura3, armadura4]
calificaciones = [armadura.calificacion() for armadura in ARMADURAS]
    