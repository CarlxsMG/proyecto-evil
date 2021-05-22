
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

        espacios = 0
        for elemento in range(len(self._inventario)):
            espacios += len(self._inventario[elemento])

        print("\u001b[31m----------INVENTARIO---------\u001b[0m")
        for x in range(len(self._inventario)):
            print("|        "+"\u001b[34m"+self._inventario[x] + "\u001b[0m"+(" " * (19 - len(self._inventario[x]) ) ) +"|")

        print("|\u001b[0m"+"\u001b[31m---------------------------\u001b[0m"+"|")
        print("\u001b[0m")
    

    def historial(self):
         
        return self._historial

    def buscarObjeto(self,object):

        objecto = str(object).upper()
        for x in self._inventario:
            if x == objecto:
                print("\u001b[31m" + objecto,"ya está en el inventario."+"\u001b[0m")
                return True
                break
               



