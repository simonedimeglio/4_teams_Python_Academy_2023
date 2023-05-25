"""
    Social Network Abstraction
    Il progetto prevede la costruzione di un social network dove e' possibile registrarsi, creare un post,
    commentare un post e aggiungere followers. Al progetto seguira' un upgrade successivo in cui sara' possibile
    definire i livelli di amicizia e visualizzare i post in base ai livelli di amicizia

    Questo progetto nasce dalla voglia di 4 giovani ragazzi di mettersi in gioco e di affrontare una sfida
    di coding lanciatagli dai loro formatori.

    "Abstraction è uno stile di vita"
"""

#Lista Utenti registrati ad Abstraction
lista_utenti_oggetto = []



# E' la classe che viene utilizzare per crear i post degli utenti
# Viene utilizzata all'interno del metodo crea_post della classe Utente
class Post:
    def __init__(self, username, contenuto):
        self.username = username
        self.post_stesso = contenuto
        self.lista_commenti_al_Post =[]

# Questa èla classe principale
# Qui si può creare l'utente con i vari attributi e metodi che saranno utilizzati nel programma

class Utente:

    # Per istanziare gli oggetti Utente
    # L'utente potrà inserire i propi dati
    def __init__(self, username, nome, cognome, password):
        self.username = username
        self.nome = nome
        self.cognome = cognome
        self.password = password
        self.amici_utente = []
        self.homepage_utente = []
        lista_utenti_oggetto.append(self)

    # metodo per cercare attraverso gli indici gli altri oggetti utente nella lista_utenti_oggetto
    def indice_username(self, lista_utenti_oggetto):
        username_look = input('Quale amico vuoi cercare?\n')
        index = False
        for item in range(len(lista_utenti_oggetto)):
            if lista_utenti_oggetto[item].username == username_look:
                index = item
        return index

    # metoto per visualizzare i post pubblicati dall'Utente stesso (Come se fosse il proprio profilo)
    def stampa_home(self):
        print(f'{self.username} home page!')
        
        for i in range(len(self.homepage_utente)):
            print(i, ':', self.homepage_utente[i].post_stesso)
            
            if self.homepage_utente[i].lista_commenti_al_Post == []:
                print()
            else:
                for j in range(len(self.homepage_utente[i].lista_commenti_al_Post)):
                    print(self.homepage_utente[i].lista_commenti_al_Post[j][0], ': ',self.homepage_utente[i].lista_commenti_al_Post[j][1] )
                print()

    # Metodo per visualizzare le persone seguite dall'Utente
    def stampa_amici(self):
        print(f'{self.username} amici!\n')
        if self.amici_utente == []:
            print('Al momento non segui nessuno! \n')
        else:
            for i in range(len(self.amici_utente)):
                print(i, ':', self.amici_utente[i])
                print()

    # Metodo per creare un post. Questo metodo è richiamato nel main del programma,
    # ovvero in Abstraction()
    def crea_post(self):
        contenutoPost = input('Scrivi il tuo post: ')
        mio_post = Post(self.username, contenutoPost)
        self.homepage_utente.append(mio_post)
        self.stampa_home()
        print()

    # Metodo per cancellare un post presente nel nostro profilo.
    # Questo metodo è richiamato nel main del programma, ovvero in Abstraction()
    def cancella_post(self):
        if self.homepage_utente != []:
            self.stampa_home()
            try:
                index_to_pop = int(input('Digita il numero del post da cancellare'))
                self.homepage_utente.pop(index_to_pop)
                print('Bravo, hai cancellato il tuo post!')
                print()
            except:
                print('Post non trovato.')

        else:
            print('Non hai post nella home!')
            print()

    # Metodo per seguire un altro utente.
    # Qui si aggiunge l'username dell'utente da seguire a una lista asseclata all'attributo amici_utente
    # Questo metodo è richiamato nel main del programma, ovvero in Abstraction()
    def following(self, lista_utenti_oggetto=lista_utenti_oggetto):
        index = self.indice_username(lista_utenti_oggetto)
        # amico = input('inserisci il nome del tuo amico: ')
        if index != False:
            self.amici_utente.append(lista_utenti_oggetto[index].username)
            print(self.amici_utente)
            print()
        else:
            print('Questo utente non esiste.')
            print()

    # Metodo per rimuovere un utente dalla lista dei "seguiti" (following)
    # Questo metodo è richiamato nel main del programma, ovvero in Abstraction()
    def un_following(self):
        if self.amici_utente == []:
            print('Al momento non segui nessun utente! \n')
        else:
            try:
                for i in range(len(self.amici_utente)):
                    print(i, ':', self.amici_utente[i])
                exAmico = input("Inserisci il nome dell'utente che non vuoi più seguire: ")
                self.amici_utente.remove(exAmico)
                print(self.amici_utente)
                print()
            except:
                print("L'utente non è nella tua lista di amici")
                print()

    # Per commentare un post di un Utente registrato in Abstract(), anche i tuoi stessi post
    # Questo metodo è richiamato nel main del programma, ovvero in Abstraction()
    def commenta_post(self, utenteX):
        for i in range(len(utenteX.homepage_utente)):
            print(i, ':', utenteX.homepage_utente[i].post_stesso)
            for j in utenteX.homepage_utente[i].lista_commenti_al_Post:
                print(j[0], ': ', j[1])

        try:
            index_post = int(input("Digita l'indice del post da commentare: "))
            print()
            commento = input('Digita il commento al post: ')
            print()

            utenteX.homepage_utente[index_post].lista_commenti_al_Post.append([self.username, commento])

            print(utenteX.homepage_utente[index_post].post_stesso)
            for j in utenteX.homepage_utente[index_post].lista_commenti_al_Post:
                print(j[0], ': ', j[1])
            print()

        except:
            print('Qualcosa è andato storto. Riprova.')
            print()

#E' una lista che ci permette di caricare utenti nel programma
#Ci permette di lavorare sul programma senza dover inserire a mano ogni volta gli utenti da zero
users = [{'nome_user': 'Vinx', 'nome':'vincenzo', 'cognome':'bruno', 'password':'1234', 'posts':['Cosenza che bella giornata','La suppressata va senza finocchietto!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['pach90','Alerisp94','Ueloiol'], 'lista_commenti':[('pach90','che bello')]},
         {'nome_user': 'Ale94', 'nome':'alessandra', 'cognome':'rispoli', 'password':'1234', 'posts':['Torino che bella giornata','Universo sto arrivando!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['pach90','Vinx989','Ueloiol'], 'lista_commenti':[('Vinx989','che bello')]},
         {'nome_user': 'Pach', 'nome':'nicola', 'cognome':'pacella', 'password':'1234', 'posts':['Firenze che bella giornata','La fiorentina batte il risotto alla milanese!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['Vinx989','Alerisp94','Ueloiol'], 'lista_commenti':[('Vinx989','che bello')]},
         {'nome_user': 'Ste', 'nome':'stefano', 'cognome':'bassi', 'password':'1234', 'posts':['Pavia che bella giornata','Noi fisici siamo degli eroi!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['pach90','Alerisp94','Vinx989'], 'lista_commenti':[('Vinx989','che bello')]}]

# Questo ciclo serve per creare gli utenti già presenti nel social Abstraction
for item in users:
    username = item['nome_user']
    nome = item['nome']
    cognome = item['cognome']
    password = item['password']
    lista_post = item['posts']
    lista_amici = item['amici']
    lista_commenti = item['lista_commenti']
    mario = Utente(username, nome, cognome, password)
    for item in lista_post:
        post_mario = Post(username,item)
        mario.homepage_utente.append(post_mario)


# Metodo utilizzato per l'istanza di Oggetti Utente in Abstraction
# Questo metodo permette di registrare un nuovo utente al social network
def Registrazione():
    print('Inserisci il tuo Username, Nome, Cognome, Password')
    inRegistrazione = True

    while inRegistrazione:
        username = input('Inserisci il tuo Username: ')

        nomeTrovato = False
        for usr in lista_utenti_oggetto:
            if username == usr.username:
                nomeTrovato = True
                break

        if nomeTrovato == False:
            name = input('Inserisci il tuo Nome: ')
            surname = input('Inserisci il tuo Cognome: ')
            password = input('Inserisci il la tua Password: ')

            giacomino = Utente(username, name, surname, password)

            print(f'Grazie per la tua registrazione {username}, ora puoi accedere ad Abstraction!\n')
            inRegistrazione = False

        else:
            print("L'username o password già utilizzati. Vuoi riprovare?\n")
            continua = input('Premi Y per riprovare o qualsiasi tasto tornare indietro .\n')
            if continua.lower() != 'y':
                inRegistrazione = False


# Software Abstraction lato utente
# Questo metodo include tutte le funzionalità a cui l'utente può accedere
# I funzionalità sono state dichiarati nella class User
def Abstraction(NumeroUtente):
    

    inAbstraction = True
    while inAbstraction:
        print(f'Salve {lista_utenti_oggetto[NumeroUtente].username}, scegli cosa vuoi fare: \n')
        
        print('0. Per accedere con un altro account \n')
        
        print('1. Pubblica un Post')
        print('2. Cancella un Post')
        print('3. Commenta un Post\n')
        
        print('4. Aggiungi Amici')
        print('5. Rimuovi Amici \n')

        print('6. Vai al tuo profilo')
        print('7. Lista utenti che segui \n')

        scelta = input('Scelta: ')

        if scelta == '0':
            print('Grazie per esserti connesso. Arrivederci\n')
            inAbstraction = False
        elif scelta == '1':
            lista_utenti_oggetto[NumeroUtente].crea_post()
            # da sistemare in questo swich la scelta dell'utente a cui commentare i post
        elif scelta == '2':
            lista_utenti_oggetto[NumeroUtente].cancella_post()

        elif scelta == '3':
            utente_cercato = input('Digita il nome di un utente: ')

            nomeTrovato = False
            for i in lista_utenti_oggetto:
                if utente_cercato == i.username:
                    nomeTrovato = True
                    utente = i
                    break

            if nomeTrovato == True:
                lista_utenti_oggetto[NumeroUtente].commenta_post(utente)
            else:
                scelta = input('Nome non trovato.')

        elif scelta == '4':
            lista_utenti_oggetto[NumeroUtente].following()

        elif scelta == '5':
            lista_utenti_oggetto[NumeroUtente].un_following()

        elif scelta == '6':
            lista_utenti_oggetto[NumeroUtente].stampa_home()

        elif scelta == '7':
            lista_utenti_oggetto[NumeroUtente].stampa_amici()

        else:
            print('Inserisci una scelta valida')
            pass


# Questo è il main del programma
# Qui si accede all'entry/exit point e si può scegliere se registrarsi
# oppure accedere al proprio profilo se esistente
def AbstractionAccess():
    accesso_registrazione = True

    while accesso_registrazione:
        print('scegli se registrarti, accedere o uscire dal solcial Abstraction')
        print('0. Per Uscire')
        print('1. Per registrarti')
        print('2. Per accedere\n')

        scelta = input('Scelta: ')

        # Per uscire dal Primo Menu
        if scelta == '0':
            print('Arrivederci')
            accesso_registrazione = False

        # Per la registrazione, non si esce dal ciclo totale, si rimane dentro finchè non ti registri con un User assente
        elif scelta == '1':
            Registrazione()

        # accedere, poi dentro altro swithc InAbstract con le cose che si possono fare nel social
        elif scelta == '2':
            user_Ins = input('Inserisci il tuo Username: ')
            pass_Ins = input('Inserisci la tua Password: ')
            check_dat = False
            for idx in range(len(lista_utenti_oggetto)):
                if user_Ins == lista_utenti_oggetto[idx].username and pass_Ins == lista_utenti_oggetto[idx].password:
                    idx_Oggetto = idx
                    check_dat = True

            if check_dat == False:
                print('Username o password errata. Riprova\n')

            else:
                print("Accesso Eseguito!\n")
                Abstraction(idx_Oggetto)

        # else del menu principale, in caso è stata inserita una scelta a caso
        else:
            print('Inserisci scelta valida')


# Parte il programma
AbstractionAccess()
