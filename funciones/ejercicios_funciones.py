
def max_3(numero1, numero2, numero3):
    max=numero1
    if numero2 > max:
        max = numero2
    if numero3>max:
        max = numero3
    return max


def numero_en_rango(numero,rango_menor,rango_mayor):
    if numero in range(rango_menor,rango_mayor):
        return True
    else:
        return False


def devolver_pares(lista):
    lista_final = []
    for numero in lista:
        if numero % 2 == 0:
            lista_final.append(numero)

    return lista_final


print("{}".format(max_3(3, 10, 5)))
print("{}".format(numero_en_rango(200, 1, 100)))
print("{}".format(devolver_pares([1, 2, 10, 15, 30, 50])))
