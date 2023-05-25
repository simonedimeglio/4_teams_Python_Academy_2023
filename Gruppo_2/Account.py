# -------------------------------------------- FUNZIONI --------------------------------------------------------
from Menu import menu_dipendente

    
# Accedi
def login(lista_dipendenti):
    # Chiedi e controlla la pasword
    nome = input("Digita nome\n").strip()
    cognome = input("Digita cognome\n").strip()
    n_utente = controllo_esistenza_dipendente(nome, cognome, lista_dipendenti)
    if n_utente == "inesistente":
        print("\nErrore: dipendente non registrato.\n")
    else:
        # Crea nuova password
        if lista_dipendenti[n_utente].primo_ingresso == True:
            print("È il tuo primo ingresso, digita la tua nuova password")
            password_digitata = input()
            # Modifica la passsword
            lista_dipendenti[n_utente].password = password_digitata
            lista_dipendenti[n_utente].primo_ingresso = False

        # Controlla password
        if controllo_password_dipendente(lista_dipendenti, n_utente):  
            # Esegui fino che l'utente non ha finito
            esci = False
            while not esci:
                esci = menu_dipendente(n_utente, lista_dipendenti)

#Funzione che controlla se un Dipendente sia registrato o meno nel sistema
def controllo_esistenza_dipendente(nome, cognome, lista_dipendenti):
    # Cicla
    for iteratore, dipendente in enumerate(lista_dipendenti):
        if dipendente.nome == nome and dipendente.cognome == cognome:
            print("L'utente esiste")
            return iteratore
    else:
        return "inesistente"


# Funzione per verificare che l'utente digiti la password corretta
def controllo_password_dipendente(lista_dipendenti, n_utente):
    print("Stai entranto come dipendente, digita la password")
    password_digitata = input()

    if password_digitata == lista_dipendenti[n_utente].password:
        print("\nPassword corretta.")  # inserire menù dipendente
        return True

    else:
        print("\nPassword errata.")
        return False

