descuentosBoletas = [
    {"color": "rojo", "descuento": 0.15},
    {"color": "verde", "descuento": 0.20}
]
totalCompra=float(input('total_compra: '))
colordelaBoleta=input("ingrese el color de la boleta (rojo, verde, otro color: )").strip().lower()
if colordelaBoleta=='rojo': 
    porcentajedelDescuento=0.15
    
elif colordelaBoleta=='verde':
    porcentajedelDescuento=0.20
else:
    porcentajedelDescuento=0.00
descuento=totalCompra*porcentajedelDescuento
totalconDescuento=totalCompra-descuento
print(f"total de la compra  ${totalCompra:.2f}")
print(f"el color de la boleta: {colordelaBoleta.capitalize()}")
print(f"el valor del descuento ${descuento:.2f}")
print(f"el total con descuento es ${totalconDescuento:.2f}")