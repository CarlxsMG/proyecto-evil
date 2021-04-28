
inventario=[]
print("Un pasillo largo y angosto poco iluminado.")
print("\n")
print("Conforme lo recorres va ganando en tamaño, por el pasaje resuena un llanto débil")
print("con tono desesperado, parece que la voz sale de una entrada en el lateral del pasillo casi llegando al final.")
print("\n")
print("Al llegar encuentras a un viejo y pequeño elfo encadenado, el cual te suplica que lo liberes y podrá ofrecerte sus vienes comerciables.")
print("\n")

while True:
    print("Pasillo:")
    print("1. Salir")
    print("2. Inspeccionar")
    op=int(input("Seleccione una opción:"))

    if op == 1:
        exit

    if op == 2:
        print("En el fondo de la sala aparece un elfo")
        print("1. Acercarse al elfo")
        op2=int(input("Seleccione una opción:"))

        if op2 == 1:
            print("Se ha acercado usted al elfo, ¿Qué desea hacer?")
        while True:
            print("1. Hablar")
            print("2. Liberar")
            print("3. Salir")

            op21=int(input("Selecciona una opción:"))

            if op21 == 1:

            
                print("\n")

            
                print("Opción 1:  ¿Quién eres? ")
                print("Opción 2: ¿Porque estás aquí?")
                print("Opción 3: ¿Cómo puedo ayudarte?")
                preg=int(input("Seleccione una opción:"))

                if preg == 1:
                    print("\n")
                    npc="NPC: Soy un humilde comerciante que ofrece sus mercancías a aventureros y malhechores."
                    print(npc)
                    print("\n")
                if preg == 2:
                    print("\n")
                    npc="NPC: Bueno, me adentré aquí en busca de nuevas mercancías para vender e hice enfadar talvez a quien no debía. Si pudieras ayudarme tengo un objeto que podría desbloquear tu camino hasta el tesoro que anhelas"
                    print(npc)
                    print("\n")
                if preg == 3:
                    print("\n")
                    npc="NPC: Para abrir esta cerradura necesitarás encontrar una llave custodiada en una caja mágica"
                    print(npc)
                    print("\n")

            if op21 == 2:
                if "llave" not in inventario:
                    print("No puedes liberar al elfo, necesitas una llave")
                    
                else:
                    print("Tiene la llave en el inventario, Has podido liberar al elfo!!")
                
            if op21 == 3:
                break
