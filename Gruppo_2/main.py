from Dipendente import Dipendente
from Gestore import Gestore
from Account import login, controllo_esistenza_dipendente, controllo_password_dipendente
from Menu import menu_dipendente, menu_gestore


lista_dipendenti = []

gestore = Gestore("Luca", "Onesto")
dip1 = Dipendente("Mario", "Rossi", 1, 2)
dip2 = Dipendente("Luigi", "Bianchi", 3, 4)
dip1.genera_password(4)
dip2.genera_password(4)
lista_dipendenti.append(dip1)
lista_dipendenti.append(dip2)

# Inizia I/O: ripeti richiesta scelta per output errati, altrimenti esci
flag = False
while not flag:
    print("\nScegli il tipo di account: ")
    print("1. Account gestore")
    print("2. Account dipendente")
    print("3. Esci")

    scelta = input().strip()

    if scelta == "1":
        # Chiedi e controlla la password
        print("Stai entranto come gestore, digita la password")
        password_digitata = input()
        if password_digitata != gestore.password:
            print("Password errata! Chiusura del programma in corso...")
        else:
            # Esegui azioni fino che l'utente non ha finito
            esci = False
            while not esci:
                esci = menu_gestore(gestore, lista_dipendenti)

    elif scelta == "2":
        login(lista_dipendenti)
    
    elif scelta == "3":
        print("esci")
        flag = True

    else:
        print("Scegliere un comando valido")


