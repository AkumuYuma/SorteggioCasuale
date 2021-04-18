#!/bin/bash

for i in {1..1000}; do
  stringa='http://localhost:5000/api/persone/persona'
  stringa1=$stringa$i
  curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' $stringa1 
  echo 
done
