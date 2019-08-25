#!/bin/bash

APITOKEN=$1

   curl -X GET \
  -H "Content-Type: application/json"  \
  -L "https://api.clubhouse.io/api/beta/members?token=${APITOKEN}"  > members.json
 
   curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/29/stories?token=${APITOKEN}" > deng.json
  
  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/96710/stories?token=${APITOKEN}" > danacommunity.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/96706/stories?token=${APITOKEN}" > danadriver.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/96704/stories?token=${APITOKEN}" > danarider.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/96711/stories?token=${APITOKEN}" > danacolombia.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/96709/stories?token=${APITOKEN}" > danafinance.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/74959/stories?token=${APITOKEN}" > dataanalytics.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/96707/stories?token=${APITOKEN}" > danac4b.json

  curl -X GET \
  -H "Content-Type: application/json" \
  -L "https://api.clubhouse.io/api/beta/projects/4483/stories?token=${APITOKEN}" > datascience.json
  
    curl -X GET \
    -H "Content-Type: application/json" \
    -L "https://api.clubhouse.io/api/beta/projects/96654/stories?token=${APITOKEN}" > danaip.json

