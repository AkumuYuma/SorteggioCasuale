from flask import render_template
from flask_cors import CORS
import connexion
# Creo l'istanza dell'applicazione
# La specification_dir indica dove trovare il file swagger
app = connexion.App(__name__, specification_dir='./')

CORS(app.app)
# Leggo il file swagger per configurare l'endpoint dell'api
app.add_api("swagger.yml")

# Base per "/" dell'applicazione
@app.route("/")
def home():
    """

    Questa funzione gestisce la risposta alle richieste su url:5000/
    Restituisce il rendering del template 'home.html'

    """
    return render_template("home.html")

# Pagina di controllo live dei nomi
@app.route("/controllo")
def controllo():
    """

    Questa funzione renderizza la pagina di controllo delle persone

    """

    return render_template("controllo.html")


if __name__ == "__main__":
    # Per esporlo alla rete modificare host = "0.0.0.0"
    app.run(host = '0.0.0.0', port= 443, debug = False)
