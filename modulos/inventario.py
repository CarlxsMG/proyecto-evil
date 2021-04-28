


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

        print('\n'.join(self._inventario))
    

    def searchItem(self,object):

        object = str(object).upper()
        for x in self._inventario:
            if x == object:
                print(object,"ya está en el inventario.")
                return True
                break
                
                






inventario = Inventario()

inventario.addItem("moneda de oro")
inventario.addItem("moneda de plata")
inventario.addItem("llave oxidada")
inventario.addItem("caja")
inventario.showItems()


