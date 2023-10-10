num = int(input("ingrese un numero"))
cpares= 0 
cimpares= 0 
while num != -1: 
    if num % 2 == 0: 
        print("el numero es par")
        cpares += 1 
    else: 
        print("el numero es impar")
        cimpares += 1 

    num = int(input("ingrese un numero: "))

print("\n", "=" * 30)
print("cantidad de numeros pares es: ", cpares)
print("cantidad de numeros impares es: ", cimpares) 





