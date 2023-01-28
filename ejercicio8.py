tabla = {
    "A":0.2,
    "F":0.17,
    "1":0.13,
    "3":0.12,
    "0":0.1,
    "M":0.08,
    "T":0.07
}

class Nodo:
    def __init__(self, letra, freq, der, izq, valor):
        self.freq = freq
        self.der = der
        self.izq = izq
        self.letra = letra
        self.valor = valor

def mezcla(lista):
    for i in range(len(lista) - 1, 0, -1):
        control = False
        for j in range(i, 0, -1):
            if lista[j].freq < lista[j - 1].freq:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
                control = True
        for j in range(i):
            if lista[j].freq > lista[j + 1].freq:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                control = True
        if control == False:
            break
    return lista

def datos(tabla):
    letras = []
    for i in tabla.keys():
        letras.append(Nodo(i, tabla[i], None, None, None))
    mezcla(letras)
    return letras

def arbol_huffman(lista):
    lista = datos(lista)
    arbol = lista
    while len(arbol) > 1:
        izq = lista.pop(0)
        izq.valor = '0'
        der = lista.pop(0)
        der.valor = '1'
        freq = der.freq + izq.freq
        nodo = Nodo(None, freq, der, izq, None)
        arbol.append(nodo)
        mezcla(arbol)
    return arbol

def comprimir_tabla(mensaje, raiz):
    mensaje = mensaje.upper()
    for i in mensaje:
        if i in tabla:
            buscar_letra(i, raiz[0], str())
        else:
            print(i, 'no es un caracter codificable')

def buscar_letra(letra, arbol, valor):
    if arbol != None:
        if arbol.valor != None:
            valor += arbol.valor

        if letra != arbol.letra:
            buscar_letra(letra, arbol.izq, valor)
            buscar_letra(letra, arbol.der, valor)
        else:
            print(valor)


def descomprimir_tabla(raiz, arbol, mensaje, i):
    if i <= len(mensaje)-1:
        if arbol.valor != None:
            if mensaje[i] == arbol.valor and arbol.der != None:
                descomprimir_tabla(raiz, arbol.izq, mensaje, i+1)
                descomprimir_tabla(raiz, arbol.der, mensaje, i+1)
            elif arbol.der == None and mensaje[i] == arbol.valor:
                print(arbol.letra)
                descomprimir_tabla(raiz, raiz, mensaje, i+1)
        else:
            descomprimir_tabla(raiz, arbol.izq, mensaje, i)
            descomprimir_tabla(raiz, arbol.der, mensaje, i)


mensaje = arbol_huffman(tabla)  
comprimir_tabla(input('Introduzca el mensaje a codificar: '), mensaje)
descomprimir_tabla(mensaje[0], mensaje[0], input("Introduzca mensaje a descodificar: "), 0)