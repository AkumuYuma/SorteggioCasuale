<?

declare(strict_types=1); // Attivo il controllo sui tipi nel passaggio dei parametri alle funzioni
// Probabilmente serve solo dove chiamo le funzioni e non dove le dichiaro ma non so quindi lo metto anche qui 

class Database {
    // credenziali (istanze private)
    private $host = "db"; // Dove si trova il database 
    private $port = "3306"; // Vedi docker-compose.yml 
    private $db_name = "db_persone"; // Nome del database 
    private $username = "root"; // username del db 
    private $password = "root"; 

    // Connessione (pubblica)
    public $connessione = null; 
    
    public function getConnection(): mixed { // : mixed indica il tipo di ritorno della funzione (type hinting)
        /**
        *   Inizializza e restituisce la connessione al db. 
        *   @return: PDO object (connessione al db)
        */
        try {
            $dsn = "mysql:host=".$this->host.":".$this->port.";dbname=".$this->db_name;
            $this->connessione = new PDO($dsn, $this->username, $this->password); 
            $this->connessione->exec("set names utf8"); 
        } 
        catch(PDOException $exception) {
            echo "Errore di connessione: " . $exception->getMessage();
        }
    return $this->connessione;
    }
}
?>