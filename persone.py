from flask import make_response, abort

PERSONE = {
    "Ciccio",
    "Mimmo",
    "Franco",
    "Emanuele Fiorente",
    "Emanuele Antonicelli"
}

# Handler per una richiesta di tipo GET all'api
def read():
    """

    Questa funzione risponde alla chiamata per /api/persone restituendo la lista delle persone
    :return: Lista ordinata delle persone

    """

    return list(sorted(PERSONE))


def create(nome):
    """

    Questa funzione crea una nuova persona nella struttura PERSONE in base al nome passato

    :param nome: nome persona da creare
    :return: 201 successo, 406 persona esistente

    """

    # Se la persona non è nella lista, la aggiungo
    if nome not in PERSONE and nome is not None:
        PERSONE.add(nome)
        return make_response(str(nome) + " creato con successo", 201)

    # Altrimenti do errore
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

    if nome in PERSONE:
        PERSONE.discard(nome)
        return make_response(str(nome) + " eliminato con successo", 200)
    else:
        abort(
            404,
            description = str(nome) + " non trovato"
        )
