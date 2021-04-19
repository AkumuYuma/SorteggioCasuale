let sorteggioURL = "http://localhost:5000/api/persone/casuale/"
let lista;
let pesca;

function preload() {
  // Carico direttamente il file statico per la selezione della persona da ignorare
  // Nota che il sorteggio non altera il file statico, quindi questa lista non sarà mai modificata
}

function setup() {
  noCanvas();
  console.log(lista);

  // Gestisco la pressione del tasto per sorteggiare
  pesca = select("#pesca");
  pesca.mousePressed(function() {
    sorteggiaPersona()
    .then( sorteggiato => console.log(sorteggiato))
    .catch( err => console.error(err));
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
  return response.text();
}
