n = int(input("cuantos usuarios?"))

totalConsumo = 0
for i in range(1, n+1): 
    print(f"\n Datos del usuario #{i}")
    cod = input("codigo?")
    nom = input("nombre?")
    est = input("estado [v: vigente o S: suspendido]?")
    estr = int(input("estrato [1 al 6]?"))
    con = float(input("condumo agua del mes [cm3]?"))

    if est == "V"  or est == "v":
         
    elif estr ==1:
            tbas= 10000
    elif estr ==2:
            tbas= 20000
    elif estr ==3:
            tbas= 30000
    elif estr ==4:
            tbas= 45000
    elif estr ==5:
            tbas= 60000
    elif estr ==6:
            tbas= 70000
    else:
        tbas = 0

#calcular el valor del consumo 
valcons = con * 200 

# calcular el valor a pagar 
valpagar = tbas + valcons 


# calcular el valor total a pagar de todos los usuarios 
totalConsumo += valpagar

#imprimir el informe del usuario 
print("\n" "=" * 40)
print("\tnombre: ", nom)
print(f"\tvalor tarifa basica: ${tbas: ,}")
print(f"\tvalor consumo: ${valcons:,.0f}")
print(f"\tvalor de la factura del agua:{valpagar:,.0f}")

# imprimir valor total a pagar de todos los usuarios 
print("\n", "=" * 40)
print(f"\tvalor total: ${totalConsumo:,.0f}") 

