#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import json
import re, string,io,csv
import operator
import requests
import shutil

api_token = sys.argv[1]


def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]


def imagedownload(url,id): 

    r = requests.get(url, stream=True,headers={'User-agent': 'Mozilla/5.0'})
    archivoGuardar = id+'.jpg'
    if r.status_code == 200:
        with open('./images/'+id+'.jpg', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return (archivoGuardar)


projects = ['deng', 'danacommunity', 'danadriver', 'danarider', 'danacolombia', 'danafinance', 'dataanalytics', 'danac4b', 'datascience','danaip']

nodes_dict = {}
links_dict = {}
member_dict = {}


with open('./members.json', 'r') as f:
    members_json = json.load(f)
total_tarjetas = 0
for member in members_json:

    member_dict[member['profile']['name']] = {}


for i in range(10):
    p = projects[i]
    p_json = p + '.json'
    with open('./'+p_json, 'r') as f:
        p_json = json.load(f)

    dpt = i

    for story in p_json:
        total_tarjetas=total_tarjetas+1
        owners= story['owner_ids']
        requester = story['requested_by_id']
        estimated = story['estimate']
        if estimated == 0:
            estimated = 0.1
        if estimated == None:
            estimated = 0
        for member in members_json:
            if member['id'] == requester:
                requester_name = member['profile']['name']

        for o in owners:

            for member in members_json:

                if member['id'] == o:
                    owner_name = member['profile']['name']

            if dpt not in member_dict[owner_name]:
                member_dict[owner_name][dpt] = 1
            else:
                member_dict[owner_name][dpt] = member_dict[owner_name][dpt] + 1

            link = str(requester_name) + '->' + str(owner_name)
            if o not in nodes_dict:
            
                nodes_dict[o] = round(estimated,2)
            else:
                nodes_dict[o] = round(nodes_dict[o] + estimated,2)
        
            if link not in links_dict:
                links_dict[link]=1
            else:
                links_dict[link] = links_dict[link]+1




nodes_dict_name = {}
for node in nodes_dict:
    for member in members_json:
        if member['id'] == node:

            name = member['profile']['name']
            image = member['profile']['display_icon']
            if image is not None:
                url = image['url']+"?token="+api_token
                print ("\nDownloading image from: "+url)
                imagename = 'http://0.0.0.0:5000/images/'+imagedownload(url,member['id'])
                print ("Image user id: "+imagename)
            else:
                url = "https://cdn.apk-cloud.com/detail/image/com.cabify.rider-w130.png?r3"
                print ("\nDownloading image from: "+url)
                imagename = 'http://0.0.0.0:5000/images/'+imagedownload(url,member['id'])
                print ("Image user id: "+imagename)

            department = (max(member_dict[name].items(), key=operator.itemgetter(1))[0])
            nodes_dict_name_dpt = {}
            attributes = str(name) + '->' +  str(department) + '->' + imagename

            nodes_dict_name[attributes] = nodes_dict[node]


w = csv.writer(open("nodes.csv", "w"))
for key, val in nodes_dict_name.items():
    w.writerow([key, val])



w = csv.writer(open("links.csv", "w"))
for key, val in links_dict.items():
    w.writerow([key, val])

