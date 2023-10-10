while True:
    try:
        num1 = int(input("ingrese un numero"))
        break
    except ValueError:
        print("error. numero no valido")

        while True:
            try:
                num2 = int(input("ingrese un numero"))
                break
            except ValueError:
                    print("error. numero entero no valido")


try:
    num2 = "a"
    suma = num1 + num2
    print("la suma es: ", suma)
except Exception as e: 
     print("error al intentar sumar.\n", e )


    