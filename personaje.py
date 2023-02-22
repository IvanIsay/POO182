class Personaje:
    
    #atributos
    especie="Humano"
    nombre="MasterChief"
    altura=2.70
    
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
        print("El armar recargada tiene "+ cargardor + " balas")