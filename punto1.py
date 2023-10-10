# punto 1

ventaMesTotal  = 0 
comisionesTotales = 0

while True:
    cedula = int(input("Ingrese la cédula (-1 para terminar): "))
    if cedula == -1:
        break
    nombre = input("Ingrese el nombre del vendedor: ")
    tipo_vendedor = int(input("Ingrese el tipo de vendedor (1, 2 o 3): "))
    ventas_mes = float(input("Ingrese el valor de las ventas realizadas en el mes: "))

    if tipo_vendedor == 1:
        comision = ventas_mes * 0.20
    elif tipo_vendedor == 2:
        comision = ventas_mes * 0.15
    elif tipo_vendedor == 3:
        comision = ventas_mes * 0.25
    else:
        print("Tipo de vendedor no válido")
        continue
    
    ventaMesTotal += ventas_mes
    comisionesTotales += comision

    print(f"Comisión a pagar a {nombre}: ${comision:.2f}")
print(f"Valor total de ventas del mes: ${ventaMesTotal:.2f}")


#punto 2 

bandera = True
gananciaConductores = 0
contNovatos = 0
contExpert = 0
while bandera == True:
    cantidadConductores = int(input("¿Cuantos conductores son? "))
    for i in range(cantidadConductores):
        cedula = input("\nIngrese la cedula del conductor:  ")
        name = input("Ingrese el nombre del conductor:  ")
        claseConductor = int(input("Ingrese la clase del conducor siendo:\n          [1]->Experto\n          [2]->Novato\nLa clase es: "))
        ingresosPasajes = float(input("Cuantas ganancias genero por pasajes? "))
        ingresoEncomiendad = float(input("¿Cuantas ganancias genero por encomiendad? "))

        if claseConductor == 1:
            ganancias = ingresosPasajes*0.3 + ingresoEncomiendad*0.2
            contExpert += 1
            print(f"El conductor {name} obtuvo una ganancia de : ${ganancias:,.0f}")
        elif claseConductor == 2:
            ganancias = ingresosPasajes*0.2 + ingresoEncomiendad*0.15
            contNovatos += 1
            print(f"El conductor {name} obtuvo una ganancia de : ${ganancias:,.0f}")
    bandera = False
    gananciaConductores += ganancias
print("="*18,"INFORME GENERAL","="*18)
print(f"El valor total a pagar a los conductores es: ${gananciaConductores:,.0f} COP")
print(f"La cantidad de conductores NOVATOS es :{contNovatos} y la cantidad de conductores EXPERTOS es:{contExpert}") 