Sto seguendo questa [guida](https://html.it/pag/69110/creare-il-database-2/). L'idea è fare un buon backend in php e un frontend decente usando tailwind css.

Servizio composto da 2 docker:
1. php-apache -> Server apache con php. Serve il contenuto della cartella app.
2. mysql -> Per il database, apre la porta 3306 nel docker

Tramite docker compose i 3 container possono comunicare e gli script php possono connettersi al db.

# Per startare il servizio:
All'interno della cartella ./docker_compose eseguire `# restart_services.sh`.
Oppure `# docker-compose up -d`.
## MEMO:
Per entrare nel docker del db e modificare dall'interno:
1. `# docker exec -it sorteggio_db bash`
2. da dentro il docker `# mysql -u root -p` -> E poi metti la password (Quella scelta nel docker-compose.yml file).
Questo comando ti fa entrare come utente root nel db. Puoi anche fare `# mysql -u root -p db_persone` per attaccarti direttamente al database
(e non dover fare `> use db_persone;` dentro mysql).

# Commento al [docker-compose.yml](./docker_compose/docker-compose.yml) file
## Database:
### db_init e inizializzazione database
importante il mounting della cartella [db_init](./docker_compose/db_init) in /docker-entrypoint-initdb.d.
Il docker di mysql esegue qualsiasi script `.sh, .sql, .sql.gz` presente in quella cartella.
Quindi monto la cartella db_init su docker-entrypoint-initdb.d.

Nella cartella db_init è presente lo script [setup.sql](./docker_compose/db_init/setup.sql), che crea la tabella di persone.
In questo modo all'avvio dell'applicazione viene creata una tabella, alla quale il backend potrà connettersi per effettuale le modifiche
tramite la rest api.
**Nota:** La sintassi per mettere primary key e auto increment a mysql è leggermente diversa da, ad esempio, sqlite3. Vai a vedere sempre la documentazione sul sito.

### Dati persistenti
Tramite il docker-compose file viene anche creato un volume per fare in modo che i dati vengano salvati anche se si esegue `# docker-compose down`.
In pratica creo un volume di nome "datavolume" e di default viene creata nella cartella /var/lib/docker/volumes. Il volume persiste fino a quando non si esegue
`# docker-compose down -v`, che forza la rimozione e distruzione dei volumi associati.
**Nota:** Ricorda di eliminare il volume una volta finito il developement.

## app:
Per prima cosa buildo l'immagine con il [Dockerfile](./docker-compose/Dockerfile) presente nella cartella.
Il Dockerfile semplicemente prende l'immagine di php-apache e installa le librerie necessarie per l'uso del database.
Il file compose semplicemente builda l'immagine e monta il contenuto della cartella [app](./app) nella cartella /var/www/html/ del docker (cartella di default che viene servita da apache).
Pacchetti php necessari:
- mysqli
- pdo
- pdo_mysql

**Nota:** Lo script docker-php-ext-install è messo a disposizione dall'immagine php-apache appositamente per semplificare l'istallazione di pacchetti php nel docker.
Se necessario usare delle particolari configurazioni di apache bisogna copiare il propfio file di configurazione (.conf) nella cartella /etc/apache2 del docker.

# Review del funzionamento dell'applicazione
Quando i servizi sono up and running con docker-compose, viene servito tutto il contenuto della cartella ./app a partire da index.html

L'idea è fare una pagina di sorteggio e una semplice interfaccia di login.
L'utente loggato può gestire i nomi da sorteggiare, aggiungere e rimuovere persone dal database, tutto tramite interfaccia web. L'utente non loggato può solamente sorteggiare un nome.

Attualmente ci sono solo due pagine di prova per verificare che funzioni tutto.

## Backend 
### classe Database
Nella cartella [config](./app/config) è presente il file [database.php](./app/config/database.php) che fa da interfaccia a mysql. La classe Database ha un solo metodo: **getConnection()**, che si connette al db e restituisce l'oggetto connessione. 
Gli oggetti di tipo Database sono utilizzati solamente dalla classe Persona, che riceve come parametro del costruttore l'oggetto connessione. 
### Modelli 
Nella cartella [models](./app/models) sono presenti i modelli. Teoricamente andrebbe costruita una classe (e quindi ripetuto il processo) per ogni tipo di oggetto che si vuole salvare nel db.
Ogni modello prende come argomento del costruttore la connessione al db (eventualmente si potrebbe passare anche il nome della tabella nel db) e deve avere almeno 4 metodi pubblici per le operazioni CRUD (create, read, update, delete), questi metodi saranno chiamati negli script con lo stesso nome nella cartella denominata con il nome del modello. 
Esempio: nella cartella [persona](./app/persona) c'è il file [read.php](./app/persona/read.php) nel quale viene chiamato il metodo **read()** della classe Persona. 

### Operazioni CRUD
Nella cartella con il nome relativo al modello ci sono i file che implementano le operazioni CRUD vere e proprie. 
Richiesta GET a http://hostname/persona/read.php -> Restituisce il json con tutte le persone; 
Richiesta POST a http://hostname/persona/create.php -> Crea una nuova persona con i dati passati nella richiesta;
e così via.

L'insieme di queste operazioni determina la REST API e permette la gestione di persone nel database usando solamente le richieste. 

**Nota**: Probabilmente sarà necessario implementare all'interno dell'api stessa la funzionalità di sorteggio in quanto implementandola nel front end potrei avere problemi di contemporaneità (stessa persona sorteggiata diverse volte). Dovrò implementare una cosa tipo http://hostmame/persona/estrai.php che estrae una persona casuale dal database. 