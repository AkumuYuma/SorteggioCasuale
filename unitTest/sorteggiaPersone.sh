#!/bin/bash

for i in {1..1000}; do
  curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"nome":"persona"}' 'http://localhost:5000/api/persone/casuale/'
done
