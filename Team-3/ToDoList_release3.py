"""
RELEASE 3.00
- Aggiunta la possibilità di avere più liste, ognuna con le proprie task
- Aggiunta la possibilità di non specificare la data (verrà inserita la data di oggi e l'ora corrente)
"""
################################### AREA APPUNTI DI SVILUPPO ##################################################

"""
INDICE:

RIGA 25  - CLASSI
RIGA 109 - FUNZIONI DI AUSILIO
RIGA 198 - FUNZIONI DI CRUD PER LE TASK
RIGA 265 - FUNZIONI DI CRUD PER LE LISTE
RIGA 313 - FUNZIONI DI NAVIGAZIONE
RIGA 557 - AREA DEMO
"""

############################### AREA DI IMPLEMENTAZIONE ############################################


# importo libreria per gestire le date
import datetime

######################################   CLASSI   ##################################################

# Classe Task
class Task:
    # stato della task se completato o non -- Default: non completato
    # priorita -- Default : Media
    status = False
    priorita = 'Media'

    # Metodo costruttore
    def __init__(self, contenuto, scadenza):
        self.contenuto = contenuto # string
        self.scadenza = scadenza  # data di scadenza task

    # Visualizzazione Task
    def to_string(self):
        return f'Contenuto: {self.contenuto}\n  Scadenza: {self.scadenza}\n  Status: {self.read_status()}\n  Priorità : {self.priorita}\n'
    
    # Modifica dello status come completata (nella modifica parziale)
    def update_status(self):
        if self.status == True:
            self.status = False
            print('Hai segnalato la task come Non Completata')
        else:
            self.status = True
            print('Hai segnalato la task come Completata')

    # Lettura dello status della task
    def read_status(self):
        if self.status:
            return 'Completato'
        else:
            return 'Non Completato'
        
    # Modifica di priorita (nella modifica parziale)
    def update_priorita(self, valore):
        # controlla che il valore sia nei valori concessi
        if valore in ['Alta', 'Media', 'Bassa']:
            self.priorita = valore
        else:
            print('Non è stato possibile modificare la priorità del task.')

    # Modifica del contenuto della task (nella modifica parziale)
    def update_contenuto(self, nuovo_contenuto):
        self.contenuto = nuovo_contenuto

    # Modifica della scadenza (nella modifica parziale)
    def update_scadenza(self, nuova_scadenza):
        self.scadenza = nuova_scadenza
    

# Classe ListaTask
class ListaTask:

    # metodo costruttore
    def __init__(self, nome):
        self.nome = nome
        self.task = []

    # aggiunge una task alla lista
    def create(self, task_da_aggiungere):
        self.task.append(task_da_aggiungere)
    
    # stampa le task contenute nella lista
    def read(self):
        """Esplora la lista contenuta nell'oggetto ListaTask,
        per ogni oggetto in lista, recupera l'indice che quell'oggetto occupa in lista,
        e stampalo insieme ai dati dell'oggetto stesso"""
        print(self.nome)
        for task in self.task:
            index = str(self.task.index(task) + 1)
            print(index + ' ' + task.to_string()) # to_string è un metodo dell'oggetto Task

    # aggiorna la task nella lista (per la modifica completa)
    def update(self, task, contenuto, scadenza):
        task.contenuto = contenuto
        task.scadenza = scadenza

    # cancella la task nella lista
    def delete(self, indice):
        self.task.remove(self.task[indice - 1])



##################################     FUNZIONI DI AUSILIO     ######################################

# funzione per richiere in input una data
def richiesta_data_e_ora():
    print("Ora ci occupiamo della data. Inserisci solo numeri interi!")
    while True:    
        print('Vuoi personalizzare la data?')
        risposta = input("Si/No (con no verrà inserita l'ora di oggi): ")
        # controllo sull'input 'risposta'
        if risposta.lower().strip() == 'si':
            while True:
                try:
                    # per gestire il tipo di errore: se l'input non può essere convertito in intero tipo_errore rimane 0
                    tipo_errore = 0
                    # trasformo tutto in int per evitare inserimento di stringhe   
                    anno = int(input("Inserisci anno: "))
                    mese = int(input("Inserisci mese: "))
                    giorno = int(input("Inserisci giorno: "))
                    ora = int(input("Inserisci ora: "))
                    minuti = int(input("Inserisci minuti: "))
                    # se la conversione a intero è corretta per tutti gli input, tipo_errore diventa 1 e l'unico errore possibile è una data o un'ora non valida
                    tipo_errore = 1
                    # concateno la data con -
                    data_str = '-'.join([str(anno), str(mese), str(giorno)])
                    # concateno l'ora con :
                    ora_str = ':'.join([str(ora), str(minuti)])
                    # concateno data e ora con spazio
                    datetime_str = ' '.join([data_str,ora_str])
                    # variabile globale che voglio ritornare alla fine della funzione
                    global data_scelta
                    # trasformo stringa in data
                    data_scelta = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
                    break
                except:
                    if tipo_errore == 1:
                        print("Errore: è stata inserita una data o un'ora non valida. Per favore, riprova.\n")
                    if tipo_errore == 0:
                        print("Errore: inserire numero intero. Riprova!\n")
            return data_scelta
        elif risposta.lower().strip() == 'no':
            print("Hai scelto di non inserire dettagli priorità")
            return datetime.datetime.utcnow()
        else: 
            print("Errore, scelta non disponibile")

    
# funzione per aggiungere dettagli alle task:
def aggiungi_dettagli_task(task_creato):
    while True:    
        print('Vuoi personalizzare la priorità?')
        risposta = input('Si/No: ')
        # controllo sull'input 'risposta'
        if risposta.lower().strip() == 'si':
            while True:
                valore = input('Inserisci il valore della priorità tra i seguenti (Alta, Media , Bassa): ').lower().strip().capitalize()
                # controllo sull'input 'valore'
                if valore in ['Alta', 'Media', 'Bassa']:
                    # aggiorno priorita
                    task_creato.update_priorita(valore)
                    break
                else:
                    print('Per favore inserisci una parola tra le seguenti : Alta/Media/Bassa')
            break
        elif risposta.lower().strip() == 'no':
            print("Hai scelto di non inserire dettagli priorità")
            break
        else: 
            print("Errore, scelta non disponibile")


# funzione per modificare task completamente
def modifica_completa(x, to_do_list):
    contenuto = input('Inserisci il nuovo contenuto: ')
    data = richiesta_data_e_ora()
    aggiungi_dettagli_task(to_do_list.task[x])
    # modifico gli attributi contenuto, scadenza e priorita
    to_do_list.update(to_do_list.task[x], contenuto, data)
    print('Hai aggiornato la task con successo.')


# Controllo uscita
def controllo_uscita(scelta):
    if scelta.lower().strip() == 'exit':
        print ("La richiesta corrente è stata annullata. Torno indietro!")
        return True
    else:
        return False


################################   FUNZIONI DI CRUD TASK   ###################################

# funzione per aggiungere task
def aggiungi_task(to_do_list):
    while True:
        contenuto = input('Inserisci contenuto (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(contenuto):
            break
        else:
            data = richiesta_data_e_ora()
            task_creato = Task(contenuto,data)
            aggiungi_dettagli_task(task_creato)
            to_do_list.create(task_creato)
            print('Hai inserito correttamente la task nella lista')
            break


# funzione per visualizzare le task
def visualizza_task(to_do_list):
    to_do_list.read()


# funzione per modificare lo status di una task
def modifica_status(to_do_list):
    print('Ti faccio visualizzare le task nella To do List: ')
    to_do_list.read()
    while True:
        scelta = input('Indica il numero della task di cui vuoi modificare lo status (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(scelta):
            break
        else:
            # Costrutto per gestire gli errori di input di 'scelta'
            try:
                x = int(scelta) - 1
                # aggiorno status
                to_do_list.task[x].update_status()
                print('Ti faccio rivisualizzare la task aggiornata:')
                print(scelta + '.' + to_do_list.task[x].to_string())
                break
            except:
                print('Errore: Hai inserito un input non valido.')
                print("Inserisci il numero corrispondente al Task di cui vuoi modificare lo status.\n")


# funzione per eliminare task
def elimina_task(to_do_list):
    while True:
        print('Ti faccio visualizzare le task nella To do List: ')
        to_do_list.read()
        scelta = input('Indica il numero della task da eliminare (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(scelta):
            break
        else:
        # Costrutto per gestire gli errori di input di 'scelta'
            try:
                # Elimino task dalla lista
                to_do_list.delete(int(scelta))
                print('Hai eliminato la task con successo.')
                break
            except:
                print('Errore: Hai inserito un input non valido.')
                print("Inserisci il numero corrispondente al Task che vuoi eliminare.\n")


################################   FUNZIONI DI CRUD LIST  ###################################

# funzione per aggiungere lista
def aggiungi_lista():
    while True:
        nome_lista = input("Aggiungi il nome della lista (exit per uscire): ")
        if controllo_uscita(nome_lista):
            break
        else:
            # creazione e inserimento nell'elenco
            lista_creata = ListaTask(nome_lista)
            elenco_liste.append(lista_creata)
            # modifica della lista
            switch_navigazione_task(elenco_liste[-1])
            break


# visualizza l'elenco delle liste
def visualizza_liste():
    for liste in elenco_liste:
        index = str(elenco_liste.index(liste) + 1)
        print(index + '. ' + liste.nome + ':') # to_string è un metodo dell'oggetto Task
        for task in liste.task:
            print(' -', task.contenuto)


# elimina una lista esistente
def elimina_lista():
    while True:
        print('Ti faccio visualizzare le liste nella To do List: ')
        # visualizza tutte le liste contenute nell'elenco liste
        visualizza_liste()
        scelta = input('Indica il numero della lista da eliminare (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(scelta):
            break
        else:
        # Costrutto per gestire gli errori di input di 'scelta'
            try:    
                indice_lista = int(scelta) - 1
                # Elimino lista
                del elenco_liste[indice_lista]
                print('Hai eliminato la lista con successo.')
                break
            except:
                print('Errore: Hai inserito un input non valido.')
                print("Inserisci il numero corrispondente alla Lista che vuoi eliminare.\n")

############################   FUNZIONI DI NAVIGAZIONE MENU   ################################
 

# Switch della modifica parziale
def switch_modifica_parziale(x, to_do_list):
    while True:
        print("\nQuesta è l'area di modifica parziale:")
        print("1. Modifica contenuto")
        print("2. Modifica scadenza")
        print("3. Modifica priorita")
        print("0. Torna indietro")
        scelta_modifica2 = input("Inserisci la tua scelta: ")
        if scelta_modifica2 == '0':
            # torno indietro
            break
        elif scelta_modifica2 == '1':
            while True:
                contenuto = input('Inserisci contenuto (exit per uscire): ')
                # controllo per tornare indietro se l'input è 'exit'
                if controllo_uscita(contenuto):
                    break
                else:
                    # modifico contenuto e stampo
                    to_do_list.task[x].update_contenuto(contenuto)
                    print('Ti faccio rivisualizzare la task aggiornata:')
                    print(str(x+1) + '.' + to_do_list.task[x].to_string())
                    break
            
        elif scelta_modifica2 == '2':
            while True:
                conferma = input("Sei sicuro di voler modificare la data? (Si/No): ")
                # controllo dell'input 'conferma'
                if conferma.lower().strip() == 'no':
                    print("Hai deciso di non modificare la data")
                    break
                elif conferma.lower().strip() == 'si':
                    # modifico scadenza e stampo
                    data = richiesta_data_e_ora()
                    to_do_list.task[x].update_scadenza(data)
                    print('Ti faccio rivisualizzare la task aggiornata:')
                    print(str(x+1) + '.' + to_do_list.task[x].to_string())
                    break
                else:
                    print("La scelta selezionata non esiste. Riprova")
                
        elif scelta_modifica2 == '3':
            # modifico priorita e stampo
            aggiungi_dettagli_task(to_do_list.task[x])
            print('Ti faccio rivisualizzare la task aggiornata:')
            print(str(x+1) + '.' + to_do_list.task[x].to_string())

        else:
            print("Errore, l'opzione da te selezionata non esiste")

# Switch per modificare una task
def switch_modifica(to_do_list):
    print('Ti faccio visualizzare le task nella To do List: ')
    to_do_list.read()
    while True:
        scelta_mod = input('Indica il numero della task da aggiornare (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(scelta_mod):
            break
        else:
            # controllo se la scelta è un intero ed esiste nella lista una task di indice x
            try:
                x = int(scelta_mod) - 1
                task_corrente = to_do_list.task[x]
                print('\nTi faccio rivisualizzare la task selezionata:\n')
                print(scelta_mod + '.' + task_corrente.to_string())
                break
            except:
                print("Per favore, inserire numero intero di una task esistente nella lista o exit \n")
    while True:
        # controllo per tornare indietro se l'input è 'exit' : nel caso l'utente voglia uscire questo while non va esplorato
        if controllo_uscita(scelta_mod):
            break
        else:
            print("Questa è l'area di modifica:")
            print("1. Modifica completa di una task")
            print("2. Modifica solo un elemento di una task")
            print("0. Torna indietro")
            scelta_modifica = input("Inserisci la tua scelta: ")
            if scelta_modifica == '0':
                # torno indietro alla switch_navigazione_task
                break
            elif scelta_modifica == '1':
                # vado a modifica completa
                modifica_completa(x, to_do_list)
                break
            elif scelta_modifica == '2':
                # vado a modifica parziale
                switch_modifica_parziale(x, to_do_list)
                break
            else:
                print("\nErrore: l'opzione da te selezionata non esiste.")
                print("Indica un numero intero tra 0 e 2.\n")
        
# Switch di navigazione menu task
def switch_navigazione_task(to_do_list):  
    accensione = True
    
    while accensione:
        print("\nStai modificando la lista:", to_do_list.nome)
        print("1. Aggiungi una task")
        print("2. Visualizza tutte le task")
        print("3. Elimina Task")
        print("4. Modifica la Task")
        print("5. Aggiorna Status della Task")
        print("0. Torna indietro")
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == '0':
            # richiesta tornare indietro al menu di accesso
            accensione = False

        elif scelta == '1':
            # Aggiungi una task contenuto, scadenza, priorita, con stato_attivita = 'Non Completato'
            aggiungi_task(to_do_list)
            
        elif scelta == '2':
            # Visualizza le task nella to do list
            if len(to_do_list.task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere visualizzate.')
            else:           
                visualizza_task(to_do_list)

        elif scelta == '3':
            # Elimina una task esistente
            if len(to_do_list.task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere eliminate.')
            else:           
                elimina_task(to_do_list)

        elif scelta == '4':
            # Aggiornare la task
            if len(to_do_list.task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere aggiornate.')
            else:
                switch_modifica(to_do_list)
    
        elif scelta == '5':
            # Aggiornare lo status della task
            if len(to_do_list.task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere aggiornate sullo status.')
            else:
                modifica_status(to_do_list)

        else:
            #opzione inesistente
            print("Errore: l'opzione da te selezionata non esiste")
            print("Inserisci un numero intero compreso tra 0 e 5 senza spazi, grazie.\n")

# Switch di scelta lista
def switch_scelta_lista():
    while True:
        print('Ti faccio visualizzare le liste nella To do List: ')
        # visualizza tutte le liste contenute nell'elenco liste
        visualizza_liste()
        scelta = input('Indica il numero della lista da gestire (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(scelta):
            break
        else:
        # Costrutto per gestire gli errori di input di 'scelta'
            try:    
                indice_lista = int(scelta) - 1
                # Elimino lista
                switch_navigazione_task(elenco_liste[indice_lista])
                break
            except:
                print('Errore: Hai inserito un input non valido.')
                print("Inserisci il numero corrispondente alla Lista che vuoi gestire.\n")

# Switch di navigazione menu liste
def switch_navigazione_liste():  
    accensione = True

    while accensione:
        print("\nBenvenuto nell' App della To Do List.")
        print("1. Aggiungi una lista")
        print("2. Visualizza tutte le liste")
        print("3. Elimina lista")
        print("4. Modifica la lista")
        print("0. Torna indietro")
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == '0':
            # richiesta tornare indietro al menu di accesso
            accensione = False

        elif scelta == '1':
            # Aggiungi una lista
            aggiungi_lista()
            
        elif scelta == '2':
            # Visualizza le liste nella to do list
            if len(elenco_liste) == 0:
                print("L'elenco delle liste è vuoto, non puoi visualizzare")
            else:           
                visualizza_liste()

        elif scelta == '3':
            # Elimina una lista esistente
            if len(elenco_liste) == 0:
                print("L'elenco delle liste è vuoto, non puoi visualizzare")
            else:           
                elimina_lista()

        elif scelta == '4':
            # Aggiornare la lista
            if len(elenco_liste) == 0:
                print("L'elenco delle liste è vuoto, non puoi visualizzare")
            else:
                switch_scelta_lista()

        else:
            #opzione inesistente
            print("Errore: l'opzione da te selezionata non esiste")
            print("Inserisci un numero intero compreso tra 0 e 4 senza spazi, grazie.\n")

# Switch accesso
def switch_accesso():
    print("\nBenvenuto nell' App della To Do List")
    # ciclo per ripetere la scelta in caso di errore
    while True:
        print("1. Entra")
        print("0. Esci")
        scelta_accesso = input("Inserisci la tua scelta: ")
        # uscita
        if scelta_accesso == '0':
            print("Arrivederci!")
            break
        # navigazione con scelte
        elif scelta_accesso == '1':
            switch_navigazione_liste()
        # opzione inesistente
        else:
            print("Errore: l'opzione da te selezionata non esiste")
            print("Inserisci un numero intero tra 0 e 1 senza spazi, grazie.\n")


############################## AREA DEMO ############################

# inizializzazione dell' oggetto di lista task  
elenco_liste = []
task1 = Task('Esposizione App', '2023-05-25 09:00')
task1.priorita = 'Alta'
task2 = Task('Fare la spesa', '2023-05-25 18:15')
to_do_list1 = ListaTask("Lista1")  
to_do_list1.task = [task1, task2]
elenco_liste.append(to_do_list1)

switch_accesso()
