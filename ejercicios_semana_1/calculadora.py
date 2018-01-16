numero_1 = int(input("dime el primer numero"))
numero_2 = int(input("dime el segundo numero"))
operacion = input("que quieres hacer Sumar, Restar , Multiplicar, Dividir?").capitalize()

if operacion =="Sumar":
    print("{}".format(numero_1+numero_2))
elif operacion=="Restar":
    print("{}".format(numero_1 - numero_2))
elif operacion=="Multiplicar":
    print("{}".format(numero_1 * numero_2))
elif operacion=="Dividir":
    print("{}".format(numero_1 /numero_2))