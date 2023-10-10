def suma(num1, num2):
    resultado = num1 + num2
    return resultado 

def resta(num1, num2):
    return num1 - num2 

def multiplicacion(num1, num2):
    return num1 * num2 

def division(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        resultado = None
    return resultado 

def menu():
    while True:
        try:
            print("*** MENU CALCULADORA***")
            print("1 sumar")
            print("2 restar")
            print("3 multiplicar")
            print("4 dividir")
            print("5. salir")
            op = int(input(">>> opcion (1-5)? ")) 
            if op < 1 or op > 5:
                print("opcion no valida. escoja de 1 a 5")
                input("presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("opcion no valida. escoja de 1 a 5")
            input("presione cualquier tecla para continuar ... ")

        return op

def leernum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num 
        except ValueError:
            print("Error. numero invalido")
            input("presione cualquier tecla para continuar...")

    pass 

    ## programa principal
while True: 
    opcion = menu()
    num1 = leernum("ingrese el primer numero")
    num2 = leernum("ingrese el segundo numero")  
    
    if opcion ==1:
        print("\n\n1. sumar")
        num1 = leernum("ingrese el primer numero")
        num2 = leernum("ingrese el segundo numero")
        print(f"el resultado de la suma es:{suma(num1, num2):.3f}")
    
    elif opcion == 2:
        print("\n\n2.Restar")
        num1 = leernum("ingrese el primer numero")
        num2 = leernum("ingrese el segundo numero")
        print(f"el resultado de la resta es:{resta(num1, num2):.3f}") 

    elif opcion == 3:
        print("\n\n3.multiplicar")
        num1 = leernum("ingrese el primer numero")
        num2 = leernum("ingrese el segundo numero")
        print(f"el resultado de la ,multiplicacion es:{multiplicacion(num1, num2):.3f}")
        
    elif opcion == 4:
        print("\n\n4.dividir")
        res= division(num1, num2)
        if res != None:
            num1 = leernum("ingrese el primer numero")
            num2 = leernum("ingrese el segundo numero")
     

        print(f"el resultado de la division es:{res:.3f}")
        
    elif opcion == 5:
        print("\n\n gracias por usar la calculadora")
        print("adios")
        input("presione cualquier tecla para continuar...")
        break
    input("presione cualquier tecla para volver al menu...")
