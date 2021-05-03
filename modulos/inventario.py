
class Inventario:
    
    def __init__(self,capacidad):
        self._capacidad = capacidad
        self._inventario = []
        

    def añadirObjeto(self,item):

        item = str(item).upper()
        if item not in self._inventario:
            self._inventario.append(item)
        else:
            print("No puedo agregar al inventario el mismo objeto.")

        self._historial = self._inventario[:]

    def verObjetos(self):


        import os
        clear = lambda: os.system("cls")
        clear()

        print("\u001b[31m-----INVENTARIO-----\u001b[0m","\u001b[34m")
        print('\n'.join(self._inventario)+"\u001b[0m") 
        print("\u001b[31m--------------------\u001b[0m")
        print("\u001b[0m")
    

    def historial(self):
         
        return self._historial

    def buscarObjeto(self,object):

        objecto = str(objecto).upper()
        for x in self._inventario:
            if x == objecto:
                print("\u001b[31m" + objecto,"ya está en el inventario."+"\u001b[0m")
                return True
                break
               
                


