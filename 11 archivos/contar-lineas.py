fd = open("11 archivos/mbox-short.txt", "r")

cl = 0
cp = 0 
for linea in fd:

    linea = linea.strip()
   #cp += len(linea.split(" "))
    for lin in linea.split(" "):
        if lin.isalnum():
        #cp += 1    
            cl += 1
   

fd.close()

print("cantidad de lineas:", cl)

