lista_numeros = []
i = 0

while i < 5:
    lista_numeros.append(int(input("dime un numero:")))
    i += 1

numero_grande = lista_numeros[0]
for numero in lista_numeros:
    if numero_grande < numero:
        numero_grande = numero

numero_pequeno=lista_numeros[0]
for numero in lista_numeros:
    if numero_pequeno > numero:
        numero_pequeno = numero

suma=0
for numero in lista_numeros:
    suma += numero

media = suma/len(lista_numeros)

print("Numero mas grande:{}\nNumero mas pequeño:{}\nMedia:{}".format(numero_grande,numero_pequeno,media))