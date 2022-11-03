# FUNDAMENTOS DE PROGRMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
# GRUPO: 2
# INTEGRANTES
# 1. Sebastián Arévalo Farías 21.224.453-8
# 2. César Rodríguez Pardo 21.382.225-K
# 3. Benjamín Navarro Rejas 21.331.312-6
# 4. Benjamín Zúñiga Jofré 21.337.525-3
# DESCRIPCIÓN DEL PROGRAMA 

#CONSTANTES

plantas = ["Epipremnum","epipremnum","Coryphanta","coryphanta"]

#ENTRADAS

print("Hola!, las plantas trabajadas en este programa son Epipremnum y Coryphanta")

planta_usuario = input("Ingrese el nombre de su planta: ")

while planta_usuario not in plantas:
    planta_usuario = input("Quizas quisiste escribir Epipremnum o Coryphanta, que deseas escribir?: ")

#PROCESAMIENTO

if planta_usuario == "Epipremnum" or "epipremnum":
    print("Recuerda que este genero de plantas debe encontrarse en su temperatura ideal para su buen desarrollo y cuidado, este debe ser entre 16°C a 21°C")
    
if planta_usuario == "Coryphanta" or "coryphanta":
    print("Recuerda que este genero de plantas debe encontrarse en su temperatura ideal para su buen desarrollo y cuidado, este debe ser entre 20°C a 35°C")
    
grados = input("Cual es la temperatura actual?: ")
