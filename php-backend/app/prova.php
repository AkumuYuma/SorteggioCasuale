<?
echo "Prova connessione al db \n"; 
try {
    $conn = new PDO("mysql:host=db:3306;dbname=db_persone", "root", "root"); 
    echo $conn; 
} catch(PDOException $exception) {
    echo "Errore di connessione: " . $exception->getMessage();
}
?>