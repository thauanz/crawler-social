#!/bin/sh

while :
do
  for file in /tmp/files/*.csv
  do
    if [ -f "$file" ];then
      echo "$file"
      mongoimport --host mongo-db:27017 -d social -c tweets --type csv --file $file --headerline
      rm $file
    else
      sleep 10
    fi
  done
done