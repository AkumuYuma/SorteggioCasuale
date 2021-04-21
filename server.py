from flask import *
import connexion

# Creo l'istanza dell'applicazione
# La specification_dir indica dove trovare il file swagger
app = connexion.FlaskApp(__name__, specification_dir='./')
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

session = set()
# Pagina di set della sessione utente
@app.route("/setsession")
def setSession():
    """

    Legge l'indirizzo ip del client e inizializza una sessione per quell'utente
    :return: 200 se la sessione è stata settata con successo

    """
    global session
    ip = request.remote_addr
    session.add(ip)
    return make_response("Sessione creata con successo", 200)

@app.route("/getsession")
def getSession():
    """

    Confronta l'indirizzo ip del richiedente con quelli presenti nella sessione.
    :return: 404 se la sessione non esiste, 200 se la sessione esiste

    """
    global session
    ip = request.remote_addr
    if session and ip in session:
        return make_response("Sei nella sessione, IP: " + str(ip), 200)
    else:
        return make_response("Non sei nella sessione", 404);

@app.route("/delsession")
def delSession():
    """

    Se l'indirizzo ip del richiedente si trova nella sessione, lo elimina. Altrimenti non fa niente
    :return: 200 se ho eliminato con successo, 404 se l'utente non è nella sessione

    """
    global session
    ip = request.remote_addr
    if session and ip in session:
        session.remove(ip)
        return make_response("Sessione eliminata con successo", 200)
    else:
        return make_response("Non sei nella sessione", 404)


if __name__ == "__main__":
    # Per esporlo alla rete modificare host = "0.0.0.0"
    app.run(host = '0.0.0.0', port = 5000, debug = False)
