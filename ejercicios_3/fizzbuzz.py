
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 20, 30, 55]

i = 0
while i < len(lista_numeros):
    if lista_numeros[i] % 3 == 0 and lista_numeros[i]%5:
        lista_numeros[i] = "bazinga"
    elif lista_numeros[i] % 3 == 0:
        lista_numeros[i] = "fizz"
    elif lista_numeros[i] % 5:
        lista_numeros[i] = "buzz"
    i += 1


multiplos_dos=[]
multiplos_tres=[]
multiplos_cuatro=[]
multiplos_cinco=[]
multiplos_siete=[]

i = 0
while i < len(lista_numeros):
    if lista_numeros[i]%2==0:
        multiplos_dos.append(lista_numeros[i])
    if lista_numeros[i]%3 == 0:
        multiplos_tres.append(lista_numeros[i])
    if lista_numeros[i]%5 == 0:
        multiplos_cinco.append(lista_numeros[i])
    if lista_numeros[i]%7 == 0:
        multiplos_siete.append(lista_numeros[i])
    i += 1