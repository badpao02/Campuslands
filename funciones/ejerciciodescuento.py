def descuento(valor):
    if valor > 150000:
        d= valor * 0.05

    else:
        d = 0 
    return d 

valor=int(input("ingrese el valor del articulo"))
d= descuento(valor)
print(f"el descuento es:${d:,}")

