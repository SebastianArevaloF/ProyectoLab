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

# IMPORTACION DE LIBRERIAS
# Se importa el modulo tkinter, con respectivas funiones
# para desarrollo de interfaz
from tkinter import Toplevel, Button, Tk, Label, LEFT, SOLID
# Se importa el modulo PIL, para imagenes
from PIL import Image, ImageTk
# Clase ToolTip, para creacion de
# Una ventana de informacion resumida
# Cuando el usuario ponga el cursor en una imagen


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 90
        y = y + cy + self.widget.winfo_rooty() + 90
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):

    toolTip = ToolTip(widget)

    def enter(event):

        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# CONSTANTES
# DATOS EPIPREMNUM
RIEGO_E = ("Los riegos deben ser frecuentes en la\n"
           "epoca cálida, manteniendo humedad alta,\n"
           "rociando las hojas y se deben reducir\n"
           "a partir de otoño. En invierno se deben\n"
           "mantener escasos. La temperatura ideal\n"
           "del agua para regarla es entre los 20°C a 25°C.")
INFOR_E = ("La Epipremnum, tambien conocida como\n"
           "potos, perteneciente a la familia Araceae\n "
           "puede tener tallos de hasta 4cm de diámetro,\n"
           "esta no florece de manera natural, sino\n"
           "de manera inducida.")
BENEFI_E = ("Este género tan curioso de plantas\n"
            "es perfecto para poder decorar cualquier\n"
            "parte de tu casa, también ayuda\n "
            "considerablemente a eliminar las\n"
            "toxinas del aire que no podemos apreciar\n"
            "a simple vista.")
CUIDAD_E = ("A esta curiosa planta, le gusta mucho\n"
            "mantenerse en un ambiente húmedo,\n"
            "evita mantenerla a la luz directa del sol\n"
            "ya que esto no le gusta, mantenla cerca\n"
            "de la ventana evitando lo anterior dicho.")
# DATOS CORYPHANYTA
RIEGO_CO = ("Los riegos deben ser de forma moderada\n"
            "en primavera y verano, siempre manteniendo\n"
            "el suelo seco de esta misma. En la epoca fría,\n"
            "los riegos deben suspenderse en pos del\n"
            "cuidado de la planta.")
INFORM_C = ("La Coryphanta, tambien conocida como\n"
            "cactus, es un género nativo de México,\n "
            "siendo uno de los mas extensos.\n"
            "Esta puede crecer aproximadamente\n "
            "hasta 5-6 cm. Cuando se desarrolla\n"
            "forma una flor central grande.")
BENEFI_C = ("Este puntiagudo género de plantas, son\n"
            "excelentes purificadores de aire, siendo\n "
            "esto perfecto a la hora de cuidar nuestra\n"
            "salud, tambien son plantas que requieren\n "
            "muy poco cuidado debido a su poca\n "
            "necesidad de agua, siendo estas perfectas\n"
            "para gente que no puede dedicar todo su\n"
            "tiempo a una planta.")
CUIDAD_C = ("A esta pequeña planta, le encanta tener\n"
            "luz directa, aunque también pueden recibir\n"
            "por periodos causando el mismo efecto de\n"
            "estar todo el dia en la luz solar. La tierra\n"
            "orgánica mezclada con fibra de coco, hojas\n"
            "secas, corteza y turba son lo mejor para su\n "
            "perfecto desarrollo.")
# DATOS FICUS
RIEGO_FI = ("Necesitan un riego de aproximadamente dos\n"
            "veces por semana en verano, una en invierno\n"
            "y en regiones húmedas: cada 8 o 10 días.\n"
            "Se debe evitar el agua muy fría y también\n"
            "tener mucho cuidado de no encharcar\n"
            "las raices.")
INFOR_FI = ("Provienen de bosques tropicales. Sus\n"
            "ramas son grandes y sus hojas bastante\n"
            "puntiagudas, lo que añade un toque de \n"
            "'jungla' tropical al ambiente. Además,\n"
            "en su variedad existen plantas que llegan\n"
            "al metro de altitud, y otras que llegan\n"
            "a los 15 metros.")
BENEFI_F = ("Son plantas que se adaptan muy bien\n"
            "al clima. Mejoran la calidad del aire\n"
            "absorbiendo toxinas. Además, algunas\n"
            "de las plantas del género contienen\n"
            " propiedades medicinales, siendo usadas\n"
            "para tratar diversas picaduras de insectos.")
CUIDAD_F = ("Estas plantas necesitan grandes\n"
            "dosis de luz, pero sin que sea directa\n"
            "necesitan un ambiente cálido y húmedo,\n"
            "por lo que es recomendable pulverizar y\n"
            "limpiar sus hojas con cierta, frecuencia.")
# DATOS ALOE
RIEGO_AL = ("Es recomendable regar a un aloe cada\n"
            "15 o 20 días, excepto por invierno que\n"
            "se pueden reducir a 1 por mes, siempre\n"
            "utilizando poca agua y vertiéndola\n"
            "directamente sobre la tierra, sin dejar\n"
            "la maceta encharcada.")
INFOR_AL = ("Son plantas siempreverdes, con hojas\n"
            "afiladas en su ápice y márgenes espinosos.\n"
            "Es un género que tiene la capacidad de\n"
            "conservar el agua de lluvia, lo que le\n"
            "permite sobrevivir durante largos\n "
            "períodos de tiempo en condiciones de sequía.")
BENEFI_A = ("Son plantas que tienen diversos pros\n"
            "para la salud, como los siguientes:\n"
            "-Posee vitaminas que son\n"
            "beneficiosas para la salud humana\n"
            "-Propiedades antiinflamatorias\n"
            "-Acción con efecto calmante\n"
            "de gastritis y esofagitis.")
CUIDAD_A = ("Estas plantas necesitan mucha luz\n"
            "para crecer sanas y florecer al máximo,\n"
            "siempre manteniendo en consideración\n"
            "la temperatura que no debe ser inferior\n"
            "a 10°C.Se pueden retirar las hojas y\n"
            "espigas florales que se hayan secado\n"
            "para evitar plagas.")
# IMAGENES

'''
Para la simplificacion de cada variable relacionada al dialogo
Se especificaran las siguientes indicaciones:
1)Para el dialogo del robot, se escribira
dialogo_robot_"NUMERO DE LA VENTANA"_"NUMERO DE DIALOGO"
2)Para el dialogo del robot hablando sobre plantas
Se escribira dialogo_robot_x_y,
Siendo "x" la primera letra del genero e "y" el numero de dialogo
'''

# VENTANA PRINCIPAL
ventana_principal = Tk()
ventana_principal.title("EcoAqua")
ventana_principal.geometry("360x660")
ventana_principal.resizable(width=False, height=False)
# CAMBIOS DE COLORES PARA LA VENTANA PRINCIPAL
ventana_principal.config(bg="yellow green")

foto_regar = Image.open("Regar.png")
foto_regar = foto_regar.resize((100, 100))
foto_regar = ImageTk.PhotoImage(foto_regar)

foto_informacion = Image.open("Informacion.png")
foto_informacion = foto_informacion.resize((100, 100))
foto_informacion = ImageTk.PhotoImage(foto_informacion)

foto_cuidados = Image.open("Cuidados.png")
foto_cuidados = foto_cuidados.resize((100, 100))
foto_cuidados = ImageTk.PhotoImage(foto_cuidados)

foto_beneficios = Image.open("Beneficios.png")
foto_beneficios = foto_beneficios.resize((100, 100))
foto_beneficios = ImageTk.PhotoImage(foto_beneficios)
# CAMBIO DE ICONO DE LA APP POR DEFINIR

# BIENVENIDA Y DIALOGOS DEL ROBOT EN VENTANA PRINCIPAL
bienvenida = Label(ventana_principal, text="Hola! bienvenido a EcoAqua",
                   font=30)
bienvenida.config(bg="dark sea green")
bienvenida.place(anchor="c", relx=0.5, y=30, width=215, height=25)

dialogo_robot_1_1 = Label(ventana_principal, text="Soy Coryphanter 3000",
                          font=30)
dialogo_robot_1_1.place(anchor="c", relx=0.5, y=60, width=175, height=25)
dialogo_robot_1_1.config(bg="dark sea green")

dialogo_robot_1_2 = Label(ventana_principal,
                          text="Estoy aquí para ayudarte\n"
                               "en el cuidado de tu planta",
                          font=30)
dialogo_robot_1_2.place(anchor="c", relx=0.5, y=100, width=195, height=40)
dialogo_robot_1_2.config(bg="dark sea green")

dialogo_robot_1_3 = Label(ventana_principal, text="¿Te gustaría continuar?",
                          font=30)
dialogo_robot_1_3.place(anchor="c", relx=0.5, y=305, width=180, height=25)
dialogo_robot_1_3.config(bg="dark sea green")

# SEGUNDA VENTANA


def ventana_2():
    segunda_ventana = Toplevel()
    segunda_ventana.title("Aplicación")
    segunda_ventana.geometry("360x660")
    segunda_ventana.config(bg="yellow green")
    segunda_ventana.resizable(width=False, height=False)

    dialogo_robot_2_1 = Label(segunda_ventana,
                              text="Poseo información de los siguientes\n"
                                   "géneros de plantas",
                              font=35)
    dialogo_robot_2_1.place(anchor="c", relx=0.5, y=35, width=280, height=45)
    dialogo_robot_2_1.config(bg="dark sea green")
    dialogo_robot_2_2 = Label(segunda_ventana,
                              text="¿Cuál te gustaría seleccionar?", font=35)
    dialogo_robot_2_2.place(anchor="c", relx=0.5, y=75, width=220, height=25)
    dialogo_robot_2_2.config(bg="dark sea green")

    numero_pagina = Label(segunda_ventana, text="1/2")
    numero_pagina.config(bg="dark sea green")
    numero_pagina.place(x=0, y=0, width=30, height=20)

# SE DEFINE UNA FUNCION PARA LA VENTANA DEL GENERO EN ESPECIFICO Y 4 EXTRAS
# DENTRO DE LA YA MENCIONADA, ASÍ PARA DAR PASO A LA VENTANA DE INFORMACION
# QUE PUEDA DESEAR EL USUARIO
    # VENTANA EPIPREMNUM
    def epipremnum_ventana():
        epipremnum_ventana = Toplevel()
        epipremnum_ventana.title("Aplicación")
        epipremnum_ventana.geometry("360x660")
        epipremnum_ventana.resizable(width=False, height=False)
        segunda_ventana.withdraw()

        dialogo_robot_e_1 = Label(epipremnum_ventana, font="Arial 17",
                                  text="¿Qué te gustaría saber?")
        dialogo_robot_e_1.config(bg="dark sea green")
        dialogo_robot_e_1.place(anchor="c", relx=0.5, y=40, width=250,
                                height=30)

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

        # RIEGO EPIPREMNUM

        def riego_e_ventana():
            riego_e_ventana = Toplevel()
            riego_e_ventana.title("Aplicación")
            riego_e_ventana.geometry("360x660")
            riego_e_ventana.config(bg="yellow green")
            riego_e_ventana.resizable(width=False, height=False)
            epipremnum_ventana.withdraw()

            dialogo_robot_e_2 = Label(riego_e_ventana, text=RIEGO_E, font=20)
            dialogo_robot_e_2.config(bg="dark sea green")
            dialogo_robot_e_2.place(anchor="c", relx=0.5, rely=0.105,
                                    width=335, height=125)

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

        # INFORMACIÓN EPIPREMNUM

        def info_e_ventana():
            info_e_ventana = Toplevel()
            info_e_ventana.title("Aplicación")
            info_e_ventana.geometry("360x660")
            info_e_ventana.config(bg="yellow green")
            info_e_ventana.resizable(width=False, height=False)
            epipremnum_ventana.withdraw()

            dialogo_robot_e_3 = Label(info_e_ventana, text=INFOR_E, font=20)
            dialogo_robot_e_3.config(bg="dark sea green")
            dialogo_robot_e_3.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=110)

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

        # BENEFICIOS EPIPREMNUM

        def beneficios_e_ventana():
            beneficios_e_ventana = Toplevel()
            beneficios_e_ventana.title("Aplicación")
            beneficios_e_ventana.geometry("360x660")
            beneficios_e_ventana.config(bg="yellow green")
            beneficios_e_ventana.resizable(width=False, height=False)
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

        # CUIDADOS EPIPREMNUM

        def cuidados_e_ventana():
            cuidados_e_ventana = Toplevel()
            cuidados_e_ventana.title("Aplicación")
            cuidados_e_ventana.geometry("360x660")
            cuidados_e_ventana.config(bg="yellow green")
            cuidados_e_ventana.resizable(width=False, height=False)
            epipremnum_ventana.withdraw()

            dialogo_robot_e_5 = Label(cuidados_e_ventana,
                                      text=CUIDAD_E, font=20)
            dialogo_robot_e_5.config(bg="dark sea green")
            dialogo_robot_e_5.place(anchor="c", relx=0.5, rely=0.105,
                                    width=305, height=105)

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

        # BOTON RIEGO EPIPREMNUM
        boton_e_riego = Button(epipremnum_ventana, image=foto_regar,
                               text="RIEGO", font="Arial 8 bold",
                               compound="bottom",
                               command=riego_e_ventana)
        boton_e_riego.config(bg="dark sea green")
        boton_e_riego.place(anchor="c", relx=0.5, y=165, width=115, height=115)

        CreateToolTip(boton_e_riego, text='¡Diversos consejos\n'
                      'para un correcto riego\n'
                      'de tu planta!')
        # BOTON INFORMACION EPIPREMNUM

        boton_e_info = Button(epipremnum_ventana, image=foto_informacion,
                              text="INFORMACIÓN", font="Arial 8 bold",
                              compound="bottom",
                              command=info_e_ventana)
        boton_e_info.config(bg="dark sea green")
        boton_e_info.place(anchor="c", relx=0.5, y=290, width=115, height=115)

        CreateToolTip(boton_e_info, text='¡Información variada\n'
                      'e interesante\n'
                      'sobre tu planta!')

        # BOTON BENEFICIOS EPIPREMNUM
        boton_e_beneficios = Button(epipremnum_ventana, image=foto_beneficios,
                                    text="BENEFICIOS", font="Arial 8 bold",
                                    compound="bottom",
                                    command=beneficios_e_ventana)
        boton_e_beneficios.config(bg="dark sea green")
        boton_e_beneficios.place(anchor="c", relx=0.5, y=415, width=115,
                                 height=115)

        CreateToolTip(boton_e_beneficios, text='¡Beneficios variados\n'
                                               'que te da tu planta!')

        # BOTON CUIDADOS EPIPREMNUM
        boton_e_cuidados = Button(epipremnum_ventana, image=foto_cuidados,
                                  text="CUIDADOS", font="Arial 8 bold",
                                  compound="bottom",
                                  command=cuidados_e_ventana)
        boton_e_cuidados.config(bg="dark sea green")
        boton_e_cuidados.place(anchor="c", relx=0.5, y=540, width=115,
                               height=115)

        CreateToolTip(boton_e_cuidados, text='¡Cuidados específicos\n'
                      'para tu planta!')

    # VENTANA CORYPHANTA

    def coryphanta_ventana():
        coryphanta_ventana = Toplevel()
        coryphanta_ventana.title("Aplicación")
        coryphanta_ventana.geometry("360x660")
        coryphanta_ventana.config(bg="yellow green")
        coryphanta_ventana.resizable(width=False, height=False)
        segunda_ventana.withdraw()

        dialogo_robot_c_1 = Label(coryphanta_ventana, font="Arial 17",
                                  text="¿Qué te gustaría saber?")
        dialogo_robot_c_1.config(bg="dark sea green")
        dialogo_robot_c_1.place(anchor="c", relx=0.5, y=40, width=250,
                                height=30)

        boton_atras = Button(coryphanta_ventana,
                             text="Atrás",
                             command=lambda: [coryphanta_ventana.destroy(),
                                              segunda_ventana.deiconify()])
        boton_atras.config(bg="dark khaki")
        boton_atras.place(x=0, y=638, width=50, height=25)

        boton_cerrar = Button(coryphanta_ventana,
                              text="Cerrar",
                              command=lambda: [coryphanta_ventana.destroy(),
                                               segunda_ventana.destroy(),
                                               ventana_principal.destroy()])
        boton_cerrar.config(bg="light coral")
        boton_cerrar.place(x=310, y=640, width=50, height=25)

        # RIEGO CORYPHANTA

        def riego_c_ventana():
            riego_c_ventana = Toplevel()
            riego_c_ventana.title("Aplicación")
            riego_c_ventana.geometry("360x660")
            riego_c_ventana.config(bg="yellow green")
            riego_c_ventana.resizable(width=False, height=False)
            coryphanta_ventana.withdraw()

            dialogo_robot_c_2 = Label(riego_c_ventana,
                                      text=RIEGO_CO, font=20)
            dialogo_robot_c_2.config(bg="dark sea green")
            dialogo_robot_c_2.place(anchor="c", relx=0.5, rely=0.105,
                                    width=325, height=110)

            boton_atras = Button(riego_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [riego_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(riego_c_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [riego_c_ventana.destroy(),
                                   coryphanta_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # INFORMACIÓN CORYPHANTA

        def info_c_ventana():
            info_c_ventana = Toplevel()
            info_c_ventana.title("Aplicación")
            info_c_ventana.geometry("360x660")
            info_c_ventana.config(bg="yellow green")
            info_c_ventana.resizable(width=False, height=False)
            coryphanta_ventana.withdraw()

            dialogo_robot_c_3 = Label(info_c_ventana,
                                      text=INFORM_C, font=20)
            dialogo_robot_c_3.config(bg="dark sea green")
            dialogo_robot_c_3.place(anchor="c", relx=0.5, rely=0.105,
                                    width=305, height=125)

            boton_atras = Button(info_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [info_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(info_c_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [info_c_ventana.destroy(),
                                   coryphanta_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # BENEFICIOS CORYPHANTA

        def beneficios_c_ventana():
            beneficios_c_ventana = Toplevel()
            beneficios_c_ventana.title("Aplicación")
            beneficios_c_ventana.geometry("360x660")
            beneficios_c_ventana.config(bg="yellow green")
            beneficios_c_ventana.resizable(width=False, height=False)
            coryphanta_ventana.withdraw()

            dialogo_robot_c_4 = Label(beneficios_c_ventana,
                                      text=BENEFI_C, font=20)
            dialogo_robot_c_4.config(bg="dark sea green")
            dialogo_robot_c_4.place(anchor="c", relx=0.5, rely=0.13,
                                    width=325, height=160)

            boton_atras = Button(beneficios_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [beneficios_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(beneficios_c_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [beneficios_c_ventana.destroy(),
                                   coryphanta_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # CUIDADOS CORYPHANTA

        def cuidados_c_ventana():
            cuidados_c_ventana = Toplevel()
            cuidados_c_ventana.title("Aplicación")
            cuidados_c_ventana.geometry("360x660")
            cuidados_c_ventana.config(bg="yellow green")
            cuidados_c_ventana.resizable(width=False, height=False)
            coryphanta_ventana.withdraw()

            dialogo_robot_c_5 = Label(cuidados_c_ventana,
                                      text=CUIDAD_C, font=20)
            dialogo_robot_c_5.config(bg="dark sea green")
            dialogo_robot_c_5.place(anchor="c", relx=0.5, rely=0.115,
                                    width=325, height=140)

            boton_atras = Button(cuidados_c_ventana,
                                 text="Atrás",
                                 command=lambda:
                                 [cuidados_c_ventana.destroy(),
                                  coryphanta_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(cuidados_c_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [cuidados_c_ventana.destroy(),
                                   coryphanta_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

        # BOTON RIEGO CORYPHANTA
        boton_c_riego = Button(coryphanta_ventana, image=foto_regar,
                               text="RIEGO", font="Arial 8 bold",
                               compound="bottom",
                               command=riego_c_ventana)
        boton_c_riego.config(bg="dark sea green")
        boton_c_riego.place(anchor="c", relx=0.5, y=165, width=115, height=115)

        CreateToolTip(boton_c_riego, text='¡Diversos consejos\n'
                      'para un correcto riego\n'
                      'de tu planta!')

        # BOTON CUIDADOS CORYPHANTA

        boton_c_info = Button(coryphanta_ventana, image=foto_informacion,
                              text="INFORMACIÓN", font="Arial 8 bold",
                              compound="bottom",
                              command=info_c_ventana)
        boton_c_info.config(bg="dark sea green")
        boton_c_info.place(anchor="c", relx=0.5, y=290, width=115, height=115)

        CreateToolTip(boton_c_info, text='¡Información variada\n'
                      'e interesante\n'
                      'sobre tu planta!')

        # BOTON BENEFICIOS CORYPHANTA

        boton_c_beneficios = Button(coryphanta_ventana, image=foto_beneficios,
                                    text="BENEFICIOS", font="Arial 8 bold",
                                    compound="bottom",
                                    command=beneficios_c_ventana)
        boton_c_beneficios.config(bg="dark sea green")
        boton_c_beneficios.place(anchor="c", relx=0.5, y=415, width=115,
                                 height=115)

        CreateToolTip(boton_c_beneficios, text='¡Beneficios variados\n'
                      'que te da tu planta!')

        # BOTON CUIDADOS CORYPHANTA

        boton_c_cuidados = Button(coryphanta_ventana, image=foto_cuidados,
                                  text="CUIDADOS", font="Arial 8 bold",
                                  compound="bottom",
                                  command=cuidados_c_ventana)
        boton_c_cuidados.config(bg="dark sea green")
        boton_c_cuidados.place(anchor="c", relx=0.5, y=540, width=115,
                               height=115)

        CreateToolTip(boton_c_cuidados, text='¡Cuidados específicos\n'
                      'para tu planta!')

    # TERCERA VENTANA
    def ventana_3():
        tercera_ventana = Toplevel()
        tercera_ventana.title("Aplicación")
        tercera_ventana.geometry("360x660")
        tercera_ventana.config(bg="yellow green")
        tercera_ventana.resizable(width=False, height=False)

        dialogo_robot_3_1 = Label(tercera_ventana,
                                  text="Poseo información de los siguientes\n"
                                       "géneros de plantas",
                                  font=35)
        dialogo_robot_3_1.place(anchor="c", relx=0.5, y=35, width=280,
                                height=45)
        dialogo_robot_3_1.config(bg="dark sea green")
        dialogo_robot_3_2 = Label(tercera_ventana, font=35,
                                  text="¿Cuál te gustaría seleccionar?")
        dialogo_robot_3_2.place(anchor="c", relx=0.5, y=75, width=220,
                                height=25)
        dialogo_robot_3_2.config(bg="dark sea green")

        numero_pagina = Label(tercera_ventana, text="2/2")
        numero_pagina.config(bg="dark sea green")
        numero_pagina.place(x=0, y=0, width=30, height=20)

        # VENTANA FICUS

        def ficus_ventana():
            ficus_ventana = Toplevel()
            ficus_ventana.title("Aplicación")
            ficus_ventana.geometry("360x660")
            ficus_ventana.config(bg="yellow green")
            ficus_ventana.resizable(width=False, height=False)
            tercera_ventana.withdraw()

            dialogo_robot_f_1 = Label(ficus_ventana, font="Arial 17",
                                      text="¿Qué te gustaría saber?")
            dialogo_robot_f_1.config(bg="dark sea green")
            dialogo_robot_f_1.place(anchor="c", relx=0.5, y=40, width=250,
                                    height=30)

            boton_atras = Button(ficus_ventana,
                                 text="Atrás",
                                 command=lambda: [ficus_ventana.destroy(),
                                                  tercera_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(ficus_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [ficus_ventana.destroy(),
                                   tercera_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

            # RIEGO FICUS

            def riego_f_ventana():
                riego_f_ventana = Toplevel()
                riego_f_ventana.title("Aplicación")
                riego_f_ventana.geometry("360x660")
                riego_f_ventana.config(bg="yellow green")
                riego_f_ventana.resizable(width=False, height=False)
                ficus_ventana.withdraw()

                dialogo_robot_f_2 = Label(riego_f_ventana,
                                          text=RIEGO_FI, font=20)
                dialogo_robot_f_2.config(bg="dark sea green")
                dialogo_robot_f_2.place(anchor="c", relx=0.5, rely=0.105,
                                        width=335, height=125)

                boton_atras = Button(riego_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [riego_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(riego_f_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [riego_f_ventana.destroy(),
                                       ficus_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # INFORMACIÓN FICUS

            def info_f_ventana():
                info_f_ventana = Toplevel()
                info_f_ventana.title("Aplicación")
                info_f_ventana.geometry("360x660")
                info_f_ventana.config(bg="yellow green")
                info_f_ventana.resizable(width=False, height=False)
                ficus_ventana.withdraw()

                dialogo_robot_f_3 = Label(info_f_ventana,
                                          text=INFOR_FI, font=20)
                dialogo_robot_f_3.config(bg="dark sea green")
                dialogo_robot_f_3.place(anchor="c", relx=0.5, rely=0.110,
                                        width=325, height=135)

                boton_atras = Button(info_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [info_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(info_f_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [info_f_ventana.destroy(),
                                       ficus_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # BENEFICIOS FICUS

            def beneficios_f_ventana():
                beneficios_f_ventana = Toplevel()
                beneficios_f_ventana.title("Aplicación")
                beneficios_f_ventana.geometry("360x660")
                beneficios_f_ventana.config(bg="yellow green")
                beneficios_f_ventana.resizable(width=False, height=False)
                ficus_ventana.withdraw()

                dialogo_robot_f_4 = Label(beneficios_f_ventana,
                                          text=BENEFI_F, font=20)
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
                                      command=lambda:
                                      [beneficios_f_ventana.destroy(),
                                       ficus_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # CUIDADOS FICUS

            def cuidados_f_ventana():
                cuidados_f_ventana = Toplevel()
                cuidados_f_ventana.title("Aplicación")
                cuidados_f_ventana.geometry("360x660")
                cuidados_f_ventana.config(bg="yellow green")
                cuidados_f_ventana.resizable(width=False, height=False)
                ficus_ventana.withdraw()

                dialogo_robot_f_5 = Label(cuidados_f_ventana,
                                          text=CUIDAD_F, font=20)
                dialogo_robot_f_5.config(bg="dark sea green")
                dialogo_robot_f_5.place(anchor="c", relx=0.5, rely=0.105,
                                        width=310, height=110)

                boton_atras = Button(cuidados_f_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [cuidados_f_ventana.destroy(),
                                      ficus_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(cuidados_f_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [cuidados_f_ventana.destroy(),
                                       ficus_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # BOTON RIEGO FICUS
            boton_f_riego = Button(ficus_ventana, image=foto_regar,
                                   text="RIEGO", font="Arial 8 bold",
                                   compound="bottom",
                                   command=riego_f_ventana)
            boton_f_riego.config(bg="dark sea green")
            boton_f_riego.place(anchor="c", relx=0.5, y=165, width=115,
                                height=115)

            CreateToolTip(boton_f_riego, text='¡Diversos consejos\n'
                          'para un correcto riego\n'
                          'de tu planta!')

            # BOTON INFORMACION FICUS
            boton_f_info = Button(ficus_ventana, image=foto_informacion,
                                  text="INFORMACIÓN", font="Arial 8 bold",
                                  compound="bottom",
                                  command=info_f_ventana)
            boton_f_info.config(bg="dark sea green")
            boton_f_info.place(anchor="c", relx=0.5, y=290, width=115,
                               height=115)

            CreateToolTip(boton_f_info, text='¡Información variada\n'
                          'e interesante\n'
                          'sobre tu planta!')

            # BOTON BENEFICIOS FICUS

            boton_f_beneficios = Button(ficus_ventana, image=foto_beneficios,
                                        text="BENEFICIOS", font="Arial 8 bold",
                                        compound="bottom",
                                        command=beneficios_f_ventana)
            boton_f_beneficios.config(bg="dark sea green")
            boton_f_beneficios.place(anchor="c", relx=0.5, y=415, width=115,
                                     height=115)

            CreateToolTip(boton_f_beneficios, text='¡Beneficios variados\n'
                          'que te da tu planta!')

            # BOTON CUIDADOS FICUS

            boton_f_cuidados = Button(ficus_ventana, image=foto_cuidados,
                                      text="CUIDADOS", font="Arial 8 bold",
                                      compound="bottom",
                                      command=cuidados_f_ventana)
            boton_f_cuidados.config(bg="dark sea green")
            boton_f_cuidados.place(anchor="c", relx=0.5, y=540, width=115,
                                   height=115)

            CreateToolTip(boton_f_cuidados, text='¡Cuidados específicos\n'
                          'para tu planta!')

        # VENTANA ALOE

        def aloe_ventana():
            aloe_ventana = Toplevel()
            aloe_ventana.title("Aplicación")
            aloe_ventana.geometry("360x660")
            aloe_ventana.config(bg="yellow green")
            aloe_ventana.resizable(width=False, height=False)
            tercera_ventana.withdraw()

            dialogo_robot_a_1 = Label(aloe_ventana, font="Arial 17",
                                      text="¿Qué te gustaría saber?")
            dialogo_robot_a_1.config(bg="dark sea green")
            dialogo_robot_a_1.place(anchor="c", relx=0.5, y=40, width=250,
                                    height=30)

            boton_atras = Button(aloe_ventana,
                                 text="Atrás",
                                 command=lambda: [aloe_ventana.destroy(),
                                                  tercera_ventana.deiconify()])
            boton_atras.config(bg="dark khaki")
            boton_atras.place(x=0, y=638, width=50, height=25)

            boton_cerrar = Button(aloe_ventana,
                                  text="Cerrar",
                                  command=lambda:
                                  [aloe_ventana.destroy(),
                                   tercera_ventana.destroy(),
                                   segunda_ventana.destroy(),
                                   ventana_principal.destroy()])
            boton_cerrar.config(bg="light coral")
            boton_cerrar.place(x=310, y=640, width=50, height=25)

            # RIEGO ALOE

            def riego_a_ventana():
                riego_a_ventana = Toplevel()
                riego_a_ventana.title("Aplicación")
                riego_a_ventana.geometry("360x660")
                riego_a_ventana.config(bg="yellow green")
                riego_a_ventana.resizable(width=False, height=False)
                aloe_ventana.withdraw()

                dialogo_robot_a_2 = Label(riego_a_ventana,
                                          text=RIEGO_AL, font=20)
                dialogo_robot_a_2.config(bg="dark sea green")
                dialogo_robot_a_2.place(anchor="c", relx=0.5, rely=0.105,
                                        width=305, height=125)

                boton_atras = Button(riego_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [riego_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(riego_a_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [riego_a_ventana.destroy(),
                                       aloe_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # INFORMACIÓN ALOE

            def info_a_ventana():
                info_a_ventana = Toplevel()
                info_a_ventana.title("Aplicación")
                info_a_ventana.geometry("360x660")
                info_a_ventana.config(bg="yellow green")
                info_a_ventana.resizable(width=False, height=False)
                aloe_ventana.withdraw()

                dialogo_robot_a_3 = Label(info_a_ventana,
                                          text=INFOR_AL, font=20)
                dialogo_robot_a_3.config(bg="dark sea green")
                dialogo_robot_a_3.place(anchor="c", relx=0.5, rely=0.105,
                                        width=335, height=125)

                boton_atras = Button(info_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [info_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(info_a_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [info_a_ventana.destroy(),
                                       aloe_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # BENEFICIOS ALOE

            def beneficios_a_ventana():
                beneficios_a_ventana = Toplevel()
                beneficios_a_ventana.title("Aplicación")
                beneficios_a_ventana.geometry("360x660")
                beneficios_a_ventana.config(bg="yellow green")
                beneficios_a_ventana.resizable(width=False, height=False)
                aloe_ventana.withdraw()

                dialogo_robot_a_4 = Label(beneficios_a_ventana,
                                          text=BENEFI_A, font=20)
                dialogo_robot_a_4.config(bg="dark sea green")
                dialogo_robot_a_4.place(anchor="c", relx=0.5, rely=0.120,
                                        width=285, height=140)

                boton_atras = Button(beneficios_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [beneficios_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(beneficios_a_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [beneficios_a_ventana.destroy(),
                                       aloe_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # CUIDADOS ALOE

            def cuidados_a_ventana():
                cuidados_a_ventana = Toplevel()
                cuidados_a_ventana.title("Aplicación")
                cuidados_a_ventana.geometry("360x660")
                cuidados_a_ventana.config(bg="yellow green")
                cuidados_a_ventana.resizable(width=False, height=False)
                aloe_ventana.withdraw()

                dialogo_robot_a_5 = Label(cuidados_a_ventana,
                                          text=CUIDAD_A, font=20)
                dialogo_robot_a_5.config(bg="dark sea green")
                dialogo_robot_a_5.place(anchor="c", relx=0.5, rely=0.120,
                                        width=305, height=140)

                boton_atras = Button(cuidados_a_ventana,
                                     text="Atrás",
                                     command=lambda:
                                     [cuidados_a_ventana.destroy(),
                                      aloe_ventana.deiconify()])
                boton_atras.config(bg="dark khaki")
                boton_atras.place(x=0, y=638, width=50, height=25)

                boton_cerrar = Button(cuidados_a_ventana,
                                      text="Cerrar",
                                      command=lambda:
                                      [cuidados_a_ventana.destroy(),
                                       aloe_ventana.destroy(),
                                       tercera_ventana.destroy(),
                                       segunda_ventana.destroy(),
                                       ventana_principal.destroy()])
                boton_cerrar.config(bg="light coral")
                boton_cerrar.place(x=310, y=640, width=50, height=25)

            # BOTON RIEGO ALOE

            boton_a_riego = Button(aloe_ventana, image=foto_regar,
                                   text="RIEGO", font="Arial 8 bold",
                                   compound="bottom",
                                   command=riego_a_ventana)
            boton_a_riego.config(bg="dark sea green")
            boton_a_riego.place(anchor="c", relx=0.5, y=165, width=115,
                                height=115)

            CreateToolTip(boton_a_riego, text='¡Diversos consejos\n'
                          'para un correcto riego\n'
                          'de tu planta!')

            # BOTON INFORMACION ALOE

            boton_a_info = Button(aloe_ventana, image=foto_informacion,
                                  text="INFORMACIÓN", font="Arial 8 bold",
                                  compound="bottom",
                                  command=info_a_ventana)
            boton_a_info.config(bg="dark sea green")
            boton_a_info.place(anchor="c", relx=0.5, y=290, width=115,
                               height=115)

            CreateToolTip(boton_a_info, text='¡Información variada\n'
                          'e interesante\n'
                          'sobre tu planta!')

            # BOTON BENEFICIOS ALOE

            boton_a_beneficios = Button(aloe_ventana, image=foto_beneficios,
                                        text="BENEFICIOS", font="Arial 8 bold",
                                        compound="bottom",
                                        command=beneficios_a_ventana)
            boton_a_beneficios.config(bg="dark sea green")
            boton_a_beneficios.place(anchor="c", relx=0.5, y=415, width=115,
                                     height=115)

            CreateToolTip(boton_a_beneficios, text='¡Beneficios variados\n'
                          'que te da tu planta!')

            # BOTON CUIDADOS ALOE

            boton_a_cuidados = Button(aloe_ventana, image=foto_cuidados,
                                      text="CUIDADOS", font="Arial 8 bold",
                                      compound="bottom",
                                      command=cuidados_a_ventana)
            boton_a_cuidados.config(bg="dark sea green")
            boton_a_cuidados.place(anchor="c", relx=0.5, y=540, width=115,
                                   height=115)

            CreateToolTip(boton_a_cuidados, text='¡Cuidados específicos\n'
                          'para tu planta!')

        # BOTONES TERCERA VENTANA

        foto_ficus = Image.open("‍Ficus.png")
        foto_ficus = foto_ficus.resize((215, 215))
        foto_ficus = ImageTk.PhotoImage(foto_ficus)

        foto_aloe = Image.open("Aloe.png")
        foto_aloe = foto_aloe.resize((215, 215))
        foto_aloe = ImageTk.PhotoImage(foto_aloe)

        texto_ficus = Label(tercera_ventana, text="Género ficus",
                            font="Helvetica 12 italic",
                            background="yellow green")
        texto_ficus.place(anchor="c", relx=0.5, y=105)
        boton_ficus = Button(tercera_ventana,
                             image=foto_ficus,
                             command=ficus_ventana)
        boton_ficus.config(bg="dark sea green")
        boton_ficus.place(anchor="c", relx=0.5, rely=0.3,
                          width=225, height=225)
        boton_ficus.pack(side="top", pady=115)
        texto_aloe = Label(tercera_ventana, text="Género aloe",
                           font="Helvetica 12 italic",
                           background="yellow green")
        texto_aloe.place(anchor="c", relx=0.5, y=370)
        boton_aloe = Button(tercera_ventana,
                            image=foto_aloe,
                            command=aloe_ventana)
        boton_aloe.config(bg="dark sea green")
        boton_aloe.place(anchor="c", relx=0.5, rely=0.75,
                         width=225, height=225)

        boton_cerrar = Button(tercera_ventana,
                              text="Cerrar",
                              command=lambda: [tercera_ventana.destroy(),
                                               segunda_ventana.destroy(),
                                               ventana_principal.destroy()])
        boton_cerrar.config(bg="light coral")
        boton_cerrar.place(x=310, y=640, width=50, height=25)

        boton_atras = Button(tercera_ventana,
                             text="Atrás",
                             command=lambda: [tercera_ventana.destroy(),
                                              segunda_ventana.deiconify()])
        boton_atras.config(bg="dark khaki")
        boton_atras.place(x=0, y=638, width=50, height=25)

        segunda_ventana.withdraw()
        tercera_ventana.mainloop()

    # BOTONES SEGUNDA VENTANA

    foto_epipremnum = Image.open("Epi.png")
    foto_epipremnum = foto_epipremnum.resize((215, 215))
    foto_epipremnum = ImageTk.PhotoImage(foto_epipremnum)

    foto_coryphanta = Image.open("Cory.png")
    foto_coryphanta = foto_coryphanta.resize((215, 215))
    foto_coryphanta = ImageTk.PhotoImage(foto_coryphanta)

    texto_epipremnum = Label(segunda_ventana, text="Género epipremnum",
                             font="Helvetica 12 italic",
                             background="yellow green")
    texto_epipremnum.place(anchor="c", relx=0.5, y=105)
    boton_epipremnum = Button(segunda_ventana,
                              image=foto_epipremnum,
                              command=epipremnum_ventana)
    boton_epipremnum.config(bg="dark sea green")
    boton_epipremnum.place(anchor="c", relx=0.5, rely=0.3,
                           width=225, height=225)
    boton_epipremnum.pack(side="top", pady=115)
    texto_coryphanta = Label(segunda_ventana, text="Género coryphanta",
                             font="Helvetica 12 italic",

                             background="yellow green")
    texto_coryphanta.place(anchor="c", relx=0.5, y=370)
    boton_coryphanta = Button(segunda_ventana,
                              image=foto_coryphanta,
                              command=coryphanta_ventana)
    boton_coryphanta.config(bg="dark sea green")
    boton_coryphanta.place(anchor="c", relx=0.5, rely=0.75,
                           width=225, height=225)

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
                           text="Siguiente página",
                           command=ventana_3)
    boton_sig_pag.config(bg="dark khaki")
    boton_sig_pag.place(x=50, y=638, width=100, height=25)

    ventana_principal.withdraw()
    segunda_ventana.mainloop()

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
