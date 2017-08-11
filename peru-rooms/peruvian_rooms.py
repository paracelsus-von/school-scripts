import pydot
import networkx as nx
import matplotlib.pyplot as plt
import graphviz as gv

girls = {
'Katya Bach'   : ['Zoe Liwicki', 'Issy Bostock', 'Bea Ritchie'],
'Lucy Rose'    : ['Bea Ritchie', 'Issy Bostock', 'Kristen Pickford'],
'Lucy Riddell' : ['Kristen Pickford', 'Bea Ritchie', 'Issy Bostock'],
'Kristen Pickford' : ['Lucy Riddell', 'Bea Ritchie'],
'Bea Ritchie'  : ['Issy Bostock', 'Katya Bach'],
'Cleme Fry'    : ['Ella North', 'Eloise', 'Lucy Rose'],
'Issy Bostock' : ['Bea Ritchie', 'Katya Bach'],
'Zoe Liwicki'  : ['Katya Bach', 'Issy Bostock', 'Bea Ritchie'],
'Eloise'       : ['Ella North', 'Jamie King', 'Livy Li'],
'Ella North'   : ['Eloise', 'Lucy Rose', 'Livy Li'],
'Jamie King'   : ['Sherri', 'Lucy Ma', 'Livy Li'],
'Lucy Ma'      : ['Sherri', 'Jamie King', 'Coco'],
'Sherri'       : ['Lucy Ma', 'Jamie King', 'Livy Li'],
'Livy Li'      : ['Chloe', 'Natalie', 'Coco'],
'Sunny'        : ['Chloe', 'Elaine', 'Sophie'],
'Jasmin'       : ['Odelia', 'Sophie', 'Sunny'],
'Odelia'       : ['Jasmin', 'Sophie', 'Sunny'],
'Sophie'       : ['Odelia', 'Elaine', 'Sunny'],
'Chloe'        : ['Natalie', 'Coco', 'Livy Li'],
'Coco'         : ['Chloe', 'Natalie', 'Livy Li'],
'Janet'        : ['Sophie', 'Elaine', 'Sunny'],
'Elaine'       : ['Janet', 'Jasmin', 'Sunny'],
'Natalie'      : ['Chloe', 'Coco', 'Livy Li'],
'Lucy Rigby'   : ['Bea Learmouth', 'Gemma', 'Sammy'],
'Sammy'        : ['Juliet', 'Gemma', 'Lucy Rigby'],
'Gemma'        : ['Katie Rigby', 'Lucy Rigby', 'Sammy'],
'Katie Rigby'  : ['Bea Learmouth', 'Gemma', 'Sammy'],
'Juliet'       : ['Bea Learmouth', 'Gemma', 'Sammy'],
'Bea Learmouth' : ['Katie Rigby', 'Lucy Rigby', 'Gemma', 'Juliet'],
'Isha'         : []
}



# Create graph
G = nx.DiGraph()

# Add nodes
for girl in girls.keys():
    G.add_node(girl)
    
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
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]

# subgraphs
F = nx.DiGraph()
for H in nx.strongly_connected_component_subgraphs(G):
    F = nx.compose(F,H)
    print H.nodes()
    print ("\n")
    #plt.figure() # plots subgraphs on separate windows
    #colors_2 = [G[u][v]['color'] for u,v in H.edges()]
    #weights_2 = [G[u][v]['weight'] for u,v in H.edges()]
    #nx.draw(H, edge_color = colors_2, node_color='w', node_size=100, width=weights_2, with_labels=True)
#plt.show()

colors_2 = [G[u][v]['color'] for u,v in F.edges()]
weights_2 = [G[u][v]['weight'] for u,v in F.edges()]
arrows_2 = [G[u][v]['color']=='g' for u,v in F.edges()]
pos = nx.spring_layout(G,k=0.15,iterations=20)


# Draw graph
nx.write_gexf(G, "test.gexf")

nx.draw(F, pos, edge_color=colors_2, node_color='w', node_size=1, width=weights_2, with_labels=True, arrows=arrows_2)        
plt.show()