# break 
# calcular si un numero es primo 
# num primo: divisible por si mismo y por 1 

num = int(input("ingrese un numero?"))

if num < 2: 
    print("No es primo ")
elif num == 2: 
    print("Es primo")
else: 
    esprimo = True # variables banderas o switch 
    for i in range(2, num):
        if num % i == 0: 
            esprimo = False 
            break

if esprimo == True: 
    print("Es primo")
else:
    print("No es primo. Lo divide", i) 


