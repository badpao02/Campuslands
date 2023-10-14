# calcular el indice promedio de spam 

fd = open("11 archivos/trabajo-simul.txt/mbox.txt", "r")

spamLst = []

for linea in fd:
    if linea.startswith("From:"):
        spamLst.append(linea.split()[1])

fd.close()

cl = len(spamLst)
print("calcular el promedio de spam del servidor :", cl)

for spam in spamLst:
    # comprueba si hay elementos repetidos
    while spamLst.count(spam) > 1:
        # si es True, elimina todas las apariciones adicionales exepto 1
        spamLst.remove(spam)

fd2 = open("11 archivos/trabajo-simul.txt/mbox.txt", "w")

for spam in reversed(spamLst):
    envio = (f"{spam} enviado [ok]")
    print(envio)
    fd2.write(envio + "\n")

fd2.close()
