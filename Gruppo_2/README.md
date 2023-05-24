# PySpark_gruppo2

Membri:
- Manuel Ehrlich  (https://github.com/maeh98),
- Manuela Montesano (https://github.com/Manuela2798),
- Leonardo Pagani (https://github.com/pagus93)

Formattazione:
- commenti: 1 commento all'inizio di ogni blocco e solo se necessario si commenta la riga
- scrittura: manuel condivide e insieme discutiamo su cosa scrivere
- separatore nome variabili: underscore

Istruzioni:
Un'azienda ha bisogno di un app per gestione le proprie risorse umane \\
Release 1.0: 
Bisogna integrare un sistema di registrazione dipendenti con funzionalità CRUD (aggiungere dipendenti, eliminarli, modificare le loro informazioni) e che generi automaticamente un report quando richiesto. \\
Release 2.0:
Bisogna implementare una funzionalità di calcolo delle retribuzioni e della gestione ferie.

# Struttura interfaccia
Il programma si compone di 3 menù: 
-il primo, il principale di login
-gli altri due riferiti a quele utente ci accede: Gestore o Dipendente,a seconda di dove si accede le funzionalità cambiano

Menu dipendenti (1):
Chiedi nome, cognome, password
Visualizza ferie
visualizza retribuzione
esci

Menu gestore (2):
Chiedi password
Aggiungi dipendente
Modifica dipendente
Rimuovi dipendente
Genera report
esci

# Struttura codice
L'implementazione usa una classe padre (Persona) e due classi figlio (Dipendente e Gestore).
La classe Persona contiene semplicemente le informazioni anagrafiche.
La classe Dipendente contiene le informzioni di interesse dell'azienda.
I metodi modificano le caratteristiche degli oggetti di tipo dipendente.
La classe Gestore contiene le informazioni sul capo.
I metodi vanno a modificare la lista dei dipendenti (sotto forma di istanze).

Per accedere ai due diversi menu, bisogna effettuare un login.
Per i dipendenti ciò avviene tramite la funzione login(), che a sua volta 
richiama le funzioni controllo_esistenza_dipendente() per verificare l'esistenza 
dipendente nella lista, e controllo_password_dipendente() per il controllo password.
Per i gestori avviene con un semplice controllo.


# ROADMAP: potenziali funzionalità future
- Avere piu gestori




