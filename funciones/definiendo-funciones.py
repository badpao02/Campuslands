# la definicion de la funcion 
def longstring(str):
    try:
        long = 0
        while str[long] != None:
            long +=1
    except:
        pass
    return long

def prepararCafe(insumo1,insumo2):
    salida = ""
    if insumo1.lower() == "cafe" and insumo2.lower () == "agua":
        salida = "tinto"
    else: 
        salida = "Se daño la cafetera" 
    return salida

#uso de la funcion 
taza = prepararCafe("cafe", "agua")
print()
print(taza)
print(longstring(taza))




