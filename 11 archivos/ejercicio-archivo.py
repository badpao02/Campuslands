fd = open("11 archivos/mbox-short.txt", "r")

# para hacer el ejercicio con listas y que no se repitan
emailListas = []
for linea in fd:
    if linea.startswith("From:"):
        emailListas.append(linea.split()[1])

fd.close()

cl = len(emailListas)
print("Cantidad de correos de origen distintos:", cl)

for email in emailListas:
    # comprueba si hay elementos repetidos
    while emailListas.count(email) > 1:
        # si es True, elimina todas las apariciones adicionales exepto 1
        emailListas.remove(email)

fd2 = open("11 archivos/correo.txt", "w")

for email in reversed(emailListas):
    envio = (f"{email} enviado [ok]")
    print(envio)
    fd2.write(envio + "\n")

fd2.close()