
lista = [1, 2, "a", 24, 35, "hola" ]

lista_tipos = []

for dato in lista:
    lista_tipos.append(type(dato))

lista_enteros = []
lista_strings = []
i=0
for dato in lista_tipos:
    if dato == int:
        lista_enteros.append(lista[i])
    elif dato == str:
        lista_strings.append(lista[i])
    i += 1

multiplicacion = 1
for dato in lista_enteros:
    multiplicacion = multiplicacion * dato

lista_largo = []
for string in lista_strings:
    lista_largo.append(len(string))
