#ejercicio
#hacer un programa que lea N estudiantes( nombre y nota). y nos muestre el promedio de la clase, el estudiante con mayor nota y el estudiante con la menor nota. 

def leerInt(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 1:
                print("valor invalido. debe ser mayor a cero")
                return n
                
            break 
        except ValueError:
            print("error al ingresar el numero.")


def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("nombre invalido")
                continue
                return nom 
        except Exception as e: 
            print("error al ingresar el nombre.", e)
            
def leerNota(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 0: 
                print("valor invalido debe ser mayor a cero")
                continue
                return n 
        except ValueError:
            print("error al ingresar el numero.")

n=leerInt("cuantos estudiantes son?")
lstNombres=[]
lstNotas=[]
for i in range(1, n+1):
    print("\nDatos del Estudiante #", i)
    lstNombres.append(leerNombre("nombre? ")) 
    lstNotas.append(leerNota("Nota?"))

#calcular y mostrar el promedio
    prom = sum(lstNotas) / n
    print("\n", "=" * 30) 
    print(" el promedio del curso es:". prom)

#encontrar y mostrar el estudiante con mayor nota 
NotaMayor = max(lstNotas)  # max es mostrar la nota mayor 
posEsrMayor = lstNotas.index(NotaMayor) 
nomEstMayoNota = lstNombres[posEsrMayor]

print("El EStudiante", nomEstMayoNota, "tiene la mayor nota:", NotaMayor)

#encontrar y mostrar el estudiante con menor nota 
NotaMenor = min(lstNotas)  # max es mostrar la nota mayor 
posEsrMenor = lstNotas.index(NotaMenor) 
nomEstMenorNota = lstNombres[posEsrMenor]
print("El EStudiante", nomEstMenorNota, "tiene la menor nota:", NotaMenor) 





