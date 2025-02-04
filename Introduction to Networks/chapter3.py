############################### Communalities & Cliques ################################
# Group of nodes that fully connected 
# simplest Cliques = edges
# simplest complex cliques = triangle
# Friend recommendation system (A knows B, B knows C, then there is probability A knows C)
from itertools import combinations
for n1,n2 in combinations(G.nodes(),2):
    print(n1,n2)

############################## Task 1 (Identifying triangle relationships)
# cek apakah yang mempunyai pekerjaan yang sama memiliki network
from itertools import combinations

# Define is_in_triangle()
def is_in_triangle(G, n):
    """
    Checks whether a node `n` in graph `G` is in a triangle relationship or not.

    Returns a boolean.
    """
    in_triangle = False

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):

        # Check if an edge exists between n1 and n2
        if G.has_edge(n1,n2):
            in_triangle = True
            break
    return in_triangle

############################### Task 2 (Finding nodes involved in triangles)
from itertools import combinations

# Write a function that identifies all nodes in a triangle relationship with a given node.
def nodes_in_triangle(G, n):
    """
    Returns the nodes in a graph `G` that are involved in a triangle relationship with the node `n`.
    """
    triangle_nodes = set([n])

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):

        # Check if n1 and n2 have an edge between them
        if G.has_edge(n1,n2):

            # Add n1 to triangle_nodes
            triangle_nodes.add(n1)

            # Add n2 to triangle_nodes
            triangle_nodes.add(n2)

    return triangle_nodes

# Write the assertion statement
assert len(nodes_in_triangle(T, 1)) == 35

############################## Task 3 (Finding open triangles)
# adalah triangles yang tidak sempurna
# Let us now move on to finding open triangles! Recall that they form the basis of friend recommendation systems; 
# if "A" knows "B" and "A" knows "C", then it's probable that "B" also knows "C".
from itertools import combinations

# Define node_in_open_triangle()
def node_in_open_triangle(G, n):
    """
    Checks whether pairs of neighbors of node `n` in graph `G` are in an 'open triangle' relationship with node `n`.
    """
    in_open_triangle = False

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):

        # Check if n1 and n2 do NOT have an edge between them
        if not G.has_edge(n1,n2):

            in_open_triangle = True

            break

    return in_open_triangle

# Compute the number of open triangles in T
num_open_triangles = 0

# Iterate over all the nodes in T
for n in T.nodes():

    # Check if the current node is in an open triangle
    if node_in_open_triangle(T,n):

        # Increment num_open_triangles
        num_open_triangles += 1

print(num_open_triangles)

#################################### Maximal Cliques ############################
# a cliques that, when we extended by one node is no longer clique
# Maximal cliques are cliques that cannot be extended by adding an adjacent edge,
# and are a useful property of the graph when finding communities
nx.find_cliques(G)# find max clique


#################################### Task 1 (Finding all maximal cliques of size "n")
# Define maximal_cliques()
def maximal_cliques(G,size):
    """
    Finds all maximal cliques in graph `G` that are of size `size`.
    """
    mcs = []
    for clique in nx.find_cliques(G):
        if len(clique) == size:
            mcs.append(clique)
    return mcs

# Check that there are 33 maximal cliques of size 3 in the graph T
assert len(maximal_cliques(T,3)) == 33


#################################### Subgraph ##########################################
import networkx as nx
G = nx.erdos_renyi_graph(n=20,p=0.2)
G.nodes()

nodes = G.neighbors(8)
nodes
nodes.append(8)

# Subgraph
G_eight = G.subgraph(nodes)
G_eight.nodes()

nx.draw(G_eight,with_label=True)

################################### Task 1 (Subgraphs I)
nodes_of_interest = [29, 38, 42]

# Define get_nodes_and_nbrs()
def get_nodes_and_nbrs(G, nodes_of_interest):
    """
    Returns a subgraph of the graph `G` with only the `nodes_of_interest` and their neighbors.
    """
    nodes_to_draw = []

    # Iterate over the nodes of interest
    for n in nodes_of_interest:

        # Append the nodes of interest to nodes_to_draw
        nodes_to_draw.append(n)

        # Iterate over all the neighbors of node n
        for nbr in G.neighbors(n):

            # Append the neighbors of n to nodes_to_draw
            nodes_to_draw.append(nbr)

    return G.subgraph(nodes_to_draw)

# Extract the subgraph with the nodes of interest: T_draw
T_draw = get_nodes_and_nbrs(T,nodes_of_interest)

# Draw the subgraph to the screen
nx.draw(T_draw)
plt.show()


###################################### Task 2 (Subgraphs II)
# Extract the nodes of interest: nodes
nodes = [n for n, d in T.nodes(data=True) if d['occupation'] == 'celebrity']

# Create the set of nodes: nodeset
nodeset = set(nodes)

# Iterate over nodes
for n in nodes:

    # Compute the neighbors of n: nbrs
    nbrs = T.neighbors(n)

    # Compute the union of nodeset and nbrs: nodeset
    nodeset = nodeset.union(nbrs)

# Compute the subgraph using nodeset: T_sub
T_sub = T.subgraph(nodeset)

# Draw T_sub to the screen
nx.draw(T_sub)
plt.show()

