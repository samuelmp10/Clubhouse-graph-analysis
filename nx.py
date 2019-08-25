import networkx as nx
import json
import csv
import community
from networkx.readwrite import json_graph


with open('./nodes.csv',encoding="utf8",newline='\n') as infile:
    reader = csv.reader(infile)
    nodes_dict = {rows[0]:rows[1] for rows in reader}

with open('./links.csv',encoding="utf8",newline='\n') as infile:
    reader = csv.reader(infile)
    links_dict = {rows[0]:rows[1] for rows in reader}

g = nx.Graph()
list_nodes=[]
for k, v in links_dict.items():
    requester, owner = k.split('->')
    g.add_edge(requester, owner, weight=float(v))
    for k, v in nodes_dict.items():
        name, dpt, image = k.split('->')
        list_nodes.append(name)


    if requester not in list_nodes:
        requester_full=str(requester)+'->'+str(10)+'->'+'None'
        nodes_dict[requester_full] = 0

for k, v in nodes_dict.items():
    name, dpt, img = k.split('->')
    g.add_node(name, weight=float(v), department=int(dpt), image=img)
    

for k, v in links_dict.items():
    requester, owner = k.split('->')
    g.add_edge(requester, owner, weight=float(v))


partition = community.best_partition(g, weight='weight')

node_list = list(g.nodes())


for n in node_list:
    g.node[n]['community'] = partition[n]


d = json_graph.node_link_data(g)

json_string=json.dumps(d, ensure_ascii=False).encode('utf8')


with open('./web/graph.json', 'w') as file:
    file.write(json_string.decode('utf8'))
