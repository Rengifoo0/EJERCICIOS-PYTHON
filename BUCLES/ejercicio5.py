#Una persona debe realizar un muestreo con 50 personas para determinar el
#promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
#Las categorías se determinar de acuerdo a la siguiente tabla:
# Listas para almacenar los pesos de las personas en diferentes categorías de edad
pesosNiños = []
pesosJovenes = []
pesosAdultos = []
pesosAncianos = []
# Bucle para ingresar los datos de 50 personas
for i in range(50):
    # Solicita al usuario que ingrese la edad 
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    # Solicita al usuario que ingrese el peso de la persona
    peso = float(input(f"Ingrese el peso de la persona {i+1}: "))
    # Clasifica el peso según la edad en las listas correspondientes
    if edad <= 12:
        pesosNiños.append(peso)  # Añade el peso a la lista de pesos de niños
    elif edad <= 29:
        pesosJovenes.append(peso)  # Añade el peso a la lista de pesos de jóvenes
    elif edad <= 59:
        pesosAdultos.append(peso)  # Añade el peso a la lista de pesos de adultos
    else:
        pesosAncianos.append(peso)  # Añade el peso a la lista de pesos de ancianos
# Función para calcular y mostrar el promedio de pesos en una categoría dada
def calcular_promedio(pesos, categoria):
    if pesos:  
        promedio = sum(pesos) / len(pesos)  
        print(f"Promedio de peso en la categoría {categoria}: {promedio:.2f} kg")
# mostrar el promedio de pesos para cada categoría
calcular_promedio(pesosNiños, "Niños")
calcular_promedio(pesosJovenes, "Jóvenes")
calcular_promedio(pesosAdultos, "Adultos")
calcular_promedio(pesosAncianos, "Ancianos")

