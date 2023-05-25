from Persona import Persona
from Controllo import controllo
from Account import controllo_esistenza_dipendente
from Dipendente import Dipendente


class Gestore(Persona):
    
    password = "12345678"

    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)

    # Metodo che riguarda il gestore: Possibilità di aggiungere un dipendente
    def aggiungi_dipendente(self, lista_dipendenti):
        print("Stai aggiungendo un nuovo dipendente")
        nome = str(input("Inserisci il nome: ")).strip()
        cognome = str(input("Inserisci il cognome: ")).strip()
        # Controlla se l'utente esiste giá
        if controllo_esistenza_dipendente(nome, cognome, lista_dipendenti) != "inesistente":
            print("L'utente inserito è giá presente")
            return None

        inquadramento_aziendale = input("Inserisci l'inquadramento aziendale: ").strip()
        reparto = input("Inserisci il reparto: ").strip()
        # Verificare se l'inquadramento aziendale e reparto chiesti all'utente siano compresi nel range scelto
        if controllo(1, 9, inquadramento_aziendale) and controllo(1, 5, reparto):
            dipendente = Dipendente(
                nome, cognome, int(inquadramento_aziendale), int(reparto)
            )
            lista_dipendenti.append(dipendente)
            print("Dipendente aggiunto con successo")
        else:
            print(
                "Errore,devi inserire un valore\n"
                "tra 0 e 8 per l'inquadramento aziendale\n "
                "e un valore tra 1 e 4 per il reparto\n"
            )

    # Metodo per gestore: modifica dipendente
    def modifica_dipendente(self, lista_dipendenti):
        self.report(lista_dipendenti)
        flag = False
        while not flag:
            indice_dipendente = input("Seleziona il dipendente da modificare: \n").strip()
            if controllo(0, len(lista_dipendenti), indice_dipendente):
                indice_dipendente_int = int(indice_dipendente)
                flag = True

        flag = False
        while not flag:
            print("Scegli l'opzione desiderata: ")
            print("1. Modifica nome")
            print("2. Modifica cognome")
            print("3. Modifica reparto")
            print("4. Modifica inquadramento aziendale")
            print("5. Esci")
            variabile = input().strip()

            if variabile == "1":
                nuovo_nome = str(input("Inserisci il nuovo nome: ")).strip()
                lista_dipendenti[indice_dipendente_int].nome = nuovo_nome

            elif variabile == "2":
                nuovo_cognome = str(input("Inserisci il nuovo cognome: ")).strip()
                lista_dipendenti[indice_dipendente_int].cognome = nuovo_cognome

            elif variabile == "3":
                flag2 = False
                while not flag2:
                    nuovo_reparto = input("Inserisci il nuovo reparto\n").strip()
                    if controllo(1, 5, nuovo_reparto):
                        flag2 = True
                lista_dipendenti[indice_dipendente_int].reparto = int(nuovo_reparto)

            elif variabile == "4":
                flag2 = False
                while not flag2:
                    nuovo_inquadramento_aziendale = input(
                        "Inserisci il nuovo inquadramento aziendale\n"
                    ).strip()
                    if controllo(1, 9, nuovo_inquadramento_aziendale):
                        flag2 = True
                lista_dipendenti[indice_dipendente_int].inquadramento_aziendale = int(
                    nuovo_inquadramento_aziendale
                )

            elif variabile == "5":
                flag = True
                continue

            else:
                print("Scegliere un comando valido")
                continue

            print("Modifica avvenuta con successo")
            print(lista_dipendenti[indice_dipendente_int].to_string())


    # Metodo per gestore: rimuovi dipendenti
    def rimuovi_dipendente(self, lista_dipendenti):
        self.report(lista_dipendenti)
        indice_dipendente = (
            input("Seleziona il dipendente che hai deciso di rimuovere\n").strip()
        )
        
        if controllo(0, len(lista_dipendenti), indice_dipendente):
                lista_dipendenti.pop(int(indice_dipendente))
                print("Dipendente rimosso")
        else:
            print("Inserisci un comando valido")


    # Metodo per gestore: stampa il report dipendenti
    def report(self, lista_dipendenti):
        if lista_dipendenti == []:
            print("Non ci sono dipendenti nella lista")
        else:
            print("Report:")
            for iteratore, elemento in enumerate(lista_dipendenti):
                print(f"{iteratore}. {elemento.to_string()}")

