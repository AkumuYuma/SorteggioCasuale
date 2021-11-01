<?php
header("Access-Control-Allow-Origin: *"); // Per i cors 
header("Content-Type: application/json; charset=UTF-8"); 
header("Access-Control-Allow-Methods: POST"); // Devo fare una richiesta POST per creare un nuova persona
// Questo permette di usare alcuni header
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");
?>