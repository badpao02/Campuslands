s = "yo soy tu padre"
print(s[7])
print(s[-8])

# recorrer las cadenas 
# recorrido por indice 
for i in range(len(s)):
    print(s[i], end=", ")

# recorrido por elemento 
print("")
for e in s: 
    print(e, end=", ") 

#slice
print("") 
print(s[2:])
print(s[4:7])

# invertir cadena 
print(s[::-1])


# operador in 
print("tu" in s)
print("yt" not in s) 


# count = contar cuantas letras hay en una frase 
print(s.count("o")) 

# find encuentra la posicion de una letra o frase 
print(s.find("pa"))
print(s.find("ma"))

#isdigit () si la cadena es numerica o no 
snum = "100" 
print(snum.isdigit())
snum= "100a"

#isalnum es si es alfanumerico y no simbolos 

#split() divide y/o separa la frase por fracciones 
nombre = "juan daniel ramirez salazar"
email = "juandaniel@gamil.com" 
miles = "1.234.231"
print(nombre.split())
print(nombre.split("daniel")) 
print(email.split("@")) 
print(miles.split(".")) 

