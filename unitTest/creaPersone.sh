#!/bin/bash


# Loop per creare 1000 nuove persone tramite l'API, ognuna con nome personai
for i in {1..1000}; do
  stringa='http://localhost:5000/api/persone/persona'
  stringa1=$stringa$i
  # Stringa di richiesta per l'API
  curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' $stringa1
  echo
done
