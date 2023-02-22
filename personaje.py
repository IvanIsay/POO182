class Personaje:
    
    # agregamos el constructor del personaje
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre=nom
        self.altura= alt
    
    #metodos
    def correr(self,status):
        if(status):
            print("El personaje "+ self.nombre +" esta corriendo")
        else:
            print("El personaje "+ self.nombre +" se detuvo")
            
            
    def lanzarGranadas(self):
        print("El personaje "+ self.nombre +" lanzo granada")
        
    def recargarArma(self,municiones):
        cargardor=10
        cargardor= cargardor+ municiones
        print("El armar recargada tiene "+ str(cargardor) + " balas")