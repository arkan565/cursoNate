
numero=int(input("dime el numero del que quieres saber la tabla de multiplicar:"))
i = 0
while i <= 10:
    print("{} X {} = {}".format(numero, i, numero*i))
    i += 1
i = 5
while i <= 15:
    print("{} X {} = {}".format(numero, i, numero * i))
    i += 1
i = 0
while i <= 10:
    if (numero*i) % 2 == 0:
        print("{} X {} = {}".format(numero, i, numero * i))
    i += 1