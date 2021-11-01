<?
header("Access-Control-Allow-Origin: *"); // Per i cors 
header("Content-Type: application/json; charset=UTF-8"); 
header("Access-Control-Allow-Methods: POST"); // Devo fare una richiesta POST per creare un nuova persona
// Questo permette di usare alcuni header
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

include_once "../config/database.php"; 
include_once "../models/persona.php"; 

$database = new Database(); 
$conn = $database->getConnection(); 
$personaDaAggiungere = new Persona($conn); 

// file_get_contents() permette di leggere il contenuto di un file. 
// Il primo argomento è il nome del file. Passando "php://input" leggi i raw data ottenuti dalla richiesta POST.
// json_decode trasforma un json in un array
$data = json_decode(file_get_contents("php://input", true));
// Ho bisogno che almeno il nome non sia vuoto 
if (!empty($data->nome)) {
    $personaDaAggiungere->nome = $data->nome; 
    if ($personaDaAggiungere->create()) {
        http_response_code(201); // Ho creato la persona con successo
        echo json_encode(array(
            "message" => "Persona creata correttamente" 
        ));
    } else {
        http_response_code(503); // Servizio non disponibile
        echo json_encode(array(
            "message" => "Impossibile creare persona"
        )); 
    }
}  else {
    http_response_code(400); // bad request
    echo json_encode(array(
        "message" => "I dati inviati non sono corretti"
    ));
}

?>