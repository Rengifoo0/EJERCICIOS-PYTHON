#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números
# definir variables
contador = 0
suma = 0
# iniciar bucle
while contador < 10:
   numero = float(input("Ingresa un número negativo: "))
if numero < 0:
        numeroPositivo = -numero
        suma += numeroPositivo
        contador += 1
else:
        print("El número ingresado no es negativo. Por favor, ingresa un número negativo.")
print("La suma de los números positivos es:", suma)

