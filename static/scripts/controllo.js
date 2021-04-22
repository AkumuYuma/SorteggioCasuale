let readURL = "https://sorteggio.herokuapp.com/api/persone"
let listaPersone;
let intervalloAggiornamento = 2000;

function setup() {
  noCanvas();
  listaPersone = select("#listaPersone");
  // Aggiorno in live la lista di persone ogni intervallo di tempo
  setInterval( function() {
    readPeople() // Restituisce una promessa
    .then(nomi => {
      listaPersone.html("Lista: <br>");
      for (let nome of nomi) {
        listaPersone.html(nome + "<br>", true);
      }
    }) // Gestisco eventuali errori
    .catch(error => {
      console.error(error);
    })}, intervalloAggiornamento)

}

async function readPeople() {
  // Richiede all'API di passare i dati relativi a tutte le persone
  // :Return: promessa di jsonificare i dati ottenuti dall'api.
  const response = await fetch(readURL, {
    method: "GET"
  });
  return response.json();
}
