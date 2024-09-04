# Define una lista de diccionarios con los descuentos asociados a cada color de boleta
descuentosBoletas = [
    {"color": "rojo", "descuento": 0.15},
    {"color": "verde", "descuento": 0.20}
]

# Solicita al usuario el total de la compra y lo convierte a tipo float
totalCompra = float(input('total_compra: '))

# Solicita al usuario el color de la boleta, elimina espacios en blanco al inicio y al final, y convierte a minúsculas
colordelaBoleta = input("ingrese el color de la boleta (rojo, verde, otro color: )").strip().lower()

# Verifica el color de la boleta para determinar el porcentaje de descuento
if colordelaBoleta == 'rojo': 
    porcentajedelDescuento = 0.15  # Asigna un descuento del 15% si el color es rojo
    
elif colordelaBoleta == 'verde':
    porcentajedelDescuento = 0.20  # Asigna un descuento del 20% si el color es verde
    
else:
    porcentajedelDescuento = 0.00  # Sin descuento si el color no es rojo ni verde

# Calcula el monto del descuento aplicando el porcentaje al total de la compra
descuento = totalCompra * porcentajedelDescuento

# Calcula el total a pagar después de aplicar el descuento
totalconDescuento = totalCompra - descuento

# Imprime el total de la compra sin descuento, formateado a dos decimales
print(f"total de la compra  ${totalCompra:.2f}")

# Imprime el color de la boleta con la primera letra en mayúsculas
print(f"el color de la boleta: {colordelaBoleta.capitalize()}")

# Imprime el valor del descuento aplicado, formateado a dos decimales
print(f"el valor del descuento ${descuento:.2f}")

# Imprime el total a pagar después de aplicar el descuento, formateado a dos decimales
print(f"el total con descuento es ${totalconDescuento:.2f}")
