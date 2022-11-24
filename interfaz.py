"""""
IMPORTACIONES
"""""
import tkinter as tk
from tkinter import messagebox

"""""
FUNCIONES
"""""


def PantallaCompleta():
    ancho_pantalla = raiz.winfo_screenwidth()
    alto_pantalla = raiz.winfo_screenheight()
    raiz.geometry("{}x{}".format(ancho_pantalla,
                                 alto_pantalla))


def CerrarApp():
    opcion = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")

    if opcion == "yes":
        raiz.quit()


def CambiarAMenu():
    ventana_bienvenida.pack(fill='both', expand="True")
    ventana_bienvenida.config(bg=FONDO)

    ventana_epi.pack_forget()
    ventana_cory.pack_forget()

    boton_cory.pack()
    boton_epi.pack()


def CambiarACory():
    ventana_cory.pack(fill='both', expand="True")
    ventana_cory.config(bg=FONDO)

    ventana_bienvenida.pack_forget()
    ventana_epi.pack_forget()
    boton_epi.pack_forget()


def CambiarAEpy():
    ventana_epi.pack(fill='both', expand="True")
    ventana_epi.config(bg=FONDO)

    ventana_bienvenida.pack_forget()
    ventana_cory.pack_forget()
    boton_cory.pack_forget()


"""""
CONSTANTES
"""""

FUENTE = ("times", 20, "normal")
FONDO = "#52BE80"

"""""
PROCESAMIENTO
"""""

raiz = tk.Tk()

raiz.title("Aplicación LAB")  # SE DEFINE EL NOMBRE DE LA VENTANA
raiz.iconbitmap("app.ico")  # SE DEFINE UN ICONO PARA LA APP

raiz.config(bg=FONDO)

"""""
CONFIGURACIÓN DE LAS VENTANAS
"""""

PantallaCompleta()

ventana_bienvenida = tk.Frame(raiz)
ventana_epi = tk.Frame(raiz)
ventana_cory = tk.Frame(raiz)


ventana_bienvenida.config(bg=FONDO)
ventana_epi.config(bg=FONDO)
ventana_cory.config(bg=FONDO)


ventana_bienvenida.pack()


texto_bienvenida = tk.Label(ventana_bienvenida,
                            text="\nBienvenido a nuestra app",
                            font=FUENTE)
texto_epi = tk.Label(ventana_epi,
                     text="\n¿Qué desea saber del género epipremnum?",
                     font=FUENTE)
texto_cory = tk.Label(ventana_cory,
                      text="\n¿Qué desea saber del género coryphantha?",
                      font=FUENTE)

texto_bienvenida.config(bg=FONDO)
texto_epi.config(bg=FONDO)
texto_cory.config(bg=FONDO)

texto_bienvenida.pack(pady=20)
texto_epi.pack(pady=20)
texto_cory.pack(pady=20)


"""""
BOTONES
"""""

valor_boton_epi = tk.IntVar()

boton_inicio = tk.Button(raiz, text="Menú Principal",
                         font=FUENTE, command=CambiarAMenu, textvariable=1)
boton_epi = tk.Button(raiz, text="Epipremnum",
                      font=FUENTE, command=CambiarAEpy)
boton_cory = tk.Button(raiz, text="Coryphantha",
                       font=FUENTE, command=CambiarACory)

boton_inicio.config(width=15, height=1, cursor="HAND1")
boton_epi.config(width=15, height=1, cursor="HAND1")
boton_cory.config(width=15, height=1, cursor="HAND1")


boton_inicio.place(x=0, y=0)
boton_epi.pack(pady=20)
boton_cory.pack(pady=20)

boton_inicio


"""""
BARRA PARA CERRAR LA APP
"""""

barra_menu = tk.Menu(raiz)
raiz.config(menu=barra_menu)

menu_salir = tk.Menu(barra_menu, tearoff=0)
menu_salir.add_command(label="Salir", command=CerrarApp)

barra_menu.add_cascade(label="Cerrar aplicación", menu=menu_salir)

raiz.mainloop()
