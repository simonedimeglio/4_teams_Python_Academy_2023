"""
RELEASE 1.0
Fare una ToDoList che abbia un sistema CRUD (Create, Read, Update, Delete)
riguardo la gestione di task da parte di un utente

"""
################################### AREA APPUNTI DI SVILUPPO ##################################################
# funzione switch che avvia app
# menu: C - R - U - D

# CLASSE OGGETTI TASK:
# ogni task deve avere il contenuto                    


# CLASSE OGGETTI TASK-list
# Liste di task
# conviene creare una classe con metodi che vadano a fare lavoro di CRUD


################################### AREA DI IMPLEMENTAZIONE ##################################################

# Classe Task
class Task:

    def __init__(self, contenuto):
        self.contenuto = contenuto #string

    def to_string(self):
        return f'Contenuto: {self.contenuto} '
    # Modifica di contenuto
    def update_contenuto(self, nuovo_contenuto):
        self.contenuto = nuovo_contenuto

# Classe ListaTask
class ListaTask:
    nome =''
    lista_task = []

    def __init__(self):
        pass
    
    # crea un task nella listaTask
    def create(self, task):
        self.lista_task.append(task)
    
    # Legge i task nella listaTask
    def read(self):
        for task in self.lista_task:
            index = str(self.lista_task.index(task) + 1)
            print(index + ' ' + task.to_string()) # to_string è un metodo dell'oggetto Task

    # Aggiorna il conteunto del task selezionato nella lista task
    def update(self, task, contenuto):
        task.contenuto = contenuto

    # Elimina il task dalla listaTask
    def delete(self, indice):
        self.lista_task.remove(self.lista_task[indice - 1])

# funzione per aggiungere task (aggiungere controlli)
def aggiungi():
    contenuto = input('Inserisci contenuto: ')
    task_creato = Task(contenuto)
    to_do_list.create(task_creato)
    print('Hai inserito correttamente la task nella lista')

# funzione per visualizzare task
def visualizza():
    to_do_list.read()

# funzione per eliminare task
def elimina():
    while True:
        # Eliminare task dalla to do list
        print('Ti faccio visualizzare le task nella To do List: ')
        to_do_list.read()
        scelta = input('Indica il numero della task da eliminare: ')
        # Costrutto per gestire gli errori di input di 'scelta'
        try:
            to_do_list.delete(int(scelta))
            print('Hai eliminato la task con successo.')
            break
        except:
            print('Errore, inserire un numero corrispondente alla task che vuoi eliminare\n')

# funzione per modificare task completamente (aggiungere controlli)
def modifica_completa():
    print('Ti faccio visualizzare le task nella To do List: ')
    to_do_list.read()
    while True:
        scelta = input('Indica il numero della task da aggiornare: ')
        # Costrutto per gestire gli errori di input di 'scelta'
        try:
            x = int(scelta) - 1
            contenuto = input('Inserisci il nuovo contenuto: ')
            to_do_list.update(to_do_list.lista_task[x], contenuto)
            print('Hai aggiornato la task con successo.')
            break
        except:
            print('Errore, inserire un numero intero come scelta')

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
            print("Errore, l'opzione da te selezionata non esiste\n")

# Switch di navigazione menu
def switch_navigazione_task():  
    accensione = True
    
    while accensione:
        print("\nBenvenuto nell' App della To Do List")
        print("1. Aggiungi una task")
        print("2. Visualizza tutte le task")
        print("3. Elimina Task")
        print("4. Modifica la Task")
        print("0. Torna indietro")
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == '0':
            # Richiesta tornare indietro al menu di accesso
            accensione = False

        elif scelta == '1':
            # Aggiungi una task contenuto, scadenza, stato_attivita, priorita
            aggiungi()
            
        elif scelta == '2':
            # Visualizza le task nella to do list
            if len(to_do_list.lista_task) == 0:
                print('Non ci sono Task salvate finora che possano quindi essere visualizzate.')
            else:
                print("Questi sono i task salvati:")           
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
                modifica_completa()

        else:
            # opzione inesistente
            print("Errore, l'opzione da te selezionata non esiste")

# inizializzazione dell' oggetto di lista task per demo
task1 = Task('Programmazione')
task2 = Task('Fare la spesa')
to_do_list = ListaTask()  
to_do_list.create(task1)
to_do_list.create(task2)

switch_accesso()