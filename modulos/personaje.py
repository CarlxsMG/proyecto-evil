
class Personaje:
    
    def __init__(self,nombre):
        
        self._nombre = nombre
        self._vida = 100   
        

    def __str__(self):

        return "Soy un personaje compuesto de nombre y vida, y tengo metodos de envenamiento, curación y obtención de información de su vida."
        
    def envenenarse(self,tiempo):
        #Le podemos indicar cuanto tiempo en segundos le va a afectar el estado de envenenamiento.
        import time

        for x in range(tiempo):
           if self._vida > 0:
                self._vida -= 1
                time.sleep(1)
            


    def curarse (self,cantidadCuración):
        #Insertamos la cantidad de curación que queremos sumar al personaje.
        if (self._vida + cantidadCuración) > 0 and (self._vida + cantidadCuración) <= 100:
            self._vida += cantidadCuración
        else:
            print("no puede ser curado, la cantida de curación es erronea.")


    def getVida(self):
        #Devuelve y printea la vida del jugador
        print("La vida de",self._nombre ,"es de:",str(self._vida))        
        return self._vida



