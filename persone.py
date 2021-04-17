from flask import make_response, abort
import json

# Carico la lista di persone dal file
PERSONE = json.load(open("dati/persone.json"))

# Handler per una richiesta di tipo GET all'api
def read():
    """

    Questa funzione risponde alla chiamata per /api/persone restituendo la lista ordinata dei nomi
    :return: Lista ordinata delle persone

    """

    return sorted(PERSONE["nomi"])


def create(nome):
    """

    Questa funzione crea una nuova persona nella struttura PERSONE in base al nome passato

    :param nome: nome persona da creare
    :return: 201 successo, 406 persona esistente

    """

    # Se la persona non è nella lista, la aggiungo
    if nome not in PERSONE and nome is not None:
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

def delete(nome):
    """

    Questa funzione cancella la persona nome dalla struttura persone se la persona esiste

    :param nome: nome persona da cancellare
    :return: 200 se eliminata con successo, 404 se persona non trovata

    """

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
