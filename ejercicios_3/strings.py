user_string = input("introduzca una cadena de caracteres:")

string_replace = user_string.replace("A","VACA")
string_replace = string_replace.replace("a","VACA")
print(string_replace)

vocales_i = user_string.replace('a', 'i')
vocales_i = vocales_i.replace('A', 'i')
vocales_i = vocales_i.replace('e', 'i')
vocales_i = vocales_i.replace('E', 'i')
vocales_i = vocales_i.replace('I', 'i')
vocales_i = vocales_i.replace('o', 'i')
vocales_i = vocales_i.replace('O', 'i')
print(vocales_i)
i = 0
contador = 1
user_string = user_string.lower()
caracteres = list(user_string)
while i < len(user_string):
    if user_string[i] in "aeiou":
        caracteres[i] = "{}".format(contador)
        contador += 1
    i += 1
user_string = "".join(caracteres)
print(user_string)