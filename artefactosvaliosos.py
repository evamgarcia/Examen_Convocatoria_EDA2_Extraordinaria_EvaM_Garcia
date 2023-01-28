class Artefactosvaliosos(object):
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print(f"El artefacto {self.nombre} se ha creado con éxito")

    def __str__(self) -> str:
        return f"El artefacto {self.nombre} pesa {self.peso} y su precio es de {self.precio} y su fecha de caducidad es {self.fecha_caducidad}"



artefacto1 = Artefactosvaliosos(3, "mi gato", 105, "13/11/2022")
artefacto2 = Artefactosvaliosos(5, "sable luz", 50, "29/11/2021")
artefacto3 = Artefactosvaliosos(4, "anillo de poder", 256, "12/12/2024")

artefactos = [artefacto1, artefacto2, artefacto3]

def ordenar_artefactos(artefactos):
    artefactos.sort(key=lambda x: x.fecha_caducidad)
    for artefacto in artefactos:
        print(artefacto)


print(ordenar_artefactos(artefactos))

artefacto3.precio = 253
print("\n El precio del artefacto ha sido modificado. El nuevo precio es:")
print(artefacto3)