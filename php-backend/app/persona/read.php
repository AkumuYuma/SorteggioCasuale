<?
declare(strict_types = 1); 
// Setto gli header della risposta
header("Access-Control-Allow-Origin: *"); // Permetto i CORS 
header("Content-type: application/json; charset=UTF-8"); // Dico che restituirò un json 

// Includo database.php e persona.php 
include_once '../config/database.php';
include_once '../models/persona.php'; 

$database = new Database(); 
$conn = $database->getConnection(); 

// Creo un oggetto Persona 
$persona = new Persona($conn); 

$stmt = $persona->read(); 
$numero_persone = $stmt->rowCount(); 

if ($numero_persone > 0) {
    // Creo un array
    $array_persone = array(); // Nota questi sono array associativi 
    $array_persone["elenco"] = array(); // Il json avrà la lista dei records
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        extract($row); // Importa le variabili da $row
        // Praticamente dopo questo statement sono definite le variabili 
        // $idPersona, $nome e $cognome e hanno come valori quelli letti da $row (cioè dal db)

        // Nuova persona da inserire nell'elenco
        $nuova_persona_letta = array(
            "idPersona" => $idPersona, 
            "nome" => $nome, 
            "cognome" => $cognome
        ); // Ho creato un array associativo  
        // la inserisco nell'array di persone 
        array_push($array_persone["elenco"], $nuova_persona_letta); 
    }
    http_response_code(200); // Setta il codice di risposta alla richiesta
    echo json_encode($array_persone); 
} else {
    http_response_code(404); 
    // Se non trovo nessuna persona mando un json con un messaggio
    echo json_encode(
        array("message" => "Nessuna Persona nel database")
    );
}

?>