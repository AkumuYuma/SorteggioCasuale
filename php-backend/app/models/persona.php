<?
declare(strict_types=1); 
class Persona {
    private $connessione; // al database 
    private $nome_table = "Persone"; // Nome della table nel db 

    public $nome; 
    public $cognome; 

    // Costruttore 
    public function __construct(mixed $db) {
        /** 
        * Inizializza la connessione al db
        * @param: mixed db: connessione al db  
        */
        $this->connessione = $db;  
    }

    function read(): PDOStatement  { // i metodi senza specificatore sono pubblici (giusto per provare )
        /**
         * Legge tutti gli elementi della tabella 
         * @return: PDOStatement. Lo statement con la query "SELECT * FROM nome_table"
        */
        $query = "SELECT * FROM " . $this->nome_table;  
        $stmt = $this->connessione->prepare($query); 
        $stmt->execute(); 
        return $stmt;
    }

    public function create(): bool {
        /**
         * Crea una nuova persona usando $this->nome e $this->cognome
         * @return: bool. True se la query è stata eseguita. False altrimenti. 
         */
        // Query per inserimento nel db
        if (!empty($this->cognome)) {
            $query = " 
            INSERT INTO " . $this->nome_table . "(nome, cognome) 
            VALUES ('" . $this->nome . "', '" . $this->cognome . "');"; 
        } else {
            $query = "
            INSERT INTO " . $this->nome_table . " (nome) 
            VALUES ('" . $this->nome . "');"; 
        }
        // Preparo la query 
        $stmt = $this->connessione->prepare($query); 
        // La eseguo
        // Il metodo execute() restituisce true in caso di successo e false altrimenti. 
        if ($stmt->execute()) {
            return true; 
        }
        return false; 
    }

    public function update(int $idPersona): bool {
        /**
         * Modifica nome e cognome della persona $idPersona usando $this->nome e $this->cognome
         * @param: int. Id della persona da modificare nel database 
         * @return: bool. True se la query è eseguita con successo, false altrimenti. 
         */

         $query = "
         UPDATE " . $this->nome_table . "SET nome = " . $this->nome . " cognome = " . $this->cognome . " WHERE idPersona = " . $idPersona . ";"; 
         $stmt = $this->connessione->prepare($query); 
         if ($stmt->execute()) {
             return true; 
         }
         return false; 
    }

    public function delete(int $idPersona): bool {
        /**
         * Elimina una persona $idPersona dal database
         * @param: int. Id della persona da eliminare
         * @return: bool. True se la query è eseguita con successo, false altrimenti. 
         */
        $query = "
        DELETE FROM " . $this->nome_table . " WHERE idPersona = " . $idPersona; 
        $stmt = $this->connessione->prepare($query); 
        if ($stmt->execute()) {
            return true; 
        }
        return false; 
    }

    

}

?>