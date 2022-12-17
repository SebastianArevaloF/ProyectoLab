# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: L-19
# PROFESOR DE TEORÍA: Gery Simken, Alejandro Cisterna
# PROFESOR DE LABORATORIO: Gery Gerena
# GRUPO: 2
# INTEGRANTES
# 1. Sebastián Arévalo Farías 21.224.453-8
# 2. Benjamín Navarro Rejas 21.331.312-6
# 3. Benjamín Zúñiga Jofré 21.337.525-3
# 4. César Rodríguez Pardo 21.382.225-K
# El programa puede entregar:
# informacion diversa, como cuidados, beneficios, etc.,
# de 4 géneros específico de plantas
# (Epipremnum,Coryphanta,Ficus y Aloe).

# CONSTANTES
RIEGO_E = ("Los riegos deben ser frecuentes en la\n"
           "epoca cálida manteniendo humedad alta\n"
           "rociando las hojas y se deben reducir\n"
           "a partir de otoño, en invierno se deben\n"
           "mantener escasos la temperatura ideal\n"
           "del agua pararegarla son los 20°C a 25°C.")
INFOR_E = ("La Epipremnum, tambien conocida como\n"
           "potos, perteneciente a la familia Araceae\n "
           "puede tener tallos dehasta 4cm de diámetro,\n"
           "esta no florece de manera natural, si no,\n"
           "de manera inducida.")
BENEFI_E = ("Este genero tan curioso de plantas\n"
            "es perfecto para poder decorar cualquier\n"
            "parte de tu casa, como también ayuda\n "
            "considerablemente a eliminar de las\n"
            "toxinas de aire que no podemos apreciar\n"
            "a simple vista.")
CUIDAD_E = ("A esta curiosa planta, le gusta mucho\n"
            "mantenerse en un ambiente humedo,\n"
            "evita mantenerla a luz directa del sol\n"
            "ya que esto no le gusta, mantenla cerca\n"
            "de la ventana evitando lo anterior dicho.")
'''
Para la simplificacion de cada variable relacionada al dialogo
Se especificaran las siguientes indicaciones:
1)Para el dialogo del robot, se escribira
dialogo_robot_"NUMERO DE LA VENTANA"_"NUMERO DE DIALOGO"
2)Para el dialogo del robot hablando sobre plantas
Se escribira dialogo_robot_x_y,
Siendo x la primera letra del genero e y el numero de dialogo
'''
# IMPORTACION DE FUNCIONES
# Se importa el modulo tkinter, con respectivas funiones
# para desarrollo de interfaz
from tkinter import Tk, Label, Button
# Se importa el modulo PIL, para imagenes
from PIL import Image, ImageTk
# DEFINICION DE FUNCIONES

# PROCESAMIENTO
# VENTANA PRINCIPAL
ventana_principal = Tk()
ventana_principal.title("Aplicación")
ventana_principal.geometry("360x660")
ventana_principal.resizable(width=False, height=False)
# CAMBIOS DE COLORES PARA LA VENTANA PRINCIPAL
ventana_principal.config(bg="yellow green")

# CAMBIO DE ICONO DE LA APP POR DEFINIR

# BIENVENIDA Y DIALOGOS DEL ROBOT EN VENTANA PRINCIPAL
bienvenida = Label(ventana_principal, text="Hola! bienvenido a EcoAqua",
                   font=30)
bienvenida.config(bg="dark sea green")
bienvenida.place(anchor="c", relx=0.5, y=30, width=200, height=25)

dialogo_robot_1_1 = Label(ventana_principal, text="Soy Coryphanter 3000",
                          font=30)
dialogo_robot_1_1.place(anchor="c", relx=0.5, y=60, width=175, height=25)
dialogo_robot_1_1.config(bg="dark sea green")

dialogo_robot_1_2 = Label(ventana_principal,
                          text="Estoy aquí para ayudarte\n"
                               "en el cuidado de tu planta",
                          font=30)
dialogo_robot_1_2.place(anchor="c", relx=0.5, y=95, width=250, height=40)
dialogo_robot_1_2.config(bg="dark sea green")

dialogo_robot_1_3 = Label(ventana_principal, text="¿Te gustaría continuar?",
                          font=30)
dialogo_robot_1_3.place(anchor="c", relx=0.5, y=300, width=250, height=25)
dialogo_robot_1_3.config(bg="dark sea green")

# SEGUNDA VENTANA


def ventana_2():
    segunda_ventana = Tk()
    segunda_ventana.title("Aplicación")
    segunda_ventana.geometry("360x660")
    segunda_ventana.config(bg="yellow green")

    dialogo_robot_2_1 = Label(segunda_ventana,
                              text="Poseo informacion de los siguientes\n"
                                   "géneros de plantas",
                              font=35)
    dialogo_robot_2_1.place(anchor="c", relx=0.5, y=35, width=280, height=45)
    dialogo_robot_2_1.config(bg="dark sea green")
    dialogo_robot_2_2 = Label(segunda_ventana,
                              text="¿Cual te gustaria seleccionar?", font=35)
    dialogo_robot_2_2.place(anchor="c", relx=0.5, y=75, width=220, height=25)
    dialogo_robot_2_2.config(bg="dark sea green")

    numero_pagina = Label(segunda_ventana, text="1/2")
    numero_pagina.config(bg="dark sea green")
    numero_pagina.place(x=0, y=0, width=30, height=20)

# SE DEFINE UNA FUNCION PARA LA VENTANA DEL GENERO EN ESPECIFICO Y 4 EXTRAS
# DENTRO DE LA YA MENCIONADA, ASÍ PARA DAR PASO A LA VENTANA DE INFORMACION
# QUE PUEDA DESEAR EL USUARIO
    def epipremnum_ventana():
        epipremnum_ventana = Tk()
        epipremnum_ventana.title("Aplicación")
        epipremnum_ventana.geometry("360x660")
        segunda_ventana.withdraw()

        dialogo_robot_e_1 = Label(epipremnum_ventana,
                                  text="¿Qué te gustaría saber?")
        dialogo_robot_e_1.config(bg="dark sea green")
        dialogo_robot_e_1.place(x=120, y=20, width=130, height=25)

        boton_atras = Button(epipremnum_ventana,
                             text="Atrás",
                             command=lambda: [epipremnum_ventana.destroy(),
                                              segunda_ventana.deiconify()])
        boton_atras.config(bg="dark khaki")
        boton_atras.place(x=0, y=638, width=50, height=25)

        boton_cerrar = Button(epipremnum_ventana,
                              text="Cerrar",
                              command=lambda: [epipremnum_ventana.destroy(),
                                               segunda_ventana.destroy(),
                                               ventana_principal.destroy()])
        boton_cerrar.config(bg="light coral")
        boton_cerrar.place(x=310, y=640, width=50, height=25)
        epipremnum_ventana.config(bg="yellow green")

        def riego_e_ventana():
            riego_e_ventana = Tk()
            riego_e_ventana.title("Aplicación")
            riego_e_ventana.geometry("360x660")
            riego_e_ventana.config(bg="yellow green")
            epipremnum_ventana.withdraw()

            dialogo_robot_e_2 = Label(riego_e_ventana, text=RIEGO_E, font=20)
            dialogo_robot_e_2.config(bg="dark sea green")
            dialogo_robot_e_2.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)
            boton_atras = Button(riego_e_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [riego_e_ventana.destroy(),
                                  epipremnum_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(riego_e_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [riego_e_ventana.destroy(),
                                   epipremnum_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def info_e_ventana():
            info_e_ventana = Tk()
            info_e_ventana.title("Aplicación")
            info_e_ventana.geometry("360x660")
            info_e_ventana.config(bg="yellow green")
            epipremnum_ventana.withdraw()

            dialogo_robot_e_3 = Label(info_e_ventana, text=INFOR_E, font=20)
            dialogo_robot_e_3.config(bg="dark sea green")
            dialogo_robot_e_3.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(info_e_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [info_e_ventana.destroy(),
                                  epipremnum_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(info_e_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [info_e_ventana.destroy(),
                                   epipremnum_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def beneficios_e_ventana():
            beneficios_e_ventana = Tk()
            beneficios_e_ventana.title("Aplicación")
            beneficios_e_ventana.geometry("360x660")
            beneficios_e_ventana.config(bg="yellow green")
            epipremnum_ventana.withdraw()

            dialogo_robot_e_4 = Label(beneficios_e_ventana,
                                      text=BENEFI_E, font=20)
            dialogo_robot_e_4.config(bg="dark sea green")
            dialogo_robot_e_4.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(beneficios_e_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [beneficios_e_ventana.destroy(),
                                  epipremnum_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(beneficios_e_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [beneficios_e_ventana.destroy(),
                                   epipremnum_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def cuidados_e_ventana():
            cuidados_e_ventana = Tk()
            cuidados_e_ventana.title("Aplicación")
            cuidados_e_ventana.geometry("360x660")
            cuidados_e_ventana.config(bg="yellow green")
            epipremnum_ventana.withdraw()

            dialogo_robot_e_5 = Label(cuidados_e_ventana,
                                      text=CUIDAD_E, font=20)
            dialogo_robot_e_5.config(bg="dark sea green")
            dialogo_robot_e_5.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(cuidados_e_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [cuidados_e_ventana.destroy(),
                                  epipremnum_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)
            boton_cerrar = Button(cuidados_e_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [cuidados_e_ventana.destroy(),
                                   epipremnum_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # BOTONES PARA CADA UNA DE LA INFORMACION DESEADA Y BOTON PARA CERRAR
        boton_e_riego = Button(epipremnum_ventana,
                               text="¿Cómo regar esta planta?",
                               command=riego_e_ventana)
        boton_e_riego.config(bg="dark sea green")
        boton_e_riego.place(x=115, y=65, width=139, height=25)

        boton_e_info = Button(epipremnum_ventana,
                              text="Información sobre esta planta",
                              command=info_e_ventana)
        boton_e_info.config(bg="dark sea green")
        boton_e_info.place(x=100, y=145, width=165, height=25)

        boton_e_beneficios = Button(epipremnum_ventana,
                                    text="Beneficios de tener esta planta",
                                    command=beneficios_e_ventana)
        boton_e_beneficios.config(bg="dark sea green")
        boton_e_beneficios.place(x=100, y=225, width=167, height=25)

        boton_e_cuidados = Button(epipremnum_ventana,
                                  text="Cuidados de esta planta",
                                  command=cuidados_e_ventana)
        boton_e_cuidados.config(bg="dark sea green")
        boton_e_cuidados.place(x=115, y=305, width=133, height=25)

    def coryphanta_ventana():
        coryphanta_ventana = Tk()
        coryphanta_ventana.title("Aplicación")
        coryphanta_ventana.geometry("360x660")
        coryphanta_ventana.config(bg="yellow green")
        segunda_ventana.withdraw()

        dialogo_robot_c_1 = Label(coryphanta_ventana,
                                  text="¿Qué te gustaría saber?")
        dialogo_robot_c_1.config(bg="dark sea green")
        dialogo_robot_c_1.place(x=120, y=20, width=130, height=25)

        boton_atras = Button(coryphanta_ventana,
                             text="Atrás",
                             command=lambda: [coryphanta_ventana.destroy(),
                                              segunda_ventana.deiconify()])
        boton_atras.config(bg="dark khaki")
        boton_atras.place(x=0, y=638, width=50, height=25)

        def riego_c_ventana():
            riego_c_ventana = Tk()
            riego_c_ventana.title("Aplicación")
            riego_c_ventana.geometry("360x660")
            riego_c_ventana.config(bg="yellow green")
            coryphanta_ventana.withdraw()

            dialogo_robot_c_2 = Label(riego_c_ventana,
                                      text="Los riegos deben ser de forma "
                                           "moderada en primavera\n"+"y verano"
                                           ", siempre manteniendo el suelo "
                                           "seco de esta misma,\n"+"en la "
                                           "epoca fria, los riegos deben "
                                           "suspenderse\n"+"en pos del cuidado"
                                           " de la planta.")
            dialogo_robot_c_2.config(bg="dark sea green")
            dialogo_robot_c_2.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(riego_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [riego_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(riego_c_ventana,
                                  text="Cerrar",
                                  command=riego_c_ventana.destroy)
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def info_c_ventana():
            info_c_ventana = Tk()
            info_c_ventana.title("Aplicación")
            info_c_ventana.geometry("360x660")
            info_c_ventana.config(bg="yellow green")
            coryphanta_ventana.withdraw()

            dialogo_robot_c_3 = Label(info_c_ventana,
                                      text="La Coryphanta, tambien conocida "
                                           "como cactus,\n"+"es un genero "
                                           "nativo de Mexico, siendo uno de "
                                           "los mas extensos.\n"+"Esta puede "
                                           "crecer aproximadamente hasta "
                                           "5-6 cm,\n"+"cuando se desarrolla "
                                           "forma una flor central grande.")
            dialogo_robot_c_3.config(bg="dark sea green")
            dialogo_robot_c_3.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(info_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [info_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(info_c_ventana,
                                  text="Cerrar",
                                  command=info_c_ventana.destroy)
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def beneficios_c_ventana():
            beneficios_c_ventana = Tk()
            beneficios_c_ventana.title("Aplicación")
            beneficios_c_ventana.geometry("360x660")
            beneficios_c_ventana.config(bg="yellow green")
            coryphanta_ventana.withdraw()

            dialogo_robot_c_4 = Label(beneficios_c_ventana,
                                      text="Este puntiagudo genero de plantas,"
                                           " son excelentes\n"+"purificadores "
                                           "de aire, siendo esto perfecto a la"
                                           "hora de\n"+"cuidar nuestra salud, "
                                           "tambien son plantas que requieren"
                                           "\n"+"muy poco cuidado debido a su "
                                           "poca necesidad de agua,\n"+"siendo"
                                           " estas perfectas para gente que no"
                                           " puede dedicar\n"+"todo su tiempo "
                                           "a una planta.")
            dialogo_robot_c_4.config(bg="dark sea green")
            dialogo_robot_c_4.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(beneficios_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [beneficios_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(beneficios_c_ventana,
                                  text="Cerrar",
                                  command=beneficios_c_ventana.destroy)
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def cuidados_c_ventana():
            cuidados_c_ventana = Tk()
            cuidados_c_ventana.title("Aplicación")
            cuidados_c_ventana.geometry("360x660")
            cuidados_c_ventana.config(bg="yellow green")
            coryphanta_ventana.withdraw()

            dialogo_robot_c_5 = Label(cuidados_c_ventana,
                                      text="A esta pequeña planta, le encanta "
                                           "tener luz directa,\n"+"aunque "
                                           "tambien pueden recibir por "
                                           "periodos causando el mismo\n"
                                           "efecto de estar todo el dia en la "
                                           "luz solar,\n"+"la tierra organica "
                                           "mezclada con fibra de coco,\n"
                                           "hojas secas, corteza y turba son "
                                           "lo mejor para su perfecto "
                                           "desarrollo.")
            dialogo_robot_c_5.config(bg="dark sea green")
            dialogo_robot_c_5.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=125)

            boton_atras = Button(cuidados_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [cuidados_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(cuidados_c_ventana,
                                  text="Cerrar",
                                  command=cuidados_c_ventana.destroy)
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # BOTONES PARA CADA UNA DE LA INFORMACION DESEADA Y BOTON PARA CERRAR
        boton_c_riego = Button(coryphanta_ventana,
                               text="¿Cómo regar esta planta?",
                               command=riego_c_ventana)
        boton_c_riego.config(bg="dark sea green")
        boton_c_riego.place(x=115, y=65, width=139, height=25)

        boton_c_info = Button(coryphanta_ventana,
                              text="Información sobre esta planta",
                              command=info_c_ventana)
        boton_c_info.config(bg="dark sea green")
        boton_c_info.place(x=100, y=145, width=165, height=25)

        boton_c_beneficios = Button(coryphanta_ventana,
                                    text="Beneficios de tener esta planta",
                                    command=beneficios_c_ventana)
        boton_c_beneficios.config(bg="dark sea green")
        boton_c_beneficios.place(x=100, y=225, width=167, height=25)

        boton_c_cuidados = Button(coryphanta_ventana,
                                  text="Cuidados de esta planta",
                                  command=cuidados_c_ventana)
        boton_c_cuidados.config(bg="dark sea green")
        boton_c_cuidados.place(x=115, y=305, width=133, height=25)

        boton_cerrar = Button(coryphanta_ventana,
                              text="Cerrar",
                              command=coryphanta_ventana.destroy)
        boton_cerrar.config(bg="light coral")
        boton_cerrar.place(x=310, y=640, width=50, height=25)

    # TERCERA VENTANA
    def tercera_ventana():
        tercera_ventana = Tk()
        tercera_ventana.title("Aplicación")
        tercera_ventana.geometry("360x660")
        tercera_ventana.config(bg="yellow green")

        dialogo_robot_3_1 = Label(tercera_ventana,
                                  text="Poseo informacion de los siguientes "
                                       "géneros de plantas")
        dialogo_robot_3_1.place(x=35, y=10, width=300, height=25)
        dialogo_robot_3_1.config(bg="dark sea green")
        dialogo_robot_3_2 = Label(tercera_ventana,
                                  text="¿Cual te gustaria seleccionar?")
        dialogo_robot_3_2.place(x=80, y=30, width=200, height=25)
        dialogo_robot_3_2.config(bg="dark sea green")

        numero_pagina = Label(tercera_ventana, text="2/2")
        numero_pagina.config(bg="dark sea green")
        numero_pagina.place(x=0, y=0, width=30, height=20)

        segunda_ventana.withdraw()

        def ficus_ventana():
            ficus_ventana = Tk()
            ficus_ventana.title("Aplicación")
            ficus_ventana.geometry("360x660")
            ficus_ventana.config(bg="yellow green")
            tercera_ventana.withdraw()

            dialogo_robot_f_1 = Label(ficus_ventana,
                                      text="¿Qué te gustaría saber?")
            dialogo_robot_f_1.config(bg="dark sea green")
            dialogo_robot_f_1.place(x=120, y=20, width=130, height=25)

            boton_atras = Button(ficus_ventana,
                                 text="Atrás",
                                 command=lambda: [ficus_ventana.destroy(),
                                                  tercera_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            def riego_f_ventana():
                riego_f_ventana = Tk()
                riego_f_ventana.title("Aplicación")
                riego_f_ventana.geometry("360x660")
                riego_f_ventana.config(bg="yellow green")
                ficus_ventana.withdraw()

                dialogo_robot_f_2 = Label(riego_f_ventana,
                                          text="Necesitan un riego de "
                                               "aproximadamente dos veces\n"
                                               "por semana en verano, una en "
                                               "invierno y en\n"+"regiones "
                                               "húmedas: cada 8 o 10 días.\n"
                                               "Se debe evitar el agua muy "
                                               "fría y también\n"+"tener mucho"
                                               " cuidado de no escarchar las "
                                               "raices.")
                dialogo_robot_f_2.config(bg="dark sea green")
                dialogo_robot_f_2.place(anchor="c", relx=0.5, rely=0.105,
                                        width=325, height=125)

                boton_atras = Button(riego_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [riego_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(riego_f_ventana,
                                      text="Cerrar",
                                      command=riego_f_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            def info_f_ventana():
                info_f_ventana = Tk()
                info_f_ventana.title("Aplicación")
                info_f_ventana.geometry("360x660")
                info_f_ventana.config(bg="yellow green")
                ficus_ventana.withdraw()

                dialogo_robot_f_3 = Label(info_f_ventana,
                                          text="Provienen de bosques "
                                               "tropicales.\n"+"Sus ramas son "
                                               "grandes y sus hojas bastante "
                                               "puntiagudas,\n"+"lo que añade "
                                               "un toque de 'jungla' tropical "
                                               "al ambiente.\n"+"Además, en su"
                                               " variedad existen plantas que "
                                               "llegan al\n"+"metro de altitud"
                                               ", tanto como a los 60 metros.")
                dialogo_robot_f_3.config(bg="dark sea green")
                dialogo_robot_f_3.place(anchor="c", relx=0.5, rely=0.105,
                                        width=325, height=125)

                boton_atras = Button(info_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [info_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(info_f_ventana,
                                      text="Cerrar",
                                      command=info_f_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            def beneficios_f_ventana():
                beneficios_f_ventana = Tk()
                beneficios_f_ventana.title("Aplicación")
                beneficios_f_ventana.geometry("360x660")
                beneficios_f_ventana.config(bg="yellow green")
                ficus_ventana.withdraw()

                dialogo_robot_f_4 = Label(beneficios_f_ventana,
                                          text="Son plantas que se adaptan muy"
                                               " bien al clima.\n"+"Mejoran la"
                                               " calidad del aire absorbiendo "
                                               "tóxicos.\n"+"Además, algunas "
                                               "de las plantas del género "
                                               "contienen\n"+"propiedades "
                                               "medicinales, siendo usada\n"
                                               "para tratar diversas picaduras"
                                               " de insectos.")
                dialogo_robot_f_4.config(bg="dark sea green")
                dialogo_robot_f_4.place(anchor="c", relx=0.5, rely=0.105,
                                        width=325, height=125)

                boton_atras = Button(beneficios_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [beneficios_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(beneficios_f_ventana,
                                      text="Cerrar",
                                      command=beneficios_f_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            def cuidados_f_ventana():
                cuidados_f_ventana = Tk()
                cuidados_f_ventana.title("Aplicación")
                cuidados_f_ventana.geometry("360x660")
                cuidados_f_ventana.config(bg="yellow green")
                ficus_ventana.withdraw()

                dialogo_robot_f_5 = Label(cuidados_f_ventana,
                                          text="Estas plantas necesitan "
                                               "grandes dosis de luz,\n"+"pero"
                                               " sin que sea directa, "
                                               "necesitan un ambiente\n"
                                               "cálido y humedo, por lo que es"
                                               "recomendable\n"+"pulverizar y "
                                               "limpiar sus hojas con cierta "
                                               "frecuencia.\n")
                dialogo_robot_f_5.config(bg="dark sea green")
                dialogo_robot_f_5.place(anchor="c", relx=0.5, rely=0.105,
                                        width=325, height=125)

                boton_atras = Button(cuidados_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [cuidados_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(cuidados_f_ventana,
                                      text="Cerrar",
                                      command=cuidados_f_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # BOTONES PARA CADA UNA DE LA INFORMACION DESEADA

            boton_f_riego = Button(ficus_ventana,
                                   text="¿Cómo regar esta planta?",
                                   command=riego_f_ventana)
            boton_f_riego.config(bg="dark sea green")
            boton_f_riego.place(x=115, y=65, width=139, height=25)

            boton_f_info = Button(ficus_ventana,
                                  text="Información sobre esta planta",
                                  command=info_f_ventana)
            boton_f_info.config(bg="dark sea green")
            boton_f_info.place(x=100, y=145, width=165, height=25)

            boton_f_beneficios = Button(ficus_ventana,
                                        text="Beneficios de tener esta planta",
                                        command=beneficios_f_ventana)
            boton_f_beneficios.config(bg="dark sea green")
            boton_f_beneficios.place(x=100, y=225, width=167, height=25)

            boton_f_cuidados = Button(ficus_ventana,
                                      text="Cuidados de esta planta",
                                      command=cuidados_f_ventana)
            boton_f_cuidados.config(bg="dark sea green")
            boton_f_cuidados.place(x=115, y=305, width=133, height=25)

            # BOTON PARA CERRAR
            boton_cerrar = Button(ficus_ventana,
                                  text="Cerrar",
                                  command=ficus_ventana.destroy)
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        def aloe_ventana():
            aloe_ventana = Tk()
            aloe_ventana.title("Aplicación")
            aloe_ventana.geometry("360x660")
            aloe_ventana.config(bg="yellow green")
            tercera_ventana.withdraw()

            dialogo_robot_a_1 = Label(aloe_ventana,
                                      text="¿Qué te gustaría saber?")
            dialogo_robot_a_1.config(bg="dark sea green")
            dialogo_robot_a_1.place(x=120, y=20, width=130, height=25)

            boton_atras = Button(aloe_ventana,
                                 text="Atrás",
                                 command=lambda: [aloe_ventana.destroy(),
                                                  tercera_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            def riego_a_ventana():
                riego_a_ventana = Tk()
                riego_a_ventana.title("Aplicación")
                riego_a_ventana.geometry("360x660")
                riego_a_ventana.config(bg="yellow green")
                aloe_ventana.withdraw()

                dialogo_robot_a_2 = Label(riego_a_ventana,
                                          text="Es recomendable regar a un "
                                               "aloe cada 15 o 20 días,\n"
                                               "excepto por invierno que se "
                                               "pueden reducir a 1 por mes,\n"
                                               "siempre utilizando poca agua y"
                                               " vertiéndola\n"+"directamente "
                                               "sobre la tierra, sin dejar la"
                                               " maceta encharcada.")
                dialogo_robot_a_2.config(bg="dark sea green")
                dialogo_robot_a_2.place(x=25, y=10, width=320, height=75)

                boton_atras = Button(riego_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [riego_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(riego_a_ventana,
                                      text="Cerrar",
                                      command=riego_a_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            def info_a_ventana():
                info_a_ventana = Tk()
                info_a_ventana.title("Aplicación")
                info_a_ventana.geometry("360x660")
                info_a_ventana.config(bg="yellow green")
                aloe_ventana.withdraw()

                dialogo_robot_a_3 = Label(info_a_ventana,
                                          text="Son plantas siempreverdes, con"
                                               " hojas\n"+"afiladas en su "
                                               "apice y margenes espinosos.\n"
                                               "Es un genero que tiene la "
                                               "capacidad de conservar el\n"
                                               "agua de lluvia, lo que le "
                                               "permite sobrevivir durante\n"
                                               "largos períodos de tiempo en "
                                               "condiciones de sequia!")
                dialogo_robot_a_3.config(bg="dark sea green")
                dialogo_robot_a_3.place(x=29, y=10, width=310, height=80)

                boton_atras = Button(info_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [info_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(info_a_ventana,
                                      text="Cerrar",
                                      command=info_a_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            def beneficios_a_ventana():
                beneficios_a_ventana = Tk()
                beneficios_a_ventana.title("Aplicación")
                beneficios_a_ventana.geometry("360x660")
                beneficios_a_ventana.config(bg="yellow green")
                aloe_ventana.withdraw()

                dialogo_robot_a_4 = Label(beneficios_a_ventana,
                                          text="Son plantas que tienen "
                                               "diversos pros para la salud,\n"
                                               "como los siguientes:\n"
                                               "-Posee vitaminas que son "
                                               "beneficiosas para la salud "
                                               "humana\n"+"-Propiedades "
                                               "antiinflamatorias\n"
                                               "-Accion con efecto calmante "
                                               "de gastritis y esofagitis.")
                dialogo_robot_a_4.config(bg="dark sea green")
                dialogo_robot_a_4.place(x=17, y=10, width=330, height=80)

                boton_atras = Button(beneficios_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [beneficios_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(beneficios_a_ventana,
                                      text="Cerrar",
                                      command=beneficios_a_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            def cuidados_a_ventana():
                cuidados_a_ventana = Tk()
                cuidados_a_ventana.title("Aplicación")
                cuidados_a_ventana.geometry("360x660")
                cuidados_a_ventana.config(bg="yellow green")
                aloe_ventana.withdraw()

                dialogo_robot_a_5 = Label(cuidados_a_ventana,
                                          text="Estas plantas necesitan mucha "
                                               "luz\n"+"para crecer sanas y "
                                               "florecer al máximo, siempre "
                                               "manteniendo\n"+"en "
                                               "consideracion la temperatura, "
                                               "no debe ser inferior a 10°C.\n"
                                               "Se pueden retirar las hojas y "
                                               "espigas florales\n"+"que se "
                                               "hayan secado para evitar "
                                               "plagas.")
                dialogo_robot_a_5.config(bg="dark sea green")
                dialogo_robot_a_5.place(x=15, y=10, width=333, height=80)

                boton_atras = Button(cuidados_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [cuidados_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(cuidados_a_ventana,
                                      text="Cerrar",
                                      command=cuidados_a_ventana.destroy)
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # BOTONES PARA CADA UNA DE LA INFORMACION DESEADA

            boton_a_riego = Button(aloe_ventana,
                                   text="¿Cómo regar esta planta?",
                                   command=riego_a_ventana)
            boton_a_riego.config(bg="dark sea green")
            boton_a_riego.place(x=115, y=65, width=139, height=25)

            boton_a_info = Button(aloe_ventana,
                                  text="Información sobre esta planta",
                                  command=info_a_ventana)
            boton_a_info.config(bg="dark sea green")
            boton_a_info.place(x=100, y=145, width=165, height=25)

            boton_a_beneficios = Button(aloe_ventana,
                                        text="Beneficios de tener esta planta",
                                        command=beneficios_a_ventana)
            boton_a_beneficios.config(bg="dark sea green")
            boton_a_beneficios.place(x=100, y=225, width=167, height=25)

            boton_a_cuidados = Button(aloe_ventana,
                                      text="Cuidados de esta planta",
                                      command=cuidados_a_ventana)
            boton_a_cuidados.config(bg="dark sea green")
            boton_a_cuidados.place(x=115, y=305, width=133, height=25)

            # BOTON PARA CERRAR

            boton_cerrar = Button(aloe_ventana,
                                  text="Cerrar",
                                  command=aloe_ventana.destroy)
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # BOTONES TERCERA VENTANA

        boton_ficus = Button(tercera_ventana,
                             text="Género Ficus",
                             command=ficus_ventana)
        boton_ficus.config(bg="dark sea green")
        boton_ficus.place(x=120, y=100, width=125, height=25)

        boton_aloe = Button(tercera_ventana,
                            text="Género Aloe",
                            command=aloe_ventana)
        boton_aloe.config(bg="dark sea green")
        boton_aloe.place(x=120, y=350, width=125, height=25)

        boton_cerrar = Button(tercera_ventana,
                              text="Cerrar",
                              command=tercera_ventana.destroy)
        boton_cerrar.config(bg="light coral")
        boton_cerrar.place(x=310, y=640, width=50, height=25)

        boton_atras = Button(tercera_ventana,
                             text="Atrás",
                             command=lambda: [tercera_ventana.destroy(),
                                              segunda_ventana.deiconify()])
        boton_atras.config(bg="dark khaki")
        boton_atras.place(x=0, y=638, width=50, height=25)

    # BOTONES SEGUNDA VENTANA

    boton_epipremnum = Button(segunda_ventana,
                              text="Género Epipremnum",
                              command=epipremnum_ventana)
    boton_epipremnum.config(bg="dark sea green")
    boton_epipremnum.place(x=120, y=100, width=125, height=25)

    boton_coryphanta = Button(segunda_ventana,
                              text="Género Coryphanta",
                              command=coryphanta_ventana)
    boton_coryphanta.config(bg="dark sea green")
    boton_coryphanta.place(x=120, y=350, width=125, height=25)

    boton_cerrar = Button(segunda_ventana,
                          text="Cerrar",
                          command=lambda:
                          [segunda_ventana.destroy(),
                           ventana_principal.destroy()])
    boton_cerrar.config(bg="light coral")
    boton_cerrar.place(x=310, y=640, width=50, height=25)

    boton_atras = Button(segunda_ventana,
                         text="Atrás",
                         command=lambda: [segunda_ventana.destroy(),
                                          ventana_principal.deiconify()])
    boton_atras.config(bg="dark khaki")
    boton_atras.place(x=0, y=638, width=50, height=25)

    boton_sig_pag = Button(segunda_ventana,
                           text="Siguiente pagina",
                           command=tercera_ventana)
    boton_sig_pag.config(bg="dark khaki")
    boton_sig_pag.place(x=50, y=638, width=100, height=25)

    ventana_principal.withdraw()

# BOTONES VENTANA PRINCIPAL


boton_cerrar1 = Button(ventana_principal,
                       text="Cerrar",
                       command=ventana_principal.destroy)
boton_cerrar1.config(bg="light coral")
boton_cerrar1.place(x=310, y=640, width=50, height=25)

boton_continuar = Button(ventana_principal,
                         text="Continuar",
                         command=ventana_2,
                         font=35)
boton_continuar.config(bg="dark sea green")
boton_continuar.place(anchor="c", relx=0.5, y=345, width=100, height=35)

# IMAGEN INICIAL

robot_imagen = ImageTk.PhotoImage(Image.open("robot.png"))
robot_label = Label(image=robot_imagen)
robot_label.config(bg="dark sea green")
robot_label.place(x=110, y=130)

ventana_principal.mainloop()
