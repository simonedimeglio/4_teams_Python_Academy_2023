# teamWork_experis2023
![team-3](https://github.com/simonedimeglio/4_teams_Python_Academy_2023/assets/78272736/e62315dc-1c7c-4b43-9183-cfbacae543ea)
**Project 3: TO-DO LIST**

   Description: Simulation of a task management system.    
      <br>
MEMBRI DEL TEAM 3: <br>
 -Franco Rinaldi - https://github.com/jalt1990 <br>
 -Carlo Schiano Di Cola - https://github.com/tbnh62 <br>
 -Monica Parmigiani - https://github.com/monicaparmigiani <br>
 -Giorgio Cappello - https://github.com/GiorgioCappello <br>

**TEAMWORKING RIFERITO AD ANALISI E SVILUPPO
DI APP GESTIONE TASK CON SERVIZI CRUD**


REGOLE DI GRUPPO

1. COORDINAMENTO INTERNO:
  - requisiti individuale preliminare e brainstorming collettivo;
  - pianificazione del tempo durante il brainstorming;
  - pianificazione delle task urgenti;
  - comunicazioni agili eliminando barriere gerarchiche con il massimo rispetto reciproco;
  - gestione dello sprint in base alle tempistiche con assegnazione task.

2. COMMIT ON GITHUB:
  - pull a inizio lavoro, con file separati;
  - push dei file personali sulla cartella condivisa ogni aggiornamento importante;
  - il teamleader, o chi per sua vece, ha l'onere di unire i file compositi;
  - le cancellazioni solo ed esclusivamente se decise in gruppo.

3. DOVE E QUANDO INSERIRE I COMMENTI:
  - uno per definire classe o funzione al di sopra delle stesse;
  - laterale se corti;
  - accanto agli script in caso di necessità per spiegare l'algoritmo;
  - a più righe se il blocco è particolarmente complesso da leggere.

4. CLEAN CODE:
  - nomi delle variabili con underscore;
  - nomi delle Classi e delle funzioni in camelCase;
  - nomi che abbiano un significato coerente;
  - raggruppamento del codice in base al tipo (classi, funzioni, test, etc...).
  
5. FEATURES DA IMPLEMENTARE:
  - possibilità di implementare più liste, ognuna con nome di riferimento o di categoria,
    con relativa data di scadenza e le diverse task all'interno;
  - inserimento di un alert per i giorni mancanti alla scadenza;
  - inserimento di un filtro controllo per le task e le liste attive, mostrando anche una deadline;
  - inserimento di un filtro task scaduta/non scaduta;
  - inserimento di un sistema di comunicazione con app calendario esterne;
  - implentazione di funzione di import/export per file di backup;
  - ordinamento delle liste per priorità, scadenza, o da completare;
  - visualizzazione del progressivo dell'esecuzione delle liste (in percentuale);
  - gestione di più profili (nome utente e password).




____________________________________________________________
MANUALE DI ISTRUZIONI - REALEASE 2.0
____________________________________________________________
L'app si avvia dal menu di accesso (1)


____________________________________________________________
1. MENU DI ACCESSO
____________________________________________________________
Nel menu di Accesso appare il seguente messaggio di Benvenuto che invita a entrare nell'App
o a uscire da essa:

Benvenuto nell' App della To Do List
1. Entra
0. Esci


____________________________________________________________
1.1 --> Entra
____________________________________________________________
Una volta entrati nell' app appare il menu Principale con le seguenti funzioni:

Benvenuto nell' App della To Do List.
1. Aggiungi una task
2. Visualizza tutte le task
3. Elimina Task
4. Modifica la Task
5. Aggiorna Status della Task        
0. Torna indietro


____________________________________________________________
1.1.1 --> Aggiungi una task
____________________________________________________________
Permette di creare una task specificandone il contenuto, la data di scadenza,
e la priorità (facoltativa).
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.2 --> Visualizza tutte le task
____________________________________________________________
Permette di visualizzare le singole task finora memorizzate all'interno della
Lista Task dell' App. Se la lista è vuota, visualizza un messaggio che dichiara
l'assenza di task.
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.3 --> Elimina Task
____________________________________________________________
Se la lista delle task ha almeno un elemento, permette di eliminare una task
dalla Lista delle task selezionandola tramite l'indice di riferimento.
Se la lista è vuota, riporta un messaggio di avviso.
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.4 --> Modifica la Task
____________________________________________________________
Se la lista delle task ha almeno un elemento, permette di modificare una task
dalla Lista delle task selezionandola tramite l'indice di riferimento.

Una volta selezionata la task da modificare, appare il seguente menu di modifica:

Questa è l'area di modifica:
1. Modifica completa di una task
2. Modifica solo un elemento di una task
0. Torna indietro


____________________________________________________________
1.1.4.1 --> Modifica completa di una task
____________________________________________________________
Arriveranno dei messaggi di inserimento input all'utente per indicare il contenuto della task,
i dati della scadenza, e la priorità aggiornata, per modificare completamente il task
precedentemente selezionato.
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.4.2 --> Modifica solo un elemento di una task
____________________________________________________________
Apparirà all' utente il seguente menu di navigazione:

Questa è l'area di modifica parziale:
1. Modifica contenuto
2. Modifica scadenza
3. Modifica priorita
0. Torna indietro

L'utente potrà selezionare cosa modificare della task precedentemente indicata.
In base alla selezione, avverrà la modifica e il task verrà visualizzato aggiornato.
Alla fine di qualsiasi modifica fatta si torna in loop a questo menu (1.1.4.2)
finchè l'utente non seleziona 0 che riporta al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.4.0 --> Torna indietro
____________________________________________________________
riporta al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.5 --> Aggiorna Status della Task
____________________________________________________________
Se la lista delle task ha almeno un elemento, permette di aggiornare lo status
di una task dalla Lista delle task selezionandola tramite l'indice di riferimento.
Eseguita l'operazione, viene visualizzata la task aggiornata con lo status,
e si torna poi al Menu di Benvenuto (1.1 Entra)
