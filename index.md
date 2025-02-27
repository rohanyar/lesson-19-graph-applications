**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Rohan Yarlagadda (rohany@udel.edu)
* Avinash Chouhan (avinashc@udel.edu)
* Ameer Abdelnasser (ameernas@udel.edu)

The focus of our project is to address various campus problems at the University of Delaware using algorithms such as Dijkstra, Prim's, and DFS. To accomplish this, we have developed two separate graphs that can be used to model and solve different types of problems.

The first graph is location-based and represents the different buildings on the UDel campus. By using algorithms like Dijkstra, we can find the shortest path between two buildings, which can be helpful in determining the most efficient way to get around campus. Additionally, we can use algorithms like Prim's to find the minimum spanning tree of the graph, which can help with planning and optimizing routes for maintenance and construction.

The second graph is based on courses and their prerequisites. By using algorithms like DFS, we can determine the path needed to take a certain course, which would help students plan and decide their future course choices. This information can be used to help students plan their academic schedules more effectively.

Overall, our project aims to provide solutions to a variety of campus problems by leveraging the power of algorithms and graph theory. By utilizing these tools, we can optimize routes, identify potential scheduling conflicts, and ultimately make life on campus a little bit easier for everyone.

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
import locationGraph
import classesNeeded
```

# Building Walkways

**Informal Description**: A contractor has decided to build walkways between locations on UD campus. Help the contractor find a way to build the walkways connecting locations using the least amount of materials.

> **Formal Description**:
>  * Input: Graph of locations of the Udel Campus, with weights representing the distance from one node to another.
>  * Output: An MST of the Udel Campus 

**Graph Problem/Algorithm**: MST (Prims)


**Setup code**:

```python
g = nx.Graph()
g.add_edge("Frazer Field", "Lil Bob", weight = 1)
g.add_edges_from([("Lil Bob", "Taylor"), ("Lil Bob", "Old College"), ("Lil Bob", "Brown Hall")], weight = 3)
g.add_edges_from([("Willard Hall", "McDowell Hall"), ("Willard Hall", "Old College"), ("Willard Hall", "Trabant")], weight = 2)
g.add_edge("Taylor", "Old College", weight = 1)
g.add_edges_from([("Brown Hall", "Harter"), ("Brown Hall", "Sypherd"), ("Brown Hall", "Sharp Hall")], weight = 1)
g.add_edges_from([("Harter", "Sypherd"), ("Harter", "Sharp Hall")], weight = 1)
g.add_edges_from([("Trabant", "Kirkbride"), ("Trabant", "Sharp Lab"), ("Trabant", "Ewing")], weight = 3)
g.add_edges_from([("Kirkbride", "Ewing"), ("Kirkbride", "Purnell"), ("Kirkbride", "Smith")], weight = 1)
g.add_edges_from([("Ewing", "Purnell"), ("Ewing", "Smith")], weight = 1)
g.add_edge("Purnell", "Smith", weight = 1)
g.add_edges_from([("Sharp Lab", "Wolf"), ("Sharp Lab", "Gore")], weight = 2)
g.add_edges_from([("Gore", "Mitchell"), ("Gore", "Memorial"), ("Gore", "Brown Lab"), ("Gore", "Smith")], weight = 2)
g.add_edges_from([("Brown Lab", "Colburn"), ("Brown Lab", "ICE")], weight = 4)
g.add_edges_from([("Morris", "Memorial"), ("Morris", "Allison"), ("Morris", "Perkins")], weight = 3)
g.add_edges_from([("Perkins", "Redding"), ("Perkins", "Russel"), ("Perkins", "Harrington")], weight = 3)
g.add_edges_from([("Harrington", "Russel"), ("Harrington", "Redding")], weight = 2)
g.add_edge("Redding", "Russel", weight = 2)
g.add_edges_from([("ICE", "Penny"), ("ICE", "Colburn"), ("ICE", "Spencer Lab")], weight = 3)
g.add_edge("Spencer Lab", "Colburn", weight = 2)
g.add_edges_from([("Allison", "Perkins"), ("Allison", "Penny")], weight = 4)

pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
plt.show()
```

**Visualization**:

![Graph of important buildings on UDel Campus](./locationGraph.png "UDel campus location graph")

**Solution code:**

```python
Prim_path = nx.minimum_spanning_tree(locationGraph.g, weight='weight', algorithm='prim', ignore_nan=False)
pos = nx.spring_layout(Prim_path)
nx.draw(Prim_path, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(Prim_path, 'weight')
nx.draw_networkx_edge_labels(Prim_path, pos, edge_labels=edge_labels)
plt.show()
```

**Output**

![Prims algorithm output graph](./PrimsPathFinal.png "MST of UD campus")

**Interpretation of Results**: This is an MST generated from the graph of campus. In other words, this shows us a way to connect all the vertices from campus together using the minimum possible total edge weight. So if the contractor wanted to build pathways using the least amount of materials he would follow this MST.

# Campus Shortest Path Problem

**Shortest Path Problem**: A student want's to figure out the fastest way to get from one building on campus to another. It's integral for them to find the fastest path as they are late for a meeting. Help the student find the shortest path from their current location to their meeting location. 

> **Formal Description**:
>  * Input: Graph of locations of the Udel Campus, with weights representing the distance from one node to another. 
>  * Output: A path of the shortest distance from the start to the target location. 

**Graph Problem/Algorithm**: Dijkstra's Algorithm


**Setup code**:

```python
class locationGraph: 


    g = nx.Graph()
    g.add_edge("Frazer Field", "Lil Bob", weight = 1)
    g.add_edges_from([("Lil Bob", "Taylor"), ("Lil Bob", "Old College"), ("Lil Bob", "Brown Hall")], weight = 3)
    g.add_edges_from([("Willard Hall", "McDowell Hall"), ("Willard Hall", "Old College"), ("Willard Hall", "Trabant")], weight = 2)
    g.add_edge("Taylor", "Old College", weight = 1)
    g.add_edges_from([("Brown Hall", "Harter"), ("Brown Hall", "Sypherd"), ("Brown Hall", "Sharp Hall")], weight = 1)
    g.add_edges_from([("Harter", "Sypherd"), ("Harter", "Sharp Hall")], weight = 1)
    g.add_edges_from([("Trabant", "Kirkbride"), ("Trabant", "Sharp Lab"), ("Trabant", "Ewing")], weight = 3)
    g.add_edges_from([("Kirkbride", "Ewing"), ("Kirkbride", "Purnell"), ("Kirkbride", "Smith")], weight = 1)
    g.add_edges_from([("Ewing", "Purnell"), ("Ewing", "Smith")], weight = 1)
    g.add_edge("Purnell", "Smith", weight = 1)
    g.add_edges_from([("Sharp Lab", "Wolf"), ("Sharp Lab", "Gore")], weight = 2)
    g.add_edges_from([("Gore", "Mitchell"), ("Gore", "Memorial"), ("Gore", "Brown Lab"), ("Gore", "Smith")], weight = 2)
    g.add_edges_from([("Brown Lab", "Colburn"), ("Brown Lab", "ICE")], weight = 4)
    g.add_edges_from([("Morris", "Memorial"), ("Morris", "Allison"), ("Morris", "Perkins")], weight = 3)
    g.add_edges_from([("Perkins", "Redding"), ("Perkins", "Russel"), ("Perkins", "Harrington")], weight = 3)
    g.add_edges_from([("Harrington", "Russel"), ("Harrington", "Redding")], weight = 2)
    g.add_edge("Redding", "Russel", weight = 2)
    g.add_edges_from([("ICE", "Penny"), ("ICE", "Colburn"), ("ICE", "Spencer Lab")], weight = 3)
    g.add_edge("Spencer Lab", "Colburn", weight = 2)
    g.add_edges_from([("Allison", "Perkins"), ("Allison", "Penny")], weight = 4)

```

**Visualization**:

![Graph of important buildings on UDel Campus](./graphviz.png "UDel campus location graph")

**Solution code:**

```python
class dijkstra: 
    import networkx as nx
    import locationGraph

    # Find shortest path from Willard Hall to Perkins
    ans_path = nx.dijkstra_path(locationGraph.g, "Willard Hall", "Perkins")
    print(f'To get from Willard to Perkins using the shortest path you need to follow this path:\n\t{ans_path}')
```

**Output**

```python
To get from Willard to Perkins using the shortest path you need to follow this path:     
        ['Willard Hall', 'Trabant', 'Sharp Lab', 'Gore', 'Memorial', 'Morris', 'Perkins']
```

**Interpretation of Results**: If a student located at Willard Hall wants to travel to reach Perkins as fast as possible they would have to follow this path, ['Willard Hall', 'Trabant', 'Sharp Lab', 'Gore', 'Memorial', 'Morris', 'Perkins']. This is the shortest path from Willard to perkins and would therefore take the shortest amount of time. 

# FIND COURSES NEEDED FOR BS COMPUTER SCIENCE MAJOR

**Informal Description**: 
Find courses needed problem: Iterates through all nodes and edges to find all the classes on the graph that a computer science student needs to take. It then groups up all of these classes through their connections and shows what classes a student needs to take in each subject breaking down enlgish, science, and math/computer science. This is important because if a student needs to know what classes to take, this graph and DFS algorithm shows the student the order of which classes to take.

> **Formal Description**:
>  * Input: Graph of classes, with same topic/pre-req nodes connected to eachoteher
>  * Output: 3 seperate groups of connected nodes representing which pre-reqs to take for which class, and the specific classes to take for each subject.

**Graph Problem/Algorithm**: DFS


**Setup code**:

```python

class classesNeeded: 
    import matplotlib.pyplot as plt
    import networkx as nx

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
    g.add_edges_from([("CISC181", "CISC250"), ("CISC250", "CISC450"),("CISC450", "CISC459")])
    nx.draw(g,node_color = "red",with_labels=True, node_size= 330 )
    plt.show()
```

**Visualization**:
![DFS graph image](./DFS_Graph.png)

**Solution code:**

```python
dfsEdges = nx.edge_dfs(classesNeeded.g,source=None, orientation=None)
DfsList = list(dfsEdges)
print(DfsList)
```

**Output**
```python
[('CISC108', 'CISC181'), ('CISC108', 'CISC210'), ('CISC210', 'CISC275'), ('CISC275', 'CISC474'), ('CISC210', 'CISC220'), ('CISC220', 'CISC320'), ('CISC320', 'MATH210'), ('MATH210', 'MATH241'), ('CISC220', 'CISC361'), ('CISC361', 'CISC260'), ('CISC260', 'CISC210'), ('CISC260', 'CISC372'), ('CISC372', 'CISC220'), ('CISC220', 'CISC304'), ('ENGL110', 'ENGL410'), ('GEOL105L', 'GEOL107'), ('GEOL107', 'GEOL107L'), ('GEOL105L', 'GEOL105'), ('CISC450', 'CISC459')]
```
**Interpretation of Results**: The list represents the different subjects and the pathway of the classes you must take. So for example to take ENGL410, you must take ENGL110 first. Also it seperates subjects that do not correlate with eachother. For example, science(geology) pre-reqs do not affect the ability to take any of the computer science or math classes, but to take some of the math and computer science classes, you must take certain pre-reqs in that subject.