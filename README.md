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

genero_e = ["Epipremnum","epipremnum"] #SE DEFINEN LOS STRINGS RECONOCIBLES POR EL PROGRAMA 

genero_c = ["Coryphanta","coryphanta"] #GENERO E = GENERO EPIPREMNUM Y GENERO C = GENERO CORYPHANTA

pregunta_1 = ["Informacion de mi planta","informacion de mi planta","Informacion de mi Planta","Informacion","informacion","informasion de mi planta","Informacion De Mi Planta","Informacion de mi planta."]
pregunta_2 = ["Cuando es optimo regarla","cuando es optimo regarla","cuando es optimo regar mi planta","Cuando es optimo reglar mi planta"]
pregunta_3 = ["Beneficios de mi planta","beneficios de mi planta","beneficios que me da mi planta","Beneficios que me da mi planta"]
pregunta_4 = ["Cuidados de mi planta","cuidados de mi planta","cuidado de mi planta","Cuidado de mi planta"]  #SE DEFINEN LOS STRINGS RECONOCIBLES PARA RESPONDER LO QUE DESEA EL USUARIO

#ENTRADAS

print("Hola!, el genero de plantas de las que se posee informacion son son Epipremnum y Coryphanta")

planta_usuario = input("Ingrese el genero de su planta: ") 

while planta_usuario not in (genero_c and genero_e): #SE ESCRIBE UN CICLO WHILE POR SI EL USUARIO NO ESCRIBE EL NOMBRE DEL GENERO DE SU PLANTA CORRECTAMENTE
    planta_usuario = input("Quizas quisiste escribir Epipremnum o Coryphanta, que deseas escribir?: ")

#PROCESAMIENTO
    
preguntas = input("Esta aplicacion te puede dar informacion de tu planta, cuando es optimo regarla, beneficios de tenerla o cuidados, que te gustaria recibir?: ")

while preguntas not in (pregunta_1 or pregunta_2 or pregunta_3 or pregunta_4): #SE ESCRIBE UN CICLO WHILE POR SI EL USUARIO NO ESCRIBE LA PREGUNTA CORRECTAMENTE
    preguntas = input("Quizas quisiste escribir una pregunta que no podemos responder, por favor haz otra!")

if planta_usuario in genero_e: #SE ESCRIBE UN CONDICIONAL PARA RESPONDER LAS PREGUNTAS SEGUN EL GENERO QUE ESCRIBIO EL USUARIO
    if preguntas in pregunta_1:
        print("La Epipremnum, tambien conocida como potos, perteneciente a la familia Araceae, puede tener tallos de hasta 4cm de diámetro!, esta no florece de manera natural, si no, de manera inducida.")
    elif preguntas in pregunta_2:
        print("Los riegos deben ser frecuentes en la epoca calida (manteniendo humedad alta rociando las hojas y se deben reducir a partir de otoño, en invierno se deben mantener escasos, la temperatura ideal del agua para regarla son los 20°C a 25°C")
    elif preguntas in pregunta_3:
        print("Este genero de plantas, es perfecto para poder decorar cualquier parte de tu casa, como también ayuda considerablemente a eliminar muchas de las toxinas del aire que no podemos apreciar a simple vista!")
    elif preguntas in pregunta_4:
        print("A esta curiosa planta, le gusta mucho mantenerse en un ambiente humedo, es por esto que siempre debes manter la tierra de esa manera!, evita mantenerla a luz directa del sol ya que esto no le gusta, mantenla cerca de la ventana evitando lo anterior dicho!")

else:
if planta_usuario in genero_c: #SE ESCRIBE UN CONDICIONAL PARA RESPONDER LAS PREGUNTAS SEGUN EL GENERO QUE ESCRIBIO EL USUARIO
    if preguntas in pregunta_1:
        
    elif preguntas in pregunta_2:
        
    elif preguntas in pregunta_3:
        
    elif preguntas in pregunta_4:
