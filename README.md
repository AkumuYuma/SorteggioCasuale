# SorteggioCasuale
Web Application dotata di REST API per sorteggiare una persona casuale all'interno di una lista

REST API in grado di leggere una lista di persone, aggiungere e rimuovere una singola persona.
Lato server Connexion e Flask sono stati utilizzati per la costruzione dell'API e dell'applicazione.
Il file server.py gestisce la l'applicazione, mentre persone.py gestisce interamente le risposte alle richieste fatte all'API. 

Il file swagger.yml è il file di configurazione per connexion.  
La cartella dati contiene il file json (eventualmente sostituibile con un database in caso di necessità di espansione)
All'Interno della cartella templates si trovano gli html renderizzati
