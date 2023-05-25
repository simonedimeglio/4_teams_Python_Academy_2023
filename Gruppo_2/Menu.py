# MENU scelte dipendente: permette di visualizzare la propria retribuzione o di aggiungere ore di ferie
def menu_dipendente(n_utente, lista_dipendenti):
    print("\nScegli l'opzione desiderata: ")
    print("1. Visualizza la propria retribuzione")
    print("2. Aggiungi giorni ferie")
    print("3. Esci")

    variabile = input().strip()

    if variabile == "1":
        lista_dipendenti[n_utente].calcola_stipendio()

    elif variabile == "2":
        lista_dipendenti[n_utente].settaFerie()

    elif variabile == "3":
        return "esci"

    else:
        print("Scegliere un comando valido")


# MENU scelta gestore: Permette la gestione del sistema CRUD ,di Stampare il report dei dipendenti o di Uscire dal Sistema
def menu_gestore(gestore, lista_dipendenti):
    print("\nScegli l'opzione desiderata: ")
    print("1. Aggiungi dipendenti")
    print("2. Modificare un dipendente")
    print("3. Rimuovi dipendenti")
    print("4. Report")
    print("5. Esci")

    variabile = input().strip()

    if variabile == "1":
        gestore.aggiungi_dipendente(lista_dipendenti)

    elif variabile == "2":
        gestore.modifica_dipendente(lista_dipendenti)

    elif variabile == "3":
        gestore.rimuovi_dipendente(lista_dipendenti)

    elif variabile == "4":
        gestore.report(lista_dipendenti)

    elif variabile == "5":
        return "esci"  # True

    else:
        print("Scegliere un comando valido")

