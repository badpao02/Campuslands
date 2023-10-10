# n = int(input("cuantos usuarios?"))
# estr = int(input("estrato [1 al 5]?"))
# nom = input("nombre?")
# con = float(input("consumo energia del mes [vol]?"))


# while estr: 

#  if estr == "1":  
#   tbas= 10.000  

#  elif estr == "2": 
#     tbas= 15.000 
#  elif estr == "3": 
#     tbas= 30.000 
#  elif estr == "4": 
#     tbas= 50.000 
#  elif estr == "5": 
#     tbas= 65.000 

# print("\n" "=" * 30)
# print("\tnombre: ", nom)
# print(f"\tvalor tarifa basica: ${tbas: ,}")
# print(f"\tvalor consumo: ${valcons:,.0f}")
# print(f"\tvalor de la factura de energia:")




#ejercicio 2 

ban = 1

# validar el nombreç
while True:
    try:
      nom = input("nombre?")
      nom = nom.strip()
      if nom == "" or nom.isalpha == False:
         print("Nombre invalido")
         continue
      break
    except Exception as e:
       print("Error al ingresar el nombre")

# validar el codigo
while True:
    try:
      nom = input("codigo?")
      nom = nom.strip()
      if nom == "" or nom.isalpha == False:
         print("codigo invalido")
         continue
      break
    except Exception as e:
       print("Error al ingresar el codigo")
# validar el programa academico

while True:
    try:
      cod = input("codigo?")
      programaAcademico = int(input(" si eres tecnico en sistemas pon 1, si eres tecnico en desarrollo de videojuegos pon 2, si eres tecnico en animacion digital pon 3 "))
      beca = int(input(" por rendimiento academico obtienes el 50% de valor matricula pon 1 , por beca cultural descuento del 40 % de matricula pon 2, presiona 3 no obtendras beca "))

      if len (programaAcademico) or programaAcademico.isalnum() == False  :  
        valorMatricula = 800000
        print("Nombre invalido. vuelva a digitarlo.")
      break
    except Exception as e:
        print("error al ingresar el nombre.\n", e)

        if beca == 1: 
           valorMatricula = valorMatricula - (valorMatricula * 0.50)
        elif beca == 2: 
           valorMatricula = valorMatricula - (valorMatricula * 0.40)
        else:
           valorMatricula = 800000
           
    if programaAcademico == 2:  
        valorMatricula = 1000000
        if beca == 1: 
           valorMatricula = valorMatricula - (valorMatricula * 0.50)
        elif beca == 2: 
           valorMatricula = valorMatricula - (valorMatricula * 0.40)
        else:
           valorMatricula = 1000000
   
    if programaAcademico == 3:  
        valorMatricula = 1200000
        if beca == 1: 
           valorMatricula = valorMatricula - (valorMatricula * 0.50)
        elif beca == 2: 
           valorMatricula = valorMatricula - (valorMatricula * 0.40)
        else:
           valorMatricula = 1200000
           
        
    print("\n" "=" * 10)
    print("\tnombre: ", nom)
    print(f"\tvalor matricula: ${valorMatricula: ,}")

    ban = int(input(" si deseas continuar ingresa 1 de lo contrario ingresa 2 "))
    if ban== 1: 
       ban= 1
    else: 
       ban= 2 
    
print(f"\tvalor total de la matricula:")

  