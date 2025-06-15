# Escribe una función llamada buscarPalabra que reciba como argumentos una palabra objetivo (objetivo) y una lista de palabras (palabras).
# La función debe comprobar si la palabra objetivo está en la lista y devolver un mensaje indicando si fue encontrada o no.

palabra_objetivo = "hola"

lista_de_palabras = ["hola", "como", "cuando", "porque", "quizas", "adios"]

def buscarPalabra(objetivo, palabras):
    for i in palabras:
        if i == objetivo:
            return f"La palabra {objetivo} esta en la lista de palabras"
        else:
            return f"La palabra {objetivo} no esta en la lista de palabras"
        
print(buscarPalabra(palabra_objetivo,lista_de_palabras))

# Crea una función llamada imprimirListaInversa que reciba una lista de elementos y la imprima en orden inverso (sin usar [::-1]).
# Debes recorrer la lista manualmente desde el último elemento hasta el primero e imprimir cada uno en una línea diferente.

lista_elementos = [2,4,5,7,6,6,7,9]

def imprimirListaInversa(lista):
    lista_invertida = []
    for i in range (len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida
print(imprimirListaInversa(lista_elementos))

# Dada la lista nombres y el diccionario edades, escribe un programa que imprima para cada persona su nombre y su edad, en este formato:
# Mengano tiene 0 años  
# Fulano tiene 25 años  
# ...

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

def devolver_edades (nombres,edades):
    for i in nombres:
        if i in edades:
            print(f"{i} tiene {edades[i]} años")

        
print(devolver_edades(nombres,edades))