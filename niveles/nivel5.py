import random
moneda=0
cont=0
inventario=[]
intentos=3


print("\n")

print("Tras recorrer el pasillo llega usted a una gran sala no demasiado iluminada custodiada por un Golem de piedra durmiente, en el suelo puede encontrar numerosos cadáveres distribuidos por él.") 
print("En esta sala se puede apreciar varios arboles, arbustos y rocas, al fondo encontrarás un altar donde se encuentra Orbe. Para llegár necesitarás acertar un puzzle para llegar camino")

print("\n")

while intentos>0:
    salir=False
    print("Esta usted en la sala principal:")
    
    print("1. Salir")
    print("2. Inspeccionar")



    op=int(input("Selecciona una opción:"))



    if op == 1:
        exit

    elif op == 2:
        
        print("Hemos inspeccionado y alrededor de la sala encontramos un Golem y un Orbe:")
        while   intentos>0 and salir == False:
            

            print("1. Acercarse al Golem")
            print("2. Acercarse al Orbe")

            op2=int(input("Selecciona una opción:"))

            if op2 == 1:
                
                
                while True:

                    print("¿Que desea hacer con el Golem?")

                    print("1. Inspeccionar")
                    print("2. Golpear")
                    print("3. Ignorar")
                    

                    op3=int(input("Selecciona una opción:"))
                    
                    if op3 == 1:

                        if cont >= 1:

                            print ("No se encuentra nada relevante cerca del Golem")
                            pass

                        else:

                            print("Cerca del Golem has encontrado varias monedas")
                            moneda+=20
                            cont+=1
                            print("Has añadido 20 monedas en tu bolsa, en total tienes",moneda)

                        
                        

                    elif op3 == 2:
                        print("Has seleccionado Golpear")
                        
                        num_aleatorio=random.randint(1,11)
                        

                        if num_aleatorio == 5:
                            print("Has podido sobrevivir del Golem")
                            pass

                        else:
                            print("El Golem te ha matado")
                            #muerto=True
                            intentos=0
                            break
                
                    elif op3 == 3:
                        print("Has seleccionado Ignorar")
                        salir=True
                        break
                
                
            
                
            

            if op2 == 2:
                
                print("Para poder alcanzar al Orbe tienes que resolver este puzzle. A continuación te encontrarás con unas rocas y un arbol, deberás de seleccionar el camino adecuado:")
                while   intentos>0 and salir == False:
                    print("PISTA1: Es un objeto duro, resistente y robusto que no tiene vida:")
                    print("1. Rocas")
                    print("2. Arbol Principal")
                    elec1=int(input("Seleccione el camino:"))
                    if elec1==1:
                        print("Has acertado, vamos a pasar por el siguiente acertijo")
                        print("PISTA2: Es un ser viviente con un reluciente color verde y se encuentra entre otros dos seres vivientes:")
                        print("1)Arbol izquierdo")
                        print("2)Arbusto")
                        print("3)Arbol derecho")

                        elect2=int(input("Selecciona el camino:"))

                        if elect2 == 1:
                            intentos-=1
                            if intentos > 0:
                                print("Has fallado, no puedes avanzar por el arbol izquierdo,  te quedan ",intentos,"intentos")
                            else:
                                print("Ya no te quedan intentos")
                        
                        elif elect2 == 2:
                        
                            print("Has acertado, ahora vamos a la última prueba")
                            print("PISTA3: Es un ser viviente con una determinada altura y repleto de hojas que se situa en dirección positiva en horizontal:")
                            print("1)Arbol izquierdo")
                            print("2)Arbusto")
                            print("3)Rocas")
                            print("4)Arbol derecho")

                            elect3=int(input("Selecciona un camino:"))
                            
                            if elect3 == 1:
                                intentos-=1
                                if intentos > 0:
                                    print("Has fallado, no puedes avanzar en el arbol izquierdo, te quedan ",intentos,"intentos")
                                else:
                                    print("Ya no te quedan intentos")
                        
                            elif elect3 == 2:
                                intentos-=1
                                if intentos > 0:
                                    print("Has fallado, no puedes avanzar en el arbusto, te quedan ",intentos,"intentos")
                                else:
                                    print("Ya no te quedan intentos")
                            elif elect3 == 3:
                                intentos-=1
                                if intentos > 0:

                                    print("Has fallado, no puedes avanzar entre las rocas, te quedan ",intentos,"intentos")
                                else:
                                    print("Ya no te quedan intentos")
                            
                            elif elect3 == 4:
                                print("Has acertado el camino, has podido llegar al Orbe")

                                
                                if "Orbe" not in inventario:
                                    inventario.append("Orbe")
                                    print("Has obtenido el Orbe")
                
                                else:
                                    print("Ya se encuentra el Orbe en tu inventario")

                                    
                                while True:
                                    print("1. Inspeccionar")
                                    print("2. Volver a la entrada de la sala")

                                    op21=int(input("Selecciona una opción:"))
                      
                    
                                    if op21 == 1:
                                        if "Calavera_dorada" not in inventario:
                            
                                            print("Desde esa posición puedes ver detrás del Golem una pila de cadáveres y parece que algo reluce entre ellos.")

                                            inventario.append("Calavera_dorada")
                                            print("Has obtenido la calavera dorada")

                                        else:
                                            print("Desde esa posición puedes ver detrás del Golem una pila de cadáveres, no hay nada más relevante")
                        
                                    elif op21 == 2:
                                            print("Volver a la sala principal")
                                            salir=True
                                            break
                                
                        
                            
                        
                                    
                        elif elect2 == 3:
                            intentos-=1
                            if intentos > 0:
                                print("Has fallado, no puedes avanzar por el arbol derecho, te quedan ",intentos,"intentos")
                            else:
                                print("Ya no quedan intentos")
                
                
                    elif elec1==2:
                        intentos-=1
                        if intentos > 0:
                            print("Has fallado, no puedes avanzar por el arbol principal, te quedan ",intentos,"intentos")
                        else:
                            print("Ya no te quedan intentos")
   
                
if intentos == 0:
    print("Has muerto, GAME OVER!")                  
                  

   
        
