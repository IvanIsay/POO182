from tkinter import Tk,Button,Frame,messagebox,simpledialog

#5. agregar funcion de mensaje
def mostarmensaje():
    messagebox.showinfo("Informacion","Te informo que todo fallo con exito")
    messagebox.showerror("Error","Perdon te falle!!")
    print(messagebox.askokcancel("Pregunta"," Seguro que quieres guardar algo"))
    respuesta= simpledialog.askstring("Pregunta:","¿Cual es tu nombre?")
    print(respuesta)
    
#6.Funcion agregar Botones 
def agregarBoton():
    botonVerde.config(text="+",bg="green",fg="white")
    botonNuevo= Button(seccion3, text="Boton Nuevo")
    botonNuevo.pack()
    





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
botonAzul= Button(seccion1,text="boton azul",fg="blue",command=mostarmensaje)
botonAzul.place(x=60,y=60,width=100, height=60)

botonNegro= Button(seccion2,text="boton negro",bg="black",fg="white")
botonNegro.grid(row=0,column=0)

botonAmarillo= Button(seccion2,text="boton amarillo",bg="#dbdb04")
botonAmarillo.grid(row=1,column=1)


botonVerde= Button(seccion3,text="boton verde",fg="green",command=agregarBoton)
botonVerde.pack()

#.4Posicionamiento de los Widgets


#Metodo Main para la ejecicion del Ventana
ventana.mainloop()