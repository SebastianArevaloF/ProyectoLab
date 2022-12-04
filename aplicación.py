#CONSTANTES
'''
Para la simplificacion de cada variable relacionada al dialogo del robot, se escribira
dialogo_ventana_NUMERO DE LA VENTANA_NUMERO DE DIALOGO, si es una ventana de un genero
se escribira dialogo_robot_x_y, siendo x la primera letra del genero e y el numero de dialogo
'''
#IMPORTACION DE FUNCIONES
from tkinter import Tk, Label, Button #Se importa el modulo tkinter, con respectivas fucniones para desarrollo de interfaz

#DEFINICION DE FUNCIONES

#PROCESAMIENTO
#VENTANA PRINCIPAL
ventana_principal = Tk()
ventana_principal.title("Aplicación")
ventana_principal.geometry("360x660")
#BIENVENIDA Y DIALOGOS DEL ROBOT EN VENTANA PRINCIPAL
bienvenida = Label(ventana_principal,text="Hola!, bienvenido a NOMBRE APP")
bienvenida.place(x=80,y=30,width=200,height=25)

dialogo_robot_1_1 = Label(ventana_principal,text="Soy, NOMBRE ROBOT")
dialogo_robot_1_1.place(x=80,y=60,width=200,height=25)

dialogo_robot_1_2 = Label(ventana_principal,text="Estoy aquí para ayudarte en el cuidado de tu planta")
dialogo_robot_1_2.place(x=-65,y=90,width=500,height=25)

dialogo_robot_1_3 = Label(ventana_principal,text="¿Te gustaría continuar?")
dialogo_robot_1_3.place(x=80,y=300,width=200,height=25)


#SEGUNDA VENTANA
def segunda_ventana():
    segunda_ventana = Tk()
    segunda_ventana.title("Aplicación")
    segunda_ventana.geometry("360x660")

    dialogo_robot_2_1 = Label(segunda_ventana,text="Poseo informacion de los siguientes géneros de plantas")
    dialogo_robot_2_1.place(x=35,y=10,width=300,height=25)

    dialogo_robot_2_2 = Label(segunda_ventana,text="¿Cual te gustaria seleccionar?")
    dialogo_robot_2_2.place(x=80,y=30,width=200,height=25)

    def epipremnum_ventana(): #SE DEFINE UNA FUNCION PARA LA VENTANA DEL GENERO EN ESPECIFICO Y 4 EXTRAS DENTRO DE LA YA MENCIONADA, ASÍ PARA DAR PASO A LA VENTANA DE INFORMACION QUE PUEDA DESEAR EL USUARIO
        epipremnum_ventana = Tk()
        epipremnum_ventana.title("Aplicación")
        epipremnum_ventana.geometry("360x660")
        segunda_ventana.withdraw()
        dialogo_robot_e_1 = Label(epipremnum_ventana,text="¿Qué te gustaría saber?")
        dialogo_robot_e_1.place(x=80,y=20,width=200,height=25)
        
        def riego_e_ventana():
            riego_e_ventana = Tk()
            riego_e_ventana.title("Aplicación")
            riego_e_ventana.geometry("360x660")
            epipremnum_ventana.withdraw()
            dialogo_robot_e_2 = Label(riego_e_ventana,text="Los riegos deben ser frecuentes en la epoca cálida,\n"
            "manteniendo humedad alta rociando las hojas y se deben reducir\n"
            "a partir de otoño, en invierno se deben mantener escasos,\n"
            "la temperatura ideal del agua pararegarla son los 20°C a 25°C")
            dialogo_robot_e_2.place(x=80,y=20,width=200,height=25)
            
        def info_e_ventana():
            info_e_ventana = Tk()
            info_e_ventana.title("Aplicación")
            info_e_ventana.geometry("360x660")
            epipremnum_ventana.withdraw()
            dialogo_robot_e_3 = Label(info_e_ventana,text="La Epipremnum, tambien conocida como potos,\n \
            perteneciente a la familia Araceae\n"
            "puede tener tallos de hasta 4cm de diámetro!,\n \
            esta no florece de manera natural,"
            "si no, de manera inducida.")
            dialogo_robot_e_3.place(x=80,y=20,width=500,height=250)
            
        def beneficios_e_ventana():
            beneficios_e_ventana = Tk()
            beneficios_e_ventana.title("Aplicación")
            beneficios_e_ventana.geometry("360x660")
            epipremnum_ventana.withdraw()
            dialogo_robot_e_4 = Label(beneficios_e_ventana,text="Este genero tan curioso de plantas,\
            es perfecto para poder decorar\n"
            "cualquier parte de tu casa, como también ayuda\n"
            "considerablemente a eliminar muchas de las toxinas del aire\n"
            "que no podemos apreciar a simple vista!")
            dialogo_robot_e_4.place(x=80,y=20,width=200,height=25)
            
        def cuidados_e_ventana():
            cuidados_e_ventana = Tk()
            cuidados_e_ventana.title("Aplicación")
            cuidados_e_ventana.geometry("360x660")
            epipremnum_ventana.withdraw()
            dialogo_robot_e_5 = Label(cuidados_e_ventana,text="A esta curiosa planta, le gusta mucho mantenerse en un\n"
            "ambiente humedo, es por esto que siempre debes manter la tierra\n"
            "de esa manera,evita mantenerla a \
            luz directa del sol ya que esto\n"
            "no le gusta, mantenla cerca de la ventana \
            evitando lo anterior dicho")
            dialogo_robot_e_5.place(x=80,y=20,width=200,height=25)

        boton_e_riego = Button(epipremnum_ventana,text="¿Cómo regar esta planta?",command=riego_e_ventana)
        boton_e_riego.place(x=115,y=55,width=139,height=25)

        boton_e_info = Button(epipremnum_ventana,text="Información sobre esta planta",command=info_e_ventana)
        boton_e_info.place(x=100,y=115,width=165,height=25)

        boton_e_beneficios = Button(epipremnum_ventana,text="Beneficios de tener esta planta",command=beneficios_e_ventana)
        boton_e_beneficios.place(x=100,y=175,width=167,height=25)

        boton_e_cuidados = Button(epipremnum_ventana,text="Cuidados de esta planta",command=cuidados_e_ventana)
        boton_e_cuidados.place(x=115,y=235,width=133,height=25)

    def coryphanta_ventana():
        coryphanta_ventana = Tk()
        coryphanta_ventana.title("Aplicación")
        coryphanta_ventana.geometry("360x660")
        segunda_ventana.withdraw()
        dialogo_robot_c_1 = Label(coryphanta_ventana,text="¿Qué te gustaría saber?")
        dialogo_robot_c_1.place(x=80,y=20,width=200,height=25)

        def riego_c_ventana():
            riego_c_ventana = Tk()
            riego_c_ventana.title("Aplicación")
            riego_c_ventana.geometry("360x660")
            coryphanta_ventana.withdraw()
            dialogo_robot_c_2 = Label(riego_c_ventana,text="Los riegos deben ser de forma moderada en primavera\n"
            "y verano, siempre manteniendo el suelo seca de esta misma,\n"
            "en la epoca fria, los riegos deben suspenderse\n"
            "en pos del cuidado de la planta")
            dialogo_robot_c_2.place(x=80,y=20,width=200,height=25)
            
        def info_c_ventana():
            info_c_ventana = Tk()
            info_c_ventana.title("Aplicación")
            info_c_ventana.geometry("360x660")
            coryphanta_ventana.withdraw()
            dialogo_robot_c_3 = Label(info_c_ventana,text="¿La Coryphanta, tambien conocida como cactus,\n"
            "es un genero nativo de Mexico, siendo uno de los mas extensos.\n"
            "Esta puede crecer aproximadamente de 5-6 cm,\n"
            "cuando se desarrolla forma una flor central grande")
            dialogo_robot_c_3.place(x=80,y=20,width=200,height=25)
            
        def beneficios_c_ventana():
            beneficios_c_ventana = Tk()
            beneficios_c_ventana.title("Aplicación")
            beneficios_c_ventana.geometry("360x660")
            coryphanta_ventana.withdraw()
            dialogo_robot_c_4 = Label(beneficios_c_ventana,text="Este puntiagudo genero de plantas, son excelentes\n"
            "purificadores de aire, siendo esto perfecto a la hora de\n"
            "cuidar nuestra salud, tambien son plantas que requieren\n"
            "muy poco cuidado debido a su poca necesidad de agua,\n"
            "siendo estas perfectas para gente que no puede dedicar\n"
            "todo su tiempo en una planta")
            dialogo_robot_c_4.place(x=80,y=20,width=200,height=25)
            
        def cuidados_c_ventana():
            cuidados_c_ventana = Tk()
            cuidados_c_ventana.title("Aplicación")
            cuidados_c_ventana.geometry("360x660")
            coryphanta_ventana.withdraw()
            dialogo_robot_c_5 = Label(cuidados_c_ventana,text="A esta pequeña planta, le encanta tener luz directa,\n"
            "aunque tambien pueden recibir por periodos causando el mismo\n"
            "efecto de estar todo el dia en la luz solar,\n"
            "la tierra organica mezclada con fibra de coco,\n"
            "hojas secas, corteza y turba,\
            es lo mejor para su perfecto desarrollo")
            dialogo_robot_c_5.place(x=80,y=20,width=200,height=25)
            

        boton_c_riego = Button(coryphanta_ventana,text="¿Cómo regar esta planta?",command=riego_c_ventana)
        boton_c_riego.place(x=115,y=55,width=139,height=25)

        boton_c_info = Button(coryphanta_ventana,text="Información sobre esta planta",command=info_c_ventana)
        boton_c_info.place(x=100,y=115,width=165,height=25)

        boton_c_beneficios = Button(coryphanta_ventana,text="Beneficios de tener esta planta",command=beneficios_c_ventana)
        boton_c_beneficios.place(x=100,y=175,width=167,height=25)

        boton_c_cuidados = Button(coryphanta_ventana,text="Cuidados de esta planta",command=cuidados_c_ventana)
        boton_c_cuidados.place(x=115,y=235,width=133,height=25)
        
    boton_epipremnum = Button(segunda_ventana,text="Género Epipremnum",command=epipremnum_ventana)
    boton_epipremnum.place(x=120,y=100,width=125,height=25)

    boton_coryphanta = Button(segunda_ventana,text="Género Coryphanta",command=coryphanta_ventana)
    boton_coryphanta.place(x=120,y=150,width=125,height=25)

    ventana_principal.withdraw()
    
#BOTON CONTINUAR VENTANA PRINCIPAL
boton_continuar = Button(ventana_principal,text="Continuar",command=segunda_ventana)
boton_continuar.place(x=130,y=330,width=100,height=25)
    
ventana_principal.mainloop()
