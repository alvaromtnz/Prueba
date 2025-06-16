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

#1. Crea una función para detectar si un numero o texto es palindromo/capicúa

def es_palindormo ():
    palabra = input("Escriba una palabra: ")
    al_reves = palabra[::-1]
    if palabra == al_reves:
        return f"La palabra {palabra} es palindormo"
    else:
        return f"La palabra {palabra} no es palindormo"
    
print(es_palindormo())

#2. Escribe una función que reciba una lista de números y un número objetivo. La función debe devolver cuántas veces aparece el número.

lista_numeros = [3,5,23,45,3,4,6,4,4,4,4,4,4,4]

numero_objetivo = 4

def buscadorNumeroObjetivo(lista, objetivo):
    contador = 0 
    for i in lista:
        if i == objetivo:
            contador += 1
    return f"El numero {objetivo} aparece {contador} veces"
        
print(buscadorNumeroObjetivo(lista_numeros,numero_objetivo))

#3. Crea una función que reciba una lista de números y devuelva el valor máximo y mínimo de la lista.

lista_maximo_minimo = [43,0,9,6]

def maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return f"El maximo de la lista es {maximo} y el minimo es {minimo}"

print (maximo_minimo(lista_maximo_minimo))

#4. Escribe una función para que invierta una lista de números enteros.

lista_enteros = [1,4,5,3,4,6,7,78,4]

def invertir_lista(lista):
    resultado = []
    for i in range(len(lista)-1,-1,-1):
        resultado.append(lista[i])
    return resultado

print(invertir_lista(lista_enteros))

# o mucho mas facil

lista_enteros = [1,4,5,3,4,6,7,78,4]

def invertir (lista):
    al_reves = lista[::-1]
    return f"La lista invertida seria {al_reves}"

print(invertir(lista_enteros))

#5. Define una función que reciba una cadena de texto y cuente cuántas vocales (a, e, i, o, u) contiene.

def cadena_de_texto ():
    contador = 0 
    palabra = input("Escriba una palabra o una cadena de texto: ")
    for i in palabra:
        if i in "aeiou":
            contador += 1
    if contador > 0:
        return f"La palabra {palabra} tiene {contador} vocales"
    else:
        return f"la palabra {palabra} no tiene ninguna vocal"


#6. Escribe una función que recibe una lista de números y devuelva el promedio de los mismos.

lista_promedio = [1,2,3,4,5,6,7]

def division(lista):
    suma = sum(lista)
    cantidad = len(lista)
    promedio = suma / cantidad
    return f"El promedio de la lista es {promedio}"

print (division(lista_promedio))


#7. Escribe una función que reciba un número y genera su tabla de multiplicar hasta el 10, mostrando los resultados en formato de lista.

#8. Crea una función que reciba un número entero y devuelva la suma de todos sus dígitos.

#9. Define una función para que, dada una palabra, la devuelva invertida, por medio de bucles.