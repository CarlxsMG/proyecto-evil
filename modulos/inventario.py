
class Inventario:
    
    def __init__(self):
        self._capacidad = 10
        self._inventario = []

    def addItem(self,item):

        item = str(item).upper()
        if item not in self._inventario:
            self._inventario.append(item)
        else:
            print("No puedo agregar al inventario el mismo objeto.")


    def showItems(self):
        
        import os
        clear = lambda: os.system("cls")
        clear()
        print("\u001b[34m")
        print('\n'.join(self._inventario),"\u001b[0m")
    

    def searchItem(self,object):

        object = str(object).upper()
        for x in self._inventario:
            if x == object:
                print("\u001b[31m" + object,"ya está en el inventario."+"\u001b[0m")
                return True
                break
               
                






inventario = Inventario()

inventario.addItem("moneda de oro")
inventario.addItem("moneda de plata")
inventario.addItem("llave oxidada")
inventario.addItem("caja")
inventario.showItems()

# inventario.searchItem("caja")


