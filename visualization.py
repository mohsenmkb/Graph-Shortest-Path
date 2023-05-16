import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

routes = pd.read_csv('routes.csv')

edge_list = []

for index,row in routes.iterrows():
    edge_list.append((row['from'],row['to'],{'distance':row['distance']}))

G = nx.DiGraph(edge_list)

pos = nx.spring_layout(G, k=0.8)
edge_labels = nx.get_edge_attributes(G, "distance")

plt.figure(figsize=(20, 12))
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,label_pos=0.5)
nx.draw(G, pos=pos, node_size=700, with_labels=True,connectionstyle="arc3, rad = 0.1")

plt.savefig("routes.png")