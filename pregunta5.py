def hijo_sin_amor(mochila, objetos_sacados=0, objeto_buscado="anillo de poder"):
    if not mochila:
        return ("No hay nada en la mochila", objetos_sacados)
    else:
        objeto = mochila.pop(0)
        objetos_sacados += 1
        if objeto == objeto_buscado:
            return ("Para encontrar el " + objeto_buscado + " han sido sacados " + str(objetos_sacados), objetos_sacados)
        else:
            return hijo_sin_amor(mochila, objetos_sacados, objeto_buscado)


mochila = ["mi gato", "anillo de poder", "ganas de estudiar", "llaves de casa"]
print(hijo_sin_amor(mochila, objeto_buscado="anillo de poder"))