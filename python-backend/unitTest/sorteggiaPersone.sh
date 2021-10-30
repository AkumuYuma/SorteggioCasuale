#!/bin/bash

#Loop per sorteggiare 1000 persone casuali 
for i in {1..1000}; do
  curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{}' 'http://localhost:5000/api/persone/casuale/'
done
