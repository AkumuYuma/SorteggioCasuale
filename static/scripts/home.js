let readURL = "http://localhost:5000/api/persone"

function setup() {
  noCanvas();
  //---------------------------------------------------------------------------------------------------//
  // [DEBUG] Aggiorno ogni mezzo secondo la lista delle persone per controllare che tutto funzioni bene
  // La sintassi è: setInterval(funzione anonima, 500)
  // La funzione anonima è quella che legge le persone in maniera asincrona e le inserisce nel paragrafo html
  let listaPersone = select("#listaPersone");
  setInterval(function() {
    readPeople() // Restituisce una promessa
      .then(nomi => {
        listaPersone.html("Lista: <br>");
        for (let nome of nomi) {
          listaPersone.html(nome + "<br>", true);
        }
      }) // Gestisco eventuali errori
      .catch(error => {
        console.error(error);
      }) // Setto l'intervallo di aggiornamento dei nomi
  }, 500);
  //---------------------------------------------------------------------------------------------------//

}


async function readPeople() {
  // Richiede all'API di passare i dati relativi a tutte le persone
  // :Return: promessa di jsonificare i dati ottenuti dall'api.
  const response = await fetch(readURL, {
    method: "GET"
  });
  return response.json();
}
