#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
#digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
# ingresa el numero a multiplicar 
numero = int(input("Ingrese el número para la tabla de multiplicar: "))
multiplo = 1
# iniciar el bucle
while multiplo <= 10:
    # iniciar el proceso
    resultado = numero * multiplo
    print(f"{numero} x {multiplo} = {resultado}")
    multiplo += 1
