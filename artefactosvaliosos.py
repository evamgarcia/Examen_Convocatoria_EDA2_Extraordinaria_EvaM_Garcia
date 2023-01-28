class Artefactosvaliosos(object):
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print(f"El artefacto {self.nombre} se ha creado con éxito")

    def __str__(self) -> str:
        return f"El artefacto {self.nombre} pesa {self.peso} y su precio es de {self.precio} y su fecha de caducidad es {self.fecha_caducidad}"



    def crear_artefacto_valioso():
            mochila = []
            num = int(input("cuantos artefactos quieres crear:"))
            for i in range (1,num+1):
                nombre = input("Nombre del artefacto: ")
                peso = input("Peso del artefacto: ")
                precio = input("Precio del artefacto: ")
                fecha_caducidad = input("Fecha de caducidad del artefacto: ")
                artefacto = Artefactosvaliosos(nombre, peso, precio, fecha_caducidad)
                mochila.append(artefacto)
            return mochila
    
def crear_mochila(self):
    mochila = self.crear_artefacto_valioso()
    for i in range(len(mochila) - 1, 0, -1):
        control = False
        for j in range(i, 0, -1):
            if mochila[j].fecha_caducidad < mochila[j - 1].fecha_caducidad:
                mochila[j], mochila[j - 1] = mochila[j - 1], mochila[j]
                control = True
        for j in range(i):
            if mochila[j].fecha_caducidad > mochila[j + 1].fecha_caducidad:
                mochila[j], mochila[j + 1] = mochila[j + 1], mochila[j]
                control = True
        if control == False:
            break
    return mochila



collar = Artefactosvaliosos(3, "collar", 105, "13/11/2021")
pendientes = Artefactosvaliosos(5, "pendientes", 50, "29/11/2023")
reloj = Artefactosvaliosos(4, "reloj", 256, "12/12/2020")

crear_mochila(collar, reloj, pendientes)