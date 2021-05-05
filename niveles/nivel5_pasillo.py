
inventario=["llave"]
dinero=15000
comp_liberar=False
ag_t=False
ag_c=False
ag_p=False
ag_am=False

print("Un pasillo largo y angosto poco iluminado.")
print("\n")










while True:
    print("\n")
    print("Usted se encuentra en un pasillo muy oscuro. En uno de los caminos conforme lo recorres va ganando en tamaño, por el pasaje resuena un llanto débil")
    print("\n")
    print("1. Ir hacia la izquierda")
    print("2. Seguir hacia delante")
    print("3. Salir")
    pasillo=int(input("Selecciona el camino:"))

    if pasillo == 3:

        break

        
    elif pasillo == 2:
        print("\n")
        print("Has podido avanzar y acabas de encontrar un portal para acceder a la Sala 5")
        print("\n")
        print("1. Entrar a la Sala 5")
        print("2. Volver")

        pas_recto=int(input("Selecciona una opción:"))

        if pas_recto == 1:
            print("Has entrado a la sala 5")
            break

        elif pas_recto == 2:
            pass
            
    
    elif pasillo == 1:
        print("\n")
        print("Con tono desesperado, parece que la voz sale de una entrada en el lateral del pasillo casi llegando al final.")
        print("\n")
        while True:
            print("\n")
            print("Se está adentrando hacia la sala ¿Que desea hacer?")
            print("\n")
            print("1. Salir")
            print("2. Inspeccionar la sala")
            op=int(input("Seleccione una opción:"))

            if op == 1:

                break
                break

            elif op == 2:
                print("\n")
                print("Al llegar encuentras a un viejo y pequeño elfo encadenado, el cual te suplica que lo liberes y podrá ofrecerte sus vienes comerciables.")
                print("\n")
                print("1. Acercarse al elfo")
                op2=int(input("Seleccione una opción:"))

                if op2 == 1:
                    
                    cont_liberar=0
                    print("\n")
                    print("Se ha acercado usted al elfo, ¿Qué desea hacer?")
                    print("\n")
                    
                    while True:
                        print("1. Hablar")

                        
                        print("2. Liberar")

                        if comp_liberar == True:
                            print("3. Comerciar")
                            

                        print("4. Salir")

                        op21=int(input("Selecciona una opción:"))

                        if op21 == 1:

                            
                            print("\n")
                            print("NPC:Muy buenas señor, acaba de encontrarme en el fondo de la sala")
                            print("\n")
                            
                            while True:
                                print("Opción 1:  ¿Quién eres? ")
                                print("Opción 2: ¿Porque estás aquí?")
                                print("Opción 3: ¿Cómo puedo ayudarte?")
                                print("4. Salir")
                                preg=int(input("Seleccione una opción:"))

                                if preg == 1:
                                    print("\n")
                                    npc="NPC: Soy un humilde comerciante que ofrece sus mercancías a aventureros y malhechores."
                                    print(npc)
                                    print("\n")
                                elif preg == 2:
                                    print("\n")
                                    npc="NPC: Bueno, me adentré aquí en busca de nuevas mercancías para vender e hice enfadar talvez a quien no debía. Si pudieras ayudarme tengo un objeto que podría desbloquear tu camino hasta el tesoro que anhelas"
                                    print(npc)
                                    print("\n")
                                elif preg == 3:
                                    print("\n")
                                    npc="NPC: Para abrir esta cerradura necesitarás encontrar una llave custodiada en una caja mágica"
                                    print(npc)
                                    print("\n")
                                elif preg == 4:
                                    break

                        elif op21 == 2:
                            if "llave" not in inventario:
                                print("No puedes liberar al elfo, necesitas una llave")
                                                   
                            else:
                                if comp_liberar:
                                    print("Ya has liberado al elfo")

                                    
                                else:
                                    
                                    print("Tiene la llave en el inventario, Has podido liberar al elfo!!")
                                    print("\n")
                                    print("NPC: Gracias por liberarme!, como recompensa tienes la oportunidad de poder comerciar conmigo")
                                    print("\n")
                                    print("Ahora que has liberado al elfo puedes comerciar con el ¿Que desea hacer?")
                                    
                                    comp_liberar=True
                                    
                        elif op21 == 3 and comp_liberar:


                            while True:
                                print("\n")
                                print("NPC: Tengo unos cuantos productos que le pueden interesar:")
                                print("\n")
                                if ag_t:
                                    print("1. Túnica (10.000 de oro) AGOTADO")
                                else:          
                                    print("1. Túnica (10.000 de oro)")

                                if ag_c:
                                    print("2. Casco Romano (2.000 de oro) AGOTADO")
                                else:
                                    print("2. Casco Romano (2.000 de oro)")

                                if ag_p:    
                                    print("3. Piedra filosofal (1.000 de oro) AGOTADO")
                                else:
                                    print("3. Piedra filosofal (1.000 de oro)")

                                if ag_am:     
                                    print("4. Amuleto dorado (500 de oro) AGOTADO")
                                else:
                                    print("4. Amuleto dorado (500 de oro)")


                                print("5. Salir")

                                comercio=int(input("Selecciona una opción:"))
                                
                                if comercio == 1:
                                    if ag_t == False:
                                        if dinero >= 10000:
                                            print("Has conseguido la Túnica!!!")
                                            inventario.append("tunica")
                                            dinero-=10000
                                            ag_t=True
                                            print(dinero)

                                        else:
                                            print("No tiene dinero suficiente")
                                    else:
                                        
                                        print("Ya has comprado la túnica")


                                
                                elif comercio == 2:
                                    if ag_c == False:
                                        if dinero >= 2000:
                                            print("Has conseguido el casco romano!!!")
                                            inventario.append("casco_romano")
                                            dinero-=2000
                                            ag_c=True
                                            print(dinero)

                                        else:
                                            print("No tiene dinero suficiente")
                                    else:
                                        print("Ya has comprado el casco romano")



                                
                                elif comercio == 3:
                                    if ag_p == False:
                                        if dinero >= 1000:
                                            print("Has conseguido la piedra filosofal!!!")
                                            inventario.append("piedra_filosofal")
                                            dinero-=1000
                                            ag_p=True
                                            print(dinero)

                                        else:
                                            print("No tiene dinero suficiente")
                                    else:
                                        print("Ya has comprado la piedra filosofal")


                                
                                elif comercio == 4:
                                    if ag_am == False:
                                        if dinero >= 500:
                                            print("Has conseguido el amuleto dorado!!!")
                                            inventario.append("amuleto_dorado")
                                            dinero-=500
                                            ag_am=True
                                            print(dinero)

                                        else:
                                            print("No tiene dinero suficiente")
                                    else:
                                        print("Ya has comprado el amuleto dorado")

                                elif comercio == 5:
                                    break
                        
                            
                    
                        elif op21 == 4:
                            break

    
