import tkinter as tk

ventana = tk.Tk()
ventana.title("Aplicación")
ventana.resizable(width=True,height=True)
ventana.config(width=400,   height=300)

bienvenida = tk.Label(
    ventana,
    text = "Hola ¿Cómo estás?\n"
    "Podemos darte infomación de las siguientes plantas :",
    anchor= tk.NW,
    foreground ="black",
    background = "green"
    )
bienvenida.place(
    x=0,
    y=0
    )



boton_1= tk.Button(
    text= "1)Epipremnum",
    width= 20,
    height=3)
boton_1.place(
    x=0,
    y=100
    )

boton_2= tk.Button(
    text= "2)Coryphanta",
    width= 20,
    height=3)

boton_2.place(
    x=0,
    y=200
    )

ventana.mainloop()

