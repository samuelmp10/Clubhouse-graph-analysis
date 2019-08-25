#!/bin/sh

APITOKEN=$1

cd /usr/src/app


echo "Descarga desde API miembros y tarjetas"

sh api-get.sh $APITOKEN

echo "Descarga desde API finalizada. Procesando datos..."

python obtencion.py $APITOKEN

echo "Datos procesados. Ejecutando detección de comunidades y generación de grafo..."

python nx.py

echo "Clubhouse Graph terminado. Por favor, recargue la página web http://0.0.0.0:5000/clubhouse.html para visualizar el grafo por departamentos predefinidos o visite http://0.0.0.0:5000/clubhouse_comm.html para visualizar el grafo mediante detección automática de comunidades"

cp ./web/graph.json ./
cp -r ./images ./web/
cd ./web

http-server -p 5000


