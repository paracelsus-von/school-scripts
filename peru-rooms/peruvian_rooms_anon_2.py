import networkx as nx
import matplotlib.pyplot as plt


girls = {
'1'  : ['8', '7', '5'],
'2'  : ['5', '7', '4'],
'3' : ['4', '5', '7'],
'4'   : ['3', '5'],
'5' : ['7', '1'],
'6'  : ['10', '9', '2'],
'7' : ['5', '1'],
'8' : ['1', '7', '5'],
'9'    : ['10'],
'10'  : ['9', '2'] 
}

# Create graph
G = nx.MultiDiGraph()
#G = nx.Graph()

# Add nodes
for girl in girls.keys():
    G.add_node(girl)
    
# Add edges
for girl in G.nodes():
    for friend in girls[girl]:
        #if friend in G.nodes() and girl in G.neighbors(friend):
        #    G.add_edge(girl, friend, color='r', weight=2)
        #else:
        #    G.add_edge(girl, friend, color='g', weight=1)
        G.add_edge(girl, friend, color='g', weight=1)

# Layout
#edges = G.edges()
#colors = [G[u][v]['color'] for u,v in edges]
#weights = [G[u][v]['weight'] for u,v in edges]
pos = nx.spring_layout(G)

# Draw graph
nx.draw(G, node_color='w', node_size=700, with_labels=True)        
plt.show()
