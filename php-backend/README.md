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
importante il mounting della cartella [db_init](./docker_compose/db_init) in /docker-entrypoint-initdb.d.
Il docker di mysql esegue qualsiasi script `.sh, .sql, .sql.gz` presente in quella cartella.
Quindi monto la cartella db_init su docker-entrypoint-initdb.d.

Nella cartella db_init è presente lo script [setup.sql](./docker_compose/db_init/setup.sql), che crea la tabella di persone.
In questo modo all'avvio dell'applicazione viene creata una tabella, alla quale il backend potrà connettersi per effettuale le modifiche
tramite la rest api.

## app:
Per prima cosa buildo l'immagine con il [Dockerfile](./docker-compose/Dockerfile) presente nella cartella.
Il Dockerfile semplicemente prende l'immagine di php-apache e installa le librerie necessarie per l'uso del database.
Il file compose semplicemente builda l'immagine e monta il contenuto della cartella [app](./app) nella cartella /var/www/html/ del docker (cartella di default che viene servita da apache). 
Pacchetti php necessari: 
- mysqli 
- pdo 
- pdo_mysql 

Nota: Lo script docker-php-ext-install è messo a disposizione dall'immagine php-apache appositamente per semplificare l'istallazione di pacchetti php nel docker. 
Se necessario usare delle particolari configurazioni di apache bisogna copiare il propfio file di configurazione (.conf) nella cartella /etc/apache2 del docker. 

# Review del funzionamento dell'applicazione
Quando i servizi sono up and running con docker-compose, viene servito tutto il contenuto della cartella ./app a partire da index.html

L'idea è fare una pagina di sorteggio e una semplice interfaccia di login. 
L'utente loggato può gestire i nomi da sorteggiare, aggiungere e rimuovere persone dal database, tutto tramite interfaccia web. L'utente non loggato può solamente sorteggiare un nome.  

Attualmente ci sono solo due pagine di prova per verificare che funzioni tutto.
# Ora bisogna scrivere il codice :)
