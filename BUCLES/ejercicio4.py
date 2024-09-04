#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
#Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
#de todo el grupo. 
sumadeCalificaciones = 0
calificacionmasAlta = 0
calificacionmasBaja = 0 
# iniciar el bucle 
for i in range(20):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    sumadeCalificaciones += calificacion
    if calificacion > calificacionmasAlta:
        calificacionmasAlta = calificacion
    if calificacion < calificacionmasBaja:
        calificacionmasBaja = calificacion
promedio = sumadeCalificaciones / 20
# imprimir resultados 
print(f"Promedio de calificaciones: {promedio:.2f}")
print(f"Calificación más alta: {calificacionmasAlta:.2f}")
print(f"Calificación más baja: {calificacionmasBaja:.2f}")
