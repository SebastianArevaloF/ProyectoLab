#VARIABLES

# Géneros de plantas
genero_e = ["1"] #SE DEFINEN LOS STRINGS RECONOCIBLES POR EL PROGRAMA
genero_c = ["2"] #GENERO E = GENERO EPIPREMNUM Y GENERO C = GENERO CORYPHANTA
generos_todos = "12" #SE ESCRIBEN TODOS LOS STRINGS DENTRO DE UN MISMO STRING PARA EVITAR PROBLEMAS

# Preguntas
pregunta_1 = "1"
pregunta_2 = "2" 
pregunta_3 = "3"
pregunta_4 = "4"
preguntas_todas = "1234" #SE ESCRIBEN TODOS LOS STRINGS DENTRO DE UN MISMO STRING PARA EVITAR PROBLEMAS 

#STRINGS AFIRMATIVOS Y NEGATIVOS
respuestas_afirmativas = ["SI"] 
respuestas_negativas = ["NO"]
respuestas_todas = ["SI","NO"]

#Alternativas
# Aquí van algunos strings que se repiten en los prints para no tener que escribirlos cada vez
# Generos
epi = "Epipremnum"
cory = "Coryphanta"
#info
info_1 = "Información de tu planta"
info_2 = "Cuando es optimo regarla"
info_3 = "Beneficios de tener la planta"
info_4 = "Cuidados para la planta"

#ENTRADAS

print("Hola!, esta app te podrá dar información sobre algunos generos de plantas , como sus cuidados, beneficios, etc.") #INICIO DEL PROGRAMA
print("Generos de plantas:")
print("1)", epi)
print("2)", cory)

planta_usuario = input("Por favor escriba el número de la alternativa deseada: ") #PRIMER INPUT PARA SABER DE QUE GENERO DESEA RECIBIR INFORMACION EL USUARIO


#PROCESAMIENTO

i = 0

while i == 0: #SE ESCRIBE UN CICLO WHILE QUE MANTENGA A TODO EL DESARROLLO, YA QUE ASI SI EL USUARIO QUIERE, PUEDE VOLVER A RESPONDER LA PREGUNTA SI QUIERE MAS INFORMACION

    while planta_usuario not in generos_todos: #SE ESCRIBEN 2 CICLOS WHILE POR SI EL USUARIO NO ESCRIBE EL NOMBRE DEL GENERO DE SU PLANTA CORRECTAMENTE
        print(("Quizas quisiste escribir 1 o 2"))
        print("1)", epi)
        print("2)", cory)
        planta_usuario = input("Por favor ingresar su alternativa otra vez: ")

    if planta_usuario == "1":
    	print("El género escogido fue:", epi)
    else:
        print("El género escogido fue:", cory)
	
	# Sección de información
    print("Te podemos brindar:")
    print("1)", info_1)
    print("2)", info_2)
    print("3)", info_3)
    print("4)", info_4)
    preguntas = input("Por favor escribir el número de la alternativa según la informacíon que le gustaría recibir: ")

    while preguntas not in preguntas_todas:
        print("Quizás quisiste ingresar 1, 2, 3 o 4.")
        preguntas = input("Por favor ingresar su respuesta nuevamente:  ")
    
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
        elif preguntas in pregunta_3:
           print("Este puntiagudo genero de plantas, son excelentes purificadores de aire, siendo esto perfecto a la hora de cuidar nuestra salud, tambien son plantas que requieren muy poco cuidado debido a su poca necesidad de agua, siendo estas perfectas para gente que no puede dedicar todo su tiempo en una planta!")
        elif preguntas in pregunta_4:
            print("A esta pequeña planta, le encanta tener luz directa, aunque tambien pueden recibir por periodos causando el mismo efecto de estar todo el dia en la luz solar!, la tierra organica mezclada con fibra de coco, hojas secas, corteza y turba, es lo mejor para su perfecto desarrollo!")

    mas_preguntas = input("¿Le gustaría saber más? (Si/No): ")
    mas_preguntas = mas_preguntas.upper()
    
    while mas_preguntas not in respuestas_todas:
        print("Por favor ingresar una respuesta valida") 
        mas_preguntas = input("¿Le gustaría saber más? (Si/No):")
    if mas_preguntas in respuestas_negativas:
        print("Esperamos que le haya servido y ayudado la informacion!")
        i = i + 1
