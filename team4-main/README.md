# team4
Esercitazione python data intelligence experis academy

I componenti del gruppo sono 

- Bassi Stefano (Ueloiol)

- Alessandra Rispoli (Alerisp94)

- Nicola Pacella (Pach90)

- Bruno Vincenzo (Vinx9898) (leader in senso lato)

# Progetto

Il progetto prevede la costruzione di un social network dove e' possinile registrarsi, creare un post, commentare un post e aggiungere followers
Al progetto seguira' un upgrade successivo in cui sara' possibile definire i livelli di amicizia e visualizzare i post in base ai livelli di amicizia

# Struttura del codice:
Il progetto contiene due classi che riguardano servono per la creazione dell'utente e delle funzionalità che esso ha a disposizione.
Un metodo principale, AbstractionAccess, che è il main del progetto. Nello script è presente anche un metodo che gestisce la registazione la social.
Infine troviamo un metodo che funge da menù per l'utente una volta entrato in Abstraction.

### lista_utenti_oggetto - 
Contiene la lista degli utenti, dove per ogni utente vengono consrvate tutte le informazioni primarie, amici e post

### classe Utente - 
Contiene le funzioni principali accedi/registra/crea e cancella post/follow ed unfollow amici. Elementi una volta creati vengono aggiunti
alla lista_utenti_oggetto

### classe Post
E' la classe che viene utilizzare per crear i post degli utenti

### AbstractionAccess 
Questo è il main del programma. Qui si accede all'entry/exit point e si può scegliere se registrarsi, oppure accedere al proprio profilo se esistente.

### Abstraction
Software Abstraction lato utente. Questo metodo include tutte le funzionalità a cui l'utente può accedere. Le funzionalità sono state dichiarati nella class User

### Registrazione
Metodo utilizzato per l'istanza di Oggetti Utente in Abstraction. Questo metodo permette di registrare un nuovo utente al social network

# Road map
Dopo la release Abstraction 1.0 è previsto un upgrade di alcune funzionalità di sotto elencate.
- Sistema di controllo sulla lunghezza e i carattare da inserire nella password
- Sistema di salvataggio ad ogni uscita dal programma
- Inserire allert di assenza amici

La data di release Astraction 1.1 è prevista per il 25/05/2023

### Astraction 2.0
Alla versione 1.1 del programma Astraction seguirà un upgrade che prevede la possibilità di gestire e stabilire la gerarchia delle amicizie( amici stretti, grado di parentela). In questa versione sarà possibile gestire la visione dei post nell'home-page in base alla gerarchia delle amicizie.

La data di release Astraction 2.0 è prevista per il 26/05/2023

### Astraction 2.1

In segutio verranno aggiunte le seguenti funzionalità che faranno riferimento ad una versione 2.1:

- reaction ai post
- ricondivisione dei post
- Indicatore di popolarità. Rendere visibile i like ricevuti, i folowers ed il numero dei post pubblicati
- Impostare un profilo business dove si potrà aggiungere un url per accedere ad eventuali shop digitali

La release della verisone 2.1 è prevista per fine settimana (31/05/2023)

### Astraction 2.2

In segutio verranno aggiunte le seguenti funzionalità che faranno riferimento ad una versione 2.2:

- bloccao di utenti che possono visualizzare il tuo profilo
- Inserimento di immagini nei post
- Possibilità di segnalare post offensivi
- Impostare un profilo pubblico/privato
- Inserire la possibilità di verificare il profilo (bollino blue)

La release della versione 2.2 è prevista per il 06/05/2023

# Commenti:

I commenti sono inseriti per ogni blocco di codice ad inizio blocco

I commenti descrivono in modo sintetico le mansioni svolte dai singoli blocchi

# Diagrammi di flusso

Il codice prevede un diagramma di flusso che descrive il funzionamento del codice

Il file è in formato pdf


# Strutturazione del lavoro

La totalità del proggetto è stato affrontano in gruppo. Per la maggior parte il lavoro è stato svolto in modalità "scrittura collettiva"
dove tutti i menbri del gruppo hanno partecipato. Di seguito è riportata la strutturazione del lavoro:

1- ANALIZZARE PROBLEMA: Cercare di capire in quanti blocchi è suddivisibile il problema. (to do list)

2- NOMENCLATURA: Definire i nomi di variabili, classi, funzioni ecc. cosi da rendere confrontabile il problema.

3- COMPITI: Suddivisione dei compiti a seconda delle autopercepite capacità, gestendo in modo consono i vari blocchi.

4- RICOSTRUZIONE: Ricostruzione del codice.

5- DEBUGGING.

