import tkinter as tk

ventana = tk.Tk()
ventana.title("Aplicación")
ventana.resizable( width = True, height = True )
ventana.config( width = 640,   height = 480 )

bienvenida = tk.Label(
    ventana,
    text = "Hola ¿Cómo estás?\n"
    "Podemos darte infomación de las siguientes plantas :",
	font = "times"
    )
bienvenida.place(
    x = 0,
    y = 0
    )



boton_1= tk.Button(
    text = "1)Epipremnum",
    width = 20,
    height = 3)
boton_1.place(
    x = 0,
    y = 100
    )

boton_2= tk.Button(
    text = "2)Coryphanta",
    width = 20,
    height = 3)
boton_2.place(
    x = 0,
    y = 200
    )

boton_cerrar = tk.Button(
	ventana,
	text = "Cerrar",
	command = ventana.destroy,
	width = 5,
	height = 1,
)
boton_cerrar.place(
	x = 595,
	y = 455,
)
ventana.mainloop()

