#Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.
# definir variables
numerosPositivos = 0
numerosNegativos = 0
numerosNeutros=0
i = 0
# iniciar el bucle
while i < 20:
    numero = float(input("Introduce un número: "))
    if numero > 0:
        numerosPositivos += 1
    elif numero < 0:
        numerosNegativos += 1
    elif numero==0:
       numerosNeutros +=1
    i += 1
    # Imprimir resultados
print(f"Cantidad de números positivos: {numerosNegativos}")
print(f"Cantidad de números negativos: {numerosPositivos}")
print(f"cantidad de numeros Neutros :{numerosNeutros}")
