


import math 

num = int(input("digite un numero entero:"))

if num < 0:
    # num = -1 * num 
    num *= -1 


cantDig = math.floor(math.log10(num)) + 1 

print("la cantidad de digitos es:", cantDig)

