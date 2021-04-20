// Url per il sorteggio casuale
let sorteggioURL = "http://localhost:5000/api/persone/casuale/";
// Url per la lista statica di persone
let readURL = "http://localhost:5000/api/persone/static/read";
let listaPersone;
let pesca;


function preload() {
  // Carico il file statico per la selezione della persona da ignorare
  // Nota che il sorteggio non altera il file statico, quindi questa lista non sarà mai modificata
  listaPersone = loadJSON(readURL);
}

function setup() {
  noCanvas();
  console.log(listaPersone);

  let risultato = select("#risultato");

  // Gestisco la pressione del tasto per sorteggiare
  pesca = select("#pesca");
  pesca.mousePressed(function() {
    sorteggiaPersona()
      .then(sorteggiato => {
        risultato.html("Hai sorteggiato: " + sorteggiato.replace(/"/g, ""));
      })
      .catch(err => risultato.html("Oh no, non ci sono più persone da sorteggiare!"));
  });

}


async function sorteggiaPersona(body = {}) {
  // Richiede all'API di sorteggiare una persona a caso. Il parametro indica il nome da ignorare
  // :param body: corpo della richiesta, se vuoto passa come body della richiesta un oggetto vuoto
  // :reutrn: promessa di ottenere il nome sorteggiato come stringa.
  const response = await fetch(sorteggioURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(body)
  });

  if (response.status == 200) {
    // Se l'API da una risposta positiva mando il corpo della risposta 
    return response.text();
  } else {
    // Se non ci sono più persone mando un errore
    throw (response.status);
  }

}
