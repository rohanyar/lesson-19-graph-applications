import networkx as nx
import classesNeeded

'''
g = nx.Graph()
g.add_edge("CISC108", "CISC181")
g.add_edges_from([("CISC210", "CISC275"), ("CISC210", "CISC220"), ("CISC210", "CISC260")])
g.add_edge("CISC108", "CISC210")
g.add_edge("MATH210", "CISC320")
g.add_edges_from([("CISC220", "CISC320"), ("CISC220", "CISC361"), ("CISC220", "CISC304"),("CISC220","CISC372")])
g.add_edges_from([("CISC260", "CISC361"), ("CISC260", "CISC372")])
g.add_edge("MATH241", "MATH210")
g.add_edge("ENGL110", "ENGL410")
g.add_edge("GEOL105L", "GEOL107")
g.add_edge("GEOL105", "GEOL105L")
g.add_edge("GEOL107", "GEOL107L")
g.add_edge("CISC275", "CISC474")
nx.draw(g,node_color = "red",with_labels=True, node_size= 330 )
plt.show()
'''

dfsEdges = nx.edge_dfs(classesNeeded.g,source=None, orientation=None)
DfsList = list(dfsEdges)
print(DfsList)