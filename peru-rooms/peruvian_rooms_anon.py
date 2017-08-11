import networkx as nx
import matplotlib.pyplot as plt


girls = {
'1' : ['8', '7', '5'],
'2' : ['5', '7', '4'],
'3' : ['4', '5', '7'],
'4' : ['3', '5'],
'5' : ['7', '1'],
'6' : ['10', '9', '2'],
'7' : ['5', '1'],
'8' : ['1', '7', '5'],
'9' : ['10', '11', '14'],
'10' : ['9', '2', '14'],
'11' : ['13', '12', '14'],
'12' : ['13', '11', '20'],
'13' : ['12', '11', '14'],
'14' : ['19', '23', '20'],
'15' : ['19', '22', '18'],
'16' : ['17', '18', '15'],
'17' : ['16', '18', '15'],
'18' : ['17', '22', '15'],
'19' : ['23', '20', '14'],
'20' : ['19', '23', '14'],
'21' : ['18', '22', '15'],
'22' : ['21', '16', '15'],
'23' : ['19', '20', '14'],
'24' : ['29', '26', '25'],
'25' : ['28', '26', '24'],
'26' : ['27', '24', '25'],
'27' : ['29', '26', '25'],
'28' : ['29', '26', '25'],
'29' : ['27', '24', '26', '28']
}

# Create graph
#G = nx.MultiDiGraph()
G = nx.Graph()

# Add nodes
for girl in girls.keys():
    G.add_node(girl)
    
# Add edges
for girl in G.nodes():
    for friend in girls[girl]:
        if friend in G.nodes() and girl in G.neighbors(friend):
            G.remove_edge(friend, girl)
            G.add_edge(girl, friend, color='r', weight=2)
        else:
            G.add_edge(girl, friend, color='g', weight=1)

# Layout
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]
pos = nx.spring_layout(G)

# Draw graph
nx.draw(G, edge_color=colors, node_color='w', node_size=1, width=weights, with_labels=True)        
plt.show()
