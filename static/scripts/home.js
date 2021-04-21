// Url per il sorteggio casuale
let sorteggioURL = "http://localhost:5000/api/persone/casuale/";
// Url per la lista statica di persone
let readURL = "http://localhost:5000/api/persone/static/read";
//Url per settare la sessione
let setSessionURL = "http://localhost:5000/setsession"
//Url per ottenere la sessione attual
let getSessionURL = "http://localhost:5000/getsession"
// Variabile per la selezione del nome
let selezione;
// Variabile per nome selezionato
let nomeSelezionato;
// Variabile attaccata al tasto pesca
let pesca;
// Variabile attaccata al paragrafo risultato
let risultato;

function preload() {
  // Carico il file statico per la selezione della persona da ignorare e popolo il campo di selezione
  selezione = select("#selezione");
  selezione.style("font-size", "25px");
  selezione.style("text-align", "center");
  selezione.style("width", "200px");
  // Variabile attaccata al paragrafo risultato
  risultato = select("#risultato");
  // Variabile attaccata al tasto pesca
  pesca = select("#pesca");
  pesca.style("width", "260px");
  pesca.style("margin-top", "20px");

  //Se c'è una sessione attiva nascondo il tasto di sorteggio
  fetch(getSessionURL)
  .then(response => {
    if (response.status == 200) {
      pesca.hide();
    }
  });

  // Popolo la selezione
  leggiPersone()
  .then( listaPersone => {
    // Popolo la selezione con la risposta dell'api.
    for (let persona of listaPersone) {
      selezione.option(persona);
    }
    // Setto di default la scelta al primo nome
    selezione.selected(listaPersone[0]);
    nomeSelezionato = listaPersone[0];
  })
  .catch( err => console.log(err) );

}


function setup() {
  // Gestitsco la pressione del tasto per il sorteggio e tengo aggiornato il valore della selezione
  noCanvas();
  // Quando cambio il nome scelto nella selezione aggiorno il nome selezionato
  selezione.changed(() => {
    if (selezione.value()) nomeSelezionato = selezione.value();
  });

  // Gestisco la pressione del tasto per sorteggiare
  pesca.mousePressed(function() {
    // Nascondo il tasto di sorteggio per impedire di sorteggiare una seconda volta
    pesca.hide();
    // Creo la sessione
    fetch(setSessionURL);
    // Passo come argomento il nome selezionato per ignorarlo durante il sorteggio
    sorteggiaPersona({nome: nomeSelezionato})
      .then(sorteggiato => {
        risultato.html("Hai sorteggiato: " + sorteggiato.replace(/"/g, ""));
      })
      .catch(err => risultato.html("Oh no, non ci sono più persone da sorteggiare!"));
  });

}


async function leggiPersone() {
  // Funzione asincrona per leggere il file statico dell'api
  // :return: promessa di ottenere la lista statica delle persone come json
  const response = await fetch(readURL);
  if (response.status == 200) {
    return response.json();
  } else {
    throw(response.status);
  }
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
