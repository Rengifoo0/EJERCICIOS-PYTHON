nombre=input("escriba su nombre ")
sexo=input("masculinno o femenino ")
edad=int(input("cuantos años tienes "))
if sexo == "masculino":
    numeroPulsaciones=(210-edad)/10
elif sexo == "femenino":
    numeroPulsaciones=(220-edad)/10
print("el nombre es: {0} sexo es {1} su edad {2} años y el numero de sus pulsaciones son :{3}".format(nombre.capitalize(),sexo.capitalize(), edad,numeroPulsaciones))