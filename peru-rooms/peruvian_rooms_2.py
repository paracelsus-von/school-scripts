import networkx as nx
import matplotlib.pyplot as plt


girls = {
'Katya Bach'   : ['Zoe Liwicki', 'Issy Bostock', 'Bea Ritchie'],
'Lucy Rose'    : ['Bea Ritchie', 'Issy Bostock', 'Kristen Pickford'],
'Lucy Riddell' : ['Kristen Pickford', 'Bea Ritchie'],#, 'Issy Bostock'],
'Kristen Pickford': ['Lucy Riddell', 'Bea Ritchie'],
'Bea Ritchie'  : ['Issy Bostock', 'Katya Bach'],
'Cleme Fry'    : ['Ella North', 'Eloise', 'Lucy Rose'],
'Issy Bostock' : ['Bea Ritchie', 'Katya Bach'],
'Zoe Liwicki'  : ['Katya Bach', 'Issy Bostock', 'Bea Ritchie'],
'Eloise'       : ['Ella North'],
'Ella North'   : ['Eloise', 'Lucy Rose']
}

positions = {
'Katya Bach'   : (-2.5,-2),
'Lucy Rose'    : (2,0),
'Lucy Riddell' : (-2,2),
'Kristen Pickford': (0,3),
'Bea Ritchie'  : (-1,0),
'Cleme Fry'    : (5,-2),
'Issy Bostock' : (-1,-7),
'Zoe Liwicki'  : (-7,-1),
'Eloise'       : (10,3),
'Ella North'   : (4,2)
}

# Create graph
G = nx.MultiDiGraph()
#G = nx.Graph()

# Add nodes
for girl in girls.keys():
    G.add_node(girl, pos=positions[girl])
    
# Add edges
for girl in G.nodes():
    for friend in girls[girl]:
        if friend in G.nodes() and girl in G.neighbors(friend):
            G.remove_edge(friend, girl)
            G.add_edge(girl, friend, color='r', weight=2)
            G.add_edge(friend, girl, color='r', weight=2)
        else:
            G.add_edge(girl, friend, color='g', weight=1)

# Layout
edges = G.edges()
colors = [G[u][v][0]['color'] for u,v in edges]
weights = [G[u][v][0]['weight'] for u,v in edges]
pos = nx.get_node_attributes(G,'pos')

# Draw graph
nx.draw(G, pos, edge_color=colors, width=weights, node_color='w', node_size=1, with_labels=True)        
plt.show()
