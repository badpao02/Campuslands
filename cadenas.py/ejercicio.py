# num = input("ingrese el numero")

# if num.startswith("+") and num.count("-") == 2:
#     partes = num.split("-")
#     print("el telefono es:", partes[1] )

# else: 
#     print("error.el numero no cumple con el formato") 
# ("")

#ejercicio 2
# s = input("digita la palabra")   
# if s == s[::-1]:
#     print("es palindroma")
# else:
#     print("no es palindroma")

# #ejercicio 3

# fecha = input("digita su fecha de nacimiento")
# partes = fecha.split("/") 
# valido = True
# if len(partes[0]) == 2 and \
#         len(partes[1]) == 2 and\
#         len(partes[2]) == 4:
            

#     valido = True 
#     for p in partes: 
#         if not p.isdigit():
#             valido = False
#             break

#     if valido: 
#         print(f"dia: {partes[0]}, mes: {partes[1]}, año: {partes[2]}")
#     else:
#         print("formato no valido")

# else:
#     print("formato no valido") 

 #ejercicio 4 

s= ("escribe los caracteres"["a-z"])

for i in range (len(s)):
 print(s[i])





