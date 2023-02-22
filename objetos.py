from personaje import *

#1. Solicitamos los datos para los objetos

print("")
print("### Solicitud Datos Heroe ###")
especieH= input("Escribe la especie del Heroe")
nombreH= input("Escribe la nombre del Heroe")
alturaH= float(input("Escribe la altura del Heroe"))
recargarH= int(input("ingresa las balas para el Heroe"))

print("")
print("### Solicitud Datos Villano ###")
especieV= input("Escribe la especie del Villano: ")
nombreV= input("Escribe la nombre del Villano:")
alturaV= float(input("Escribe la altura del Villano: "))
recargarV= int(input("ingresa las balas para el Villano"))


#2. Creamos los objetos
Heroe= Personaje(especieH,nombreH,alturaH)
Villano= Personaje(especieV,nombreV,alturaV)


#3. usamos los atributos Heroe y villano

print("")
print("### atributos y Metodos de Heroe ###")
print("El personaje se llama "+ Heroe.nombre)
print("pertenece a la especie"+ Heroe.especie)
print("y una altura de  "+ str(Heroe.altura))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargarH)



print("")
print("### atributos y Metodos del villano ###")

print("El personaje se llama "+ Villano.nombre)
print("pertenece a la especie"+ Villano.especie)
print("y una altura de  "+ str(Villano.altura))
Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargarV)


#4. usar los Metodos

