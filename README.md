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
# El programa puede entregar informacion diversa, como cuidados, beneficios, etc., de 2 (a expandir si alcanza el tiempo) géneros específico de planta (Epipremnum y Coryphanta).

#CONSTANTES

genero_e = ["Epipremnum","epipremnum"] #SE DEFINEN LOS STRINGS RECONOCIBLES POR EL PROGRAMA 
genero_c = ["Coryphanta","coryphanta"] #GENERO E = GENERO EPIPREMNUM Y GENERO C = GENERO CORYPHANTA
generos_todos = ["Coryphanta","coryphanta","Epipremnum","epipremnum"] #SE ESCRIBEN TODOS LOS STRINGS DENTRO DE UN MISMO STRING PARA EVITAR PROBLEMAS

pregunta_1 = ["Informacion de mi planta","informacion de mi planta","Informacion de mi Planta","Informacion","informacion","informasion de mi planta","Informacion De Mi Planta","Informacion de mi planta."]
pregunta_2 = ["Cuando es optimo regarla","cuando es optimo regarla","cuando es optimo regar mi planta","Cuando es optimo reglar mi planta"] #SE DEFINEN LOS STRINGS RECONOCIBLES PARA RESPONDER LO QUE DESEA EL USUARIO, P1,P2,P3 O P4.
pregunta_3 = ["Beneficios de mi planta","beneficios de mi planta","beneficios que me da mi planta","Beneficios que me da mi planta","Beneficios","beneficios"]
pregunta_4 = ["Cuidados de mi planta","cuidados de mi planta","cuidado de mi planta","Cuidado de mi planta"]  
preguntas_todas = ["Informacion de mi planta","informacion de mi planta","Informacion de mi Planta","Informacion","informacion","informasion de mi planta", #SE ESCRIBEN TODOS LOS STRINGS DENTRO DE UN MISMO STRING PARA EVITAR PROBLEMAS
                   "Informacion De Mi Planta","Informacion de mi planta.","Cuando es optimo regarla","cuando es optimo regarla","cuando es optimo regar mi planta",
                   "Cuando es optimo reglar mi planta","Beneficios de mi planta","beneficios de mi planta","beneficios que me da mi planta","Beneficios que me da mi planta",
                   "Beneficios","beneficios","Cuidados de mi planta","cuidados de mi planta","cuidado de mi planta","Cuidado de mi planta"]

respuestas_afirmativas = ["Si","si"] #STRINGS AFIRMATIVOS Y NEGATIVOS
respuestas_negativas = ["No","no"]

#ENTRADAS

print("Hola!, esta app te dará información sobre generos de plantas que tu desees, como cuidados, beneficios, etc., Siendo estos el genero de plantas: Epipremnum y Coryphanta") #INICIO DEL PROGRAMA

planta_usuario = input("Escriba el genero de plantas deseado para obtener diversa informacion: ") #PRIMER INPUT PARA SABER DE QUE GENERO DESEA RECIBIR INFORMACION EL USUARIO

#PROCESAMIENTO

while planta_usuario not in generos_todos: #SE ESCRIBEN 2 CICLOS WHILE POR SI EL USUARIO NO ESCRIBE EL NOMBRE DEL GENERO DE SU PLANTA CORRECTAMENTE
    planta_usuario = input("Quizas quisiste escribir Epipremnum o Coryphanta, que deseas escribir?: ")

preguntas = input("Esta aplicacion te puede dar informacion de tu planta, cuando es optimo regarla, beneficios de tenerla o cuidados, que te gustaria recibir?: ")

while preguntas not in preguntas_todas:
    preguntas = input("Escribiste algo que aun no podemos procesar, por favor escribe otra cosa!: ")

#SALIDA

if planta_usuario in genero_e: #SE ESCRIBEN 2 CONDICIONALES PARA RESPONDER LAS PREGUNTAS SEGUN EL GENERO QUE ESCRIBIO EL USUARIO
    if preguntas in pregunta_1:
        print("La Epipremnum, tambien conocida como potos, perteneciente a la familia Araceae, puede tener tallos de hasta 4cm de diámetro!, esta no florece de manera natural, si no, de manera inducida.")
    elif preguntas in pregunta_2:
        print("Los riegos deben ser frecuentes en la epoca calida (manteniendo humedad alta rociando las hojas y se deben reducir a partir de otoño, en invierno se deben mantener escasos, la temperatura ideal del agua para regarla son los 20°C a 25°C")
    elif preguntas in pregunta_3:
        print("Este genero tan curioso de plantas, es perfecto para poder decorar cualquier parte de tu casa, como también ayuda considerablemente a eliminar muchas de las toxinas del aire que no podemos apreciar a simple vista!")
    elif preguntas in pregunta_4:
        print("A esta curiosa planta, le gusta mucho mantenerse en un ambiente humedo, es por esto que siempre debes manter la tierra de esa manera!, evita mantenerla a luz directa del sol ya que esto no le gusta, mantenla cerca de la ventana evitando lo anterior dicho!")

if planta_usuario in genero_c:
    if preguntas in pregunta_1:
        print("La Coryphanta, tambien conocida como cactus, es un genero nativo de Mexico, siendo uno de los mas extensos. Esta puede crecer aproximadamente de 5-6 cm, cuando se desarrolla forma una flor central grande!")
    elif preguntas in pregunta_2:
        print("Los riegos deben ser de forma moderada en primavera y verano, siempre manteniendo el suelo seca de esta misma, en la epoca fria, los riegos deben suspenderse en pos del cuidado de la planta")
    elif preguntas in pregunta_3
        print("Este puntiagudo genero de plantas, son excelentes purificadores de aire, siendo esto perfecto a la hora de cuidar nuestra salud, tambien son plantas que requieren muy poco cuidado debido a su poca necesidad de agua, siendo estas perfectas para gente que no puede dedicar todo su tiempo en una planta!")
    elif preguntas in pregunta_4
        print("A esta pequeña planta, le encanta tener luz directa, aunque tambien pueden recibir por periodos causando el mismo efecto de estar todo el dia en la luz solar!, la tierra organica mezclada con fibra de coco, hojas secas, corteza y turba, es lo mejor para su perfecto desarrollo!")
