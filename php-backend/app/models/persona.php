<?
declare(strict_types=1); 
class Persona {
    private $connessione; // al database 
    private $nome_table = "Persone"; // Nome della table nel db 

    public $nome; 
    public $cognome; 

    // Costruttore 
    public function __construct(mixed $db) {
        /*
        Inizializza la connessione al db
        @param: mixed db: connessione al db  
        */
        $this->connessione = $db;  
    }

    function read() { // i metodi senza specificatore sono pubblici (giusto per provare )
        /*
        Legge tutti gli elementi della tabella 
        @return: PDOStatement. Lo statement con la query "SELECT * FROM nome_table"
        */
        $query = "SELECT * FROM " . $this->nome_table;  
        $stmt = $this->connessione->prepare($query); 
        $stmt->execute(); 
        return $stmt;
    }

    

}

?>