from flask import Flask, render_template

import connexion

# Creo l'istanza dell'applicazione
# La specification_dir indica dove trovare il file swagger
app = connexion.App(__name__, specification_dir='./')

# Leggo il file swagger per configurare l'endpoint dell'api
app.add_api("swagger.yml")

# Base per "/" dell'applicazione
@app.route("/")
def home():
    """

    Questa funzione gestisce la risposta alle richieste su url:5000/
    Restituisce il rendering del template 'home.html'

    """
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = False) 