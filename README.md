# FUNDAMENTOS DE PROGRMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
# GRUPO: 2
# INTEGRANTES
# 1.
# 2.
# 3.
# 4. Benjamín Zúñiga Jofré 21.337.525-3
# DESCRIPCIÓN DEL PROGRAMA 

# ENTRADAS
planta = input("Ingrese el tipo de planta: ") 
temperatura = int(input("Ingresar grados: "))

# PROCESAMIENTO

if planta == "coryphanta":
    if 25 > temperatura > 15:
        hora_riego = "8 de la tarde"
    if temperatura < 15:
        hora_riego = "No regar hoy"
# SALIDAS
