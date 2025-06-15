# Escribe una función llamada buscarPalabra que reciba como argumentos una palabra objetivo (objetivo) y una lista de palabras (palabras).
# La función debe comprobar si la palabra objetivo está en la lista y devolver un mensaje indicando si fue encontrada o no.

palabra_objetivo = "ola"

lista_de_palabras = ["hola", "como", "cuando", "porque", "quizas", "adios"]

def buscarPalabra(objetivo, palabras):
    for i in palabras:
        if i == objetivo:
            return f"La palabra {objetivo} esta en la lista de palabras"
        else:
            return f"La palabra {objetivo} no esta en la lista de palabras"
        
print(buscarPalabra(palabra_objetivo,lista_de_palabras))


#def imprimirListaInversa(lista):


#nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
#edades = {
    #"Mengano": 0,
    #"Fulano": 25,
    #"Zutano": 50,
    #"Perantano": 75
#}
