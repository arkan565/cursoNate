
string_usuario=input("Cual es la cadena de la que quieres contar carácteres:")

vocales_comparar="aeiouAeiou"

vocales=[]
mayusculas = 0
espacios = string_usuario.count(' ')
puntos = string_usuario.count('.')
comas = string_usuario.count(',')

for letra in string_usuario:
    if letra.isupper():
        mayusculas += 1
    if vocales_comparar.count(letra) > 0:
        vocales.append(letra)
print("mayusculas:{}\nespacios:{}\npuntos:{}\ncomas:{}\nvocales:{}".format(mayusculas, espacios, puntos, comas, vocales))
