

apetece_helado_input = input("Te apetece un helado? (Si/No)").capitalize()
tienes_dinero_input = input("Tienes dinero? (Si/No)").capitalize()
esta_tu_tia_input = input("estas con tu tia? (Si/No)").capitalize()

apetece_helado = apetece_helado_input == "Si"
tienes_dinero = tienes_dinero_input == "Si"
esta_tu_tia= esta_tu_tia_input == "Si"

if apetece_helado and (tienes_dinero or esta_tu_tia):
    print('comete un helado')
elif apetece_helado:
    print("pues ve por dinero")
else:
    print("pues nada")