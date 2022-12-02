import tkinter as tk

# Ventana principal
principal = tk.Tk()
principal.title("Aplicación")
principal.geometry("360x660")
principal.resizable(width=False, height=False)


# Ventana epipremnum
def ventana_epipremnum():
    # Configuración ventana epipremnum
    epipremnum = tk.Toplevel()
    epipremnum.title("Aplicación")
    epipremnum.geometry("360x660")
    epipremnum.resizable(width=False, height=False)
    principal.withdraw()

# Ventana información
    def info1():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        epipremnum.withdraw()
        info = tk.Label(
            info_e,
            text="La Epipremnum, tambien conocida como potos,\n \
            perteneciente a la familia Araceae\n"
            "puede tener tallos de hasta 4cm de diámetro!,\n \
            esta no florece de manera natural,"
            "si no, de manera inducida.",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Botón Atrás
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), epipremnum.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Boton cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             epipremnum.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
        )

    # Ventana cuando es optimo
    def info2():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        epipremnum.withdraw()
        info = tk.Label(
            info_e,
            text="Los riegos deben ser frecuentes en la epoca cálida,\n"
            "manteniendo humedad alta rociando las hojas y se deben reducir\n"
            "a partir de otoño,en invierno se deben mantener escasos,\n"
            "la temperatura ideal del agua pararegarla son los 20°C a 25°C",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Botón Atrás
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), epipremnum.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             epipremnum.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            relx=0.5,
            rely=1,
        )

    # Ventana benficios
    def info3():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        epipremnum.withdraw()
        info = tk.Label(
            info_e,
            text="Este genero tan curioso de plantas,\
            es perfecto para poder decorar\n"
            "cualquier parte de tu casa, como también ayuda\n"
            "considerablemente a eliminar muchas de las toxinas del aire\n"
            "que no podemos apreciar a simple vista!",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Boton Atras
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), epipremnum.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             epipremnum.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
            )

    # Ventana cuidados
    def info4():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        epipremnum.withdraw()
        info = tk.Label(
            info_e,
            text="A esta curiosa planta, le gusta mucho mantenerse en un\n"
            "ambiente humedo, es por esto que siempre debes manter la tierra\n"
            "de esa manera,evita mantenerla a \
            luz directa del sol ya que esto\n"
            "no le gusta, mantenla cerca de la ventana \
            evitando lo anterior dicho",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Botón Atrás
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), epipremnum.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )

        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             epipremnum.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
        )

    # Mensaje principal ventana epipremnum
    mensaje = tk.Label(
        epipremnum,
        text="Que deseas saber acerca del género epipremnum",
        font="times"
    )
    mensaje.place(
        x=35,
        y=0
    )
    # Boton información
    boton_1 = tk.Button(
        epipremnum,
        text="Información",
        command=info1,
        width=32,
        height=4
    )
    boton_1.place(
        anchor="c",
        relx=0.5,
        y=100
    )
    # Botón cuándo es óptimo
    boton_2 = tk.Button(
        epipremnum,
        text="Cuando es optimo regar la planta",
        command=info2,
        height=4,
        width=32,
    )
    boton_2.place(
        anchor="c",
        relx=0.5,
        y=200
    )
    # Botón beneficios
    boton_3 = tk.Button(
        epipremnum,
        text="Beneficios de tener la planta ",
        command=info3,
        height=4,
        width=32,
    )
    boton_3.place(
        anchor="c",
        relx=0.5,
        y=300
    )
    # Bóton cuidados
    boton_4 = tk.Button(
        epipremnum,
        text="Cuidados de la planta ",
        command=info4,
        height=4,
        width=32,
    )
    boton_4.place(
        anchor="c",
        relx=0.5,
        y=400
    )
    # Botón Atrás
    boton_atras = tk.Button(
        epipremnum,
        text="Atrás",
        command=lambda: [epipremnum.destroy(), principal.deiconify()],
        padx=42,
        pady=10)
    boton_atras.place(
        anchor="sw",
        relx=0,
        rely=1,
    )
    # Botón cerrar
    boton_cerrar = tk.Button(
        epipremnum,
        text="Cerrar",
        command=lambda: [epipremnum.destroy(), principal.destroy()],
        padx=40,
        pady=10)
    boton_cerrar.place(
        anchor="s",
        relx=0.5,
        rely=1,
    )


# Ventana coryphanta
def ventana_coryphanta():
    # Configuración ventana coryphanta
    coryphanta = tk.Toplevel()
    coryphanta.title("Coryphanta")
    coryphanta.geometry("360x660")
    principal.withdraw()

    def info1():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        coryphanta.withdraw()
        info = tk.Label(
            info_e,
            text="La Coryphanta, tambien conocida como cactus,\n"
            "es un genero nativo de Mexico, siendo uno de los mas extensos.\n"
            "Esta puede crecer aproximadamente de 5-6 cm,\n"
            "cuando se desarrolla forma una flor central grande",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Botón Atrás
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), coryphanta.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             coryphanta.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
        )

    # Ventana cuando es optimo
    def info2():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        coryphanta.withdraw()
        info = tk.Label(
            info_e,
            text="Los riegos deben ser de forma moderada en primavera\n"
            "y verano, siempre manteniendo el suelo seca de esta misma,\n"
            "en la epoca fria, los riegos deben suspenderse\n"
            "en pos del cuidado de la planta",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )

        # Botón Atrás
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), coryphanta.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             coryphanta.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
        )

    # Ventana beneficios
    def info3():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        coryphanta.withdraw()
        info = tk.Label(
            info_e,
            text="Este puntiagudo genero de plantas, son excelentes\n"
            "purificadores de aire, siendo esto perfecto a la hora de\n"
            "cuidar nuestra salud, tambien son plantas que requieren\n"
            "muy poco cuidado debido a su poca necesidad de agua,\n"
            "siendo estas perfectas para gente que no puede dedicar\n"
            "todo su tiempo en una planta",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Botón Atrás
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), coryphanta.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             coryphanta.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
        )

    # Ventana cuidados
    def info4():
        info_e = tk.Toplevel()
        info_e.geometry("360x660")
        info_e.title("Información")
        info_e.resizable(width=False, height=False)
        coryphanta.withdraw()
        info = tk.Label(
            info_e,
            text="A esta pequeña planta, le encanta tener luz directa,\n"
            "aunque tambien pueden recibir por periodos causando el mismo\n"
            "efecto de estar todo el dia en la luz solar,\n"
            "la tierra organica mezclada con fibra de coco,\n"
            "hojas secas, corteza y turba,\
            es lo mejor para su perfecto desarrollo",
            padx=10,
            pady=10
        )
        info.place(
            anchor="n",
            relx=0.5,
            rely=0
        )
        # Botón Atras
        boton_atras = tk.Button(
            info_e,
            text="Atrás",
            command=lambda: [info_e.destroy(), coryphanta.deiconify()],
            padx=42,
            pady=10)
        boton_atras.place(
            anchor="sw",
            relx=0,
            rely=1,
        )
        # Botón cerrar
        boton_cerrar = tk.Button(
            info_e,
            text="Cerrar",
            command=lambda: [info_e.destroy(),
                             coryphanta.destroy(), principal.destroy()],
            padx=40,
            pady=10)
        boton_cerrar.place(
            anchor="s",
            relx=0.5,
            rely=1,
        )
    mensaje = tk.Label(
        coryphanta,
        text="Que deseas saber acerca del género coryphanta",
        font="times"
    )
    mensaje.place(
        x=35,
        y=0
    )
    # Botón información
    boton_1 = tk.Button(
        coryphanta,
        text="Información",
        command=info1,
        height=4,
        width=32,
    )
    boton_1.place(
        anchor="c",
        relx=0.5,
        y=100
    )
    # Botón cuándo es óptimo
    boton_2 = tk.Button(
        coryphanta,
        text="Cuando es optimo regar la planta",
        command=info2,
        height=4,
        width=32,
    )
    boton_2.place(
        anchor="c",
        relx=0.5,
        y=200
    )
    # Botón beneficios
    boton_3 = tk.Button(
        coryphanta,
        text="Beneficios de tener la planta ",
        command=info3,
        height=4,
        width=32,
    )
    boton_3.place(
        anchor="c",
        relx=0.5,
        y=300
    )
    # Botón cuidados
    boton_4 = tk.Button(
        coryphanta,
        text="Cuidados de la planta ",
        command=info4,
        height=4,
        width=32,
    )
    boton_4.place(
        anchor="c",
        relx=0.5,
        y=400
    )
    # Botón atrás
    boton_atras = tk.Button(
        coryphanta,
        text="Atrás",
        command=lambda: [coryphanta.destroy(), principal.deiconify()],
        padx=42,
        pady=10)
    boton_atras.place(
        anchor="sw",
        relx=0,
        rely=1)
    # Boton cerrar
    boton_cerrar = tk.Button(
        coryphanta,
        text="Cerrar",
        command=lambda: [coryphanta.destroy(), principal.destroy()],
        padx=40,
        pady=10)
    boton_cerrar.place(
        anchor="s",
        relx=0.5,
        rely=1)


# Mensaje ventana principal
bienvenida = tk.Label(
    principal,
    text="Hola ¿Cómo estás?\n"
    "Podemos darte infomación de las siguientes plantas :",
    font="times"
    )
bienvenida.place(
    x=35,
    y=0
    )


# Botón epiprmnum
boton_epipremnum = tk.Button(
    text="1)Epipremnum",
    height=4,
    width=32,
    command=ventana_epipremnum,
    )
boton_epipremnum.place(
    anchor="c",
    relx=0.5,
    y=100
    )
# Botón Coryphanta
boton_coryphanta = tk.Button(
    text="2)Coryphanta",
    command=ventana_coryphanta,
    height=4,
    width=32)
boton_coryphanta.place(
    anchor="c",
    relx=0.5,
    y=200
    )
# Botón cerrar
boton_cerrar_principal = tk.Button(
    principal,
    text="Cerrar",
    command=principal.destroy,
    padx=45,
    pady=10)
boton_cerrar_principal.place(
    anchor="s",
    relx=0.5,
    rely=1,
)
principal.mainloop()
