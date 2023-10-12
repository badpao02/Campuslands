fd = open("11 archivos/nombres.txt","r")


fd2 = open("11 archivos/nombres-bak.txt","w")


for linea in fd:
    print(linea, end="")



fd2.close()
fd.close()
