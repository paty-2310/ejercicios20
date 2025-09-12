print("\n\n-------------MENU-------------\n\n") 

print("\n a continuacion se le mostrara algunas opciones del menu para que eliga ") 

menu = input("\n1.AREPA REINA PEPIADA.\n2.PABELLON CRIOLLO.\n3.PATACON.\n\nelija una opcion:  ").upper() 
if menu == "AREPA" or menu == "1" : 
    print("\nsu arepa va en camino\n") 
elif menu == "PABELLON" or menu == "2" : 
    print("\nsu pabellon va en camino\n") 
else : 
    print("su patacon va en camino.") 