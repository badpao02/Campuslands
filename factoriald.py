# calcular el factorial de un numero 
#factorial de 5 = 1 * 2 * 3 * 4 * 5 = 120

n = int(input("numero?"))

fact = 1 
for i in range(1, n+1): 
    fact *= i # fact = * i 

print(f"el factorial de {n} es {fact:,}") 
 