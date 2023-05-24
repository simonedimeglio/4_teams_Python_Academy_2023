"""
RELEASE 2.00
Fare una ToDoList che abbia un sistema CRUD (Create, Read, Update, Delete)
riguardo la gestione di task da parte di un utente.
Aggiungere alle Task le seguenti caratteristiche:
-la priorità,
-data di scadenza,
-stato di attività 
"""
################################### AREA APPUNTI DI SVILUPPO ##################################################

# CLASSE OGGETTI TASK:
# ogni task deve avere il contenuto,
#                      la scadenza (entro quando va completata la task ?),
#                      stato di attività (completata, non completata),
#                      priorita (Alta, Media, Bassa)


"""
INDICE:

RIGA 35  - CLASSI
RIGA 119 - FUNZIONI DI AUSILIO
RIGA 199 - FUNZIONI DI CRUD
RIGA 266 - FUNZIONI DI NAVIGAZIONE
RIGA 442 - AREA DEMO
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
    # attributi di classe
    lista_task = []

    # metodo costruttore
    def __init__(self):
        pass

    # aggiunge una task alla lista
    def create(self, task):
        self.lista_task.append(task)
    
    # stampa le task contenute nella lista
    def read(self):
        """Esplora la lista contenuta nell'oggetto ListaTask,
        per ogni oggetto in lista, recupera l'indice che quell'oggetto occupa in lista,
        e stampalo insieme ai dati dell'oggetto stesso"""
        for task in self.lista_task:
            index = str(self.lista_task.index(task) + 1)
            print(index + ' ' + task.to_string()) # to_string è un metodo dell'oggetto Task

    # aggiorna la task nella lista (per la modifica completa)
    def update(self, task, contenuto, scadenza):
        task.contenuto = contenuto
        task.scadenza = scadenza

    # cancella la task nella lista
    def delete(self, indice):
        self.lista_task.remove(self.lista_task[indice - 1])


##################################     FUNZIONI DI AUSILIO     ######################################

# funzione per richiere in input una data
def richiesta_data_e_ora():
    print("Ora ci occupiamo della data. Inserisci solo numeri interi!")
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
            global datatime
            # trasformo stringa in data
            datatime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            break
        except:
            if tipo_errore == 1:
                print("Errore: è stata inserita una data o un'ora non valida. Per favore, riprova.\n")
            if tipo_errore == 0:
                print("Errore: inserire numero intero. Riprova!\n")
        
    return datatime


# funzione per aggiungere dettagli alle task:
def aggiungiDettagliTask(task_creato):
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
def modifica_completa(x):
    contenuto = input('Inserisci il nuovo contenuto: ')
    data = richiesta_data_e_ora()
    aggiungiDettagliTask(to_do_list.lista_task[x])
    # modifico gli attributi contenuto, scadenza e priorita
    to_do_list.update(to_do_list.lista_task[x], contenuto, data)
    print('Hai aggiornato la task con successo.')


# Controllo uscita
def controllo_uscita(scelta):
    if scelta.lower().strip() == 'exit':
        print ("La richiesta corrente è stata annullata. Torno indietro!")
        return True
    else:
        return False


################################   FUNZIONI DI CRUD    ###################################

# funzione per aggiungere task
def aggiungi():
    while True:
        contenuto = input('Inserisci contenuto (exit per uscire): ')
        # controllo per tornare indietro se l'input è 'exit'
        if controllo_uscita(contenuto):
            break
        else:
            data = richiesta_data_e_ora()
            task_creato = Task(contenuto,data)
            aggiungiDettagliTask(task_creato)
            to_do_list.create(task_creato)
            print('Hai inserito correttamente la task nella lista')
            break


# funzione per visualizzare task
def visualizza():
    to_do_list.read()


# funzione per modificare lo status di una task
def modifica_status():
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
                to_do_list.lista_task[x].update_status()
                print('Ti faccio rivisualizzare la task aggiornata:')
                print(scelta + '.' + to_do_list.lista_task[x].to_string())
                break
            except:
                print('Errore: Hai inserito un input non valido.')
                print("Inserisci il numero corrispondente al Task di cui vuoi modificare lo status.\n")


# funzione per eliminare task
def elimina():
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


############################   FUNZIONI DI NAVIGAZIONE MENU   ################################
 

# Switch della modifica parziale
def switch_modifica_parziale(x):
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
                    to_do_list.lista_task[x].update_contenuto(contenuto)
                    print('Ti faccio rivisualizzare la task aggiornata:')
                    print(str(x+1) + '.' + to_do_list.lista_task[x].to_string())
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
                    to_do_list.lista_task[x].update_scadenza(data)
                    print('Ti faccio rivisualizzare la task aggiornata:')
                    print(str(x+1) + '.' + to_do_list.lista_task[x].to_string())
                    break
                else:
                    print("La scelta selezionata non esiste. Riprova")
                
        elif scelta_modifica2 == '3':
            # modifico priorita e stampo
            aggiungiDettagliTask(to_do_list.lista_task[x])
            print('Ti faccio rivisualizzare la task aggiornata:')
            print(str(x+1) + '.' + to_do_list.lista_task[x].to_string())

        else:
            print("Errore, l'opzione da te selezionata non esiste")

# Switch per modificare una task
def switch_modifica():
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
                task_corrente = to_do_list.lista_task[x]
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
                modifica_completa(x)
                break
            elif scelta_modifica == '2':
                # vado a modifica parziale
                switch_modifica_parziale(x)
                break
            else:
                print("\nErrore: l'opzione da te selezionata non esiste.")
                print("Indica un numero intero tra 0 e 2.\n")
        
# Switch di navigazione menu
def switch_navigazione_task():  
    accensione = True
    
    while accensione:
        print("\nBenvenuto nell' App della To Do List.")
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
            aggiungi()
            
        elif scelta == '2':
            # Visualizza le task nella to do list
            if len(to_do_list.lista_task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere visualizzate.')
            else:           
                visualizza()

        elif scelta == '3':
            # Elimina una task esistente
            if len(to_do_list.lista_task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere eliminate.')
            else:           
                elimina()

        elif scelta == '4':
            # Aggiornare la task
            if len(to_do_list.lista_task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere aggiornate.')
            else:
                switch_modifica()
    
        elif scelta == '5':
            # Aggiornare lo status della task
            if len(to_do_list.lista_task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere aggiornate sullo status.')
            else:
                modifica_status()

        else:
            #opzione inesistente
            print("Errore: l'opzione da te selezionata non esiste")
            print("Inserisci un numero intero compreso tra 0 e 5 senza spazi, grazie.\n")


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
            switch_navigazione_task()
        # opzione inesistente
        else:
            print("Errore: l'opzione da te selezionata non esiste")
            print("Inserisci un numero intero tra 0 e 1 senza spazi, grazie.\n")


############################## AREA DEMO ############################

# inizializzazione dell' oggetto di lista task  
task1 = Task('Esposizione App', '2023-05-25 09:00')
task1.priorita = 'Alta'
task2 = Task('Fare la spesa', '2023-05-25 18:15')
to_do_list = ListaTask()  
to_do_list.lista_task = [task1, task2]

switch_accesso()
