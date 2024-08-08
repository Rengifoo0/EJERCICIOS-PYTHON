nombre=(input("nombre del estudiante "))
colegio=(input("nombre del colegio: "))
curso=(input("grado que cursa: "))
print(f"El estudiante {nombre} estudia en el {colegio} el programa de formación {curso}")


#ejersicio 2
base=int(input("digite la base: "))
altura=int(input("digite la altura: "))
print(f"el perimetero del rectangulo es:{base*altura} el area del r ectangulo es:{2*(base+altura)}")


#ejersicio 3
numero1=int(input("digite el primer numero: "))
numero2=int(input("digite el segundo numero: "))
numero3=int(input("digite el tercer numero: "))
resultado=numero1+numero2+numero3
print(f"el promedio de los numeros ingresados es {resultado/3} ")


#ejercicio 4
nombre= input("digite su nombre: ")
sueldo=int (input("digite el sueldo: "))
comision=int (input("digite la comision : "))
ventasrealizadas=int(input("digite las ventas realizadas: "))
comisiones= (ventasrealizadas/100) * comision
sueldo_final = comisiones + sueldo

print(f"el trabajador {nombre} tiene un sueldo de: {sueldo} y una comision de: {comision} en este mes realizo {ventasrealizadas} ventas con esto tuvo un total de {comisiones} comisiones conseguidas y un sueldo final de {sueldo_final}")

#ejercicio 5
valor_delacompra= int (input("digite el valor de la compra: "))
valor_deldescuento= int (input("digite el descuento: "))
descuento= (valor_delacompra * valor_deldescuento) /100
total = valor_delacompra - descuento
print(f"el producto tiene un costo de: {valor_delacompra} el producto tiene un descuento del {valor_deldescuento}% entonces le quedaria en: {total} ")

#ejercicio adicional
nombre=input("digite su nombre: ")
notaactividadesenclase=int(input("ingrese la calificacion por actividades en clase (0-100): "))
notaproyectofinal=int(input("ingrese la calificacion por proyecto final:(0-100)"))
notaevaluacionesparciales=int(input("ingresar la calificacion por evaluaciones: (0-100)"))
porcentajeactividades = 30
porcentajeprojectofinal = 50
porcentajeevaluaciones = 20
resultado= (notaactividadesenclase*porcentajeactividades/100 + notaproyectofinal*porcentajeprojectofinal/100+ notaevaluacionesparciales*porcentajeevaluaciones/100)
print(f"la nota final de algoritmia del estudiante {nombre} es {resultado} ")