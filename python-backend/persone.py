from flask import make_response, abort, jsonify
import json
import random

# Carico la lista di persone dal file
PERSONE = json.load(open("dati/persone.json"))


#------------------------------------------------------------------------------#
# Operazioni live. Le operazioni seguenti sono offettuate solamente sulla variabile live.
# Resettato il server, tutte le modifiche live verranno dimenticate.


# Handler per una richiesta di tipo GET all'api
def read():
    """

    Questa funzione risponde alla chiamata per /api/persone restituendo la lista ordinata dei nomi
    :return: Lista ordinata delle persone

    """
    global PERSONE
    return sorted(PERSONE["nomi"])

# Handler per la richiesta di estrazione
def estrai(nome):
    """
    Questa funzione estrae casualmente una persona dalla lista. Se viene passato il parametro nome, esso viene ignorato durante l'estrazione
    La persona estratta viene eliminata dalla lista.
    Nota: Questa operazione non sovrascrive il file statico, cambia solo il database dinamico.
    Bisogna passare un dizionario del tipo:
    {
        "nome": "...."
    }

    :param nome: Dizionario. Persona da ignorare nel sorteggio in nome["nome"]
    :return: Persona estratta

    """
    global PERSONE
    # Se la lista è vuota esco subito
    if not PERSONE["nomi"]:
        abort(
            406,
            description = "La lista è vuota"
        )

    # Gestione nel caso in cui venga passato il parametro
    if nome:
        # Se la sintassi è sbagliata
        if not "nome" in nome:
            abort(
                400,
                description = """Sintassi sbagliata nella richiesta la richiesta deve essere del tipo:{"nome": "...."}"""
            )
        # Se la lista contiene solo il nome da ignorare
        if PERSONE["nomi"] == [nome["nome"]]:
            abort(
                406,
                description = "La lista contiene solo te stesso"
            )
        # Se la persona da ignorare è nella lista
        elif nome["nome"] in PERSONE["nomi"]:
            # Lo rimuovo per non sorteggiarlo
            PERSONE["nomi"].remove(nome["nome"])
            # Estraggo un elemento casuale
            estratto = PERSONE["nomi"].pop(random.randint(0, len(PERSONE["nomi"]) - 1))
            # Lo riaggiungo alla lista 
            PERSONE["nomi"].append(nome["nome"])
            return estratto
    
    # Se non viene passato il nome estraggo tra tutti
    estratto = PERSONE["nomi"].pop(random.randint(0, len(PERSONE["nomi"]) - 1))

    return estratto


#------------------------------------------------------------------------------#
# Operazioni statiche. Le operazioni statiche hanno effetto ANCHE sul file statico contenente i dati.
# Le modifiche effettuate con queste richieste saranno permanenti e ricordate anche dopo il riavvio del server


def read_static():
    """
    Questa funzione legge e restituisce la lista statica di persone, ricarica il file json statico
    e lo passa come risposta.

    :return: Lista ordinata delle persone.
    """
    risposta = json.load(open("dati/persone.json"))
    return sorted(risposta["nomi"])


# Creazione di una nuova persona
def create(nome):
    """

    Questa funzione crea una nuova persona nella struttura PERSONE in base al nome passato

    :param nome: nome persona da creare
    :return: 201 successo, 406 persona esistente

    """
    global PERSONE
    # Se la persona non è nella lista, la aggiungo
    if nome not in PERSONE["nomi"] and nome is not None:
        # Aggiungo la persona alla lista
        PERSONE["nomi"].append(nome)
        # Prima di fare la risposta aggiorno il file permanente
        with open("dati/persone.json", "w") as out:
            json.dump(PERSONE, out)

        # Faccio la risposta
        return make_response(str(nome) + " creato con successo", 201)

    else:
        abort(
            406,
            description = str(nome) + " già esistente"
        )

# Eliminazione di una persona
def delete(nome):
    """

    Questa funzione cancella la persona nome dalla struttura persone se la persona esiste

    :param nome: nome persona da cancellare
    :return: 200 se eliminata con successo, 404 se persona non trovata

    """
    global PERSONE
    # Se la persona è nella lista la rimuovo
    if nome in PERSONE["nomi"]:
        # Rimuovo la persona dalla variabile
        PERSONE["nomi"].remove(nome)
        # Aggiorno il file json permanente dopo la modifica
        with open("dati/persone.json", "w") as out:
            json.dump(PERSONE, out)
        # Faccio la risposta alla richiesta
        return make_response(str(nome) + " eliminato con successo", 200)

    else:
        abort(
            404,
            description = str(nome) + " non trovato"
        )
