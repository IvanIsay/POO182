from tkinter import Tk,Button,Frame

#1. Generar una ventana
ventana=Tk()
ventana.title("Ejemplo 3 Frames")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1= Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana,bg="gray")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana,bg="purple")
seccion3.pack(expand=True,fill='both')

#3. Agregamos botones 
botonAzul= Button(seccion1,text="boton azul",fg="blue")
botonAzul.place(x=60,y=60,width=100, height=60)

botonNegro= Button(seccion2,text="boton negro",bg="black",fg="white")
botonNegro.grid(row=0,column=0)

botonAmarillo= Button(seccion2,text="boton amarillo",bg="yellow")
botonAmarillo.grid(row=1,column=1)


botonVerde= Button(seccion3,text="boton verde",fg="green")
botonVerde.pack()




#Metodo Main para la ejecicion del Ventana
ventana.mainloop()