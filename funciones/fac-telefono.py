def calcularValorImpulso(impulso):
    return 100 * impulso



def calcularTarifaBasica(estrato):
    if estrato ==1:
        return 10000
    elif estrato ==2:
        return 15000
    elif estrato ==3:
        return 20000
    elif estrato ==4:
        return 25000
    else:
        return 30000

def leerEstrato(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1 or n > 5: 
                print("Estrato invalido. ingrese del 1 al 5")
                continue
                return n 
        except ValueError:
            print("error al ingresar el estrato.")


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

def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("valor invalido. debe ser mayor a cero")
                return n
                
            break 
        except ValueError:
            print("error al ingresar el numero.")

    
n= leerInt("ingrese la cantidad de usuarios: ")
valtot = 0 
for i in range(1, n+1):
    print("\nDatos del usuario #", i)
    nombre = leerNombre("nombre? ")
    estrato = leerEstrato("estrato? ")
    impulso = leerInt("impulsos? ")
    valtbas = calcularTarifaBasica(estrato)
    valimpu = calcularValorImpulso(impulso)

    print("=" * 30)
    print("nombre:",nombre)
    print("valor a pagar:", valtbas+valimpu)
    print("tarifa basica:", valtbas)
    print("valor de impulsos:", valimpu)

    valtot += valtbas + valimpu

print("\n","*" * 30)
print("el valor total a pagar es:",valtot)
