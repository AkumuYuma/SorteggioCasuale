Sto seguendo questa [guida](https://html.it/pag/69110/creare-il-database-2/). L'idea è fare un buon backend in php e un frontend decente usando tailwind css.

Servizio composto da 3 docker:
1. nginx -> Apre un web server configurato con php fastcgi sulla porta 80 della macchina locale. (porta 80 anche nel docker)
2. php-fpm -> Il server php per il backend.
3. mysql -> Per il database, apre la porta 3000 nel docker

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

# Commento al [docker-compose.yml](docker-compose.yml) file
## Database:
importante il mounting della cartella [db_init](db_init) in /docker-entrypoint-initdb.d.
Il docker di mysql esegue qualsiasi script `.sh, .sql, .sql.gz` presente in quella cartella.
Quindi monto la cartella db_init su docker-entrypoint-initdb.d.

Nella cartella db_init è presente lo script [setup.sql](setup.sql), che crea la tabella di persone.
In questo modo all'avvio dell'applicazione viene creata una tabella, alla quale il backend potrà connettersi per effettuale le modifiche
tramite la rest api.

## Nginx:
Non so bene (Devi capire come funziona il file conf.d)
## php:
Non so bene

# Review del funzionamento dell'applicazione
Quando i servizi sono up and running con docker-compose, viene servito tutto il contenuto della cartella ./html_files/ a partire da index.html
Attualmente ci sono solo due pagine di prova per verificare che funzioni tutto.

# Ora bisogna scrivere il codice :)
