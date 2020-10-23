############################## Basic Definition ########################
# 1. Network = Graph = (nodes,eddge)
# 2. Directed or Undirected 
# - Undirected : Facebook
# - Directed : Twitter
# 3. networkx : API for analysis of Graph
# 4. nxviz : API for creating beautiful and rational graph viz

import networkx as nx
G.nodes()
G.edges()
len(G.nodes())
len(G.edges())

type(G) #Check type of Graph

import nxviz as nv 
import matplotlib.pyplot as plt

c = nv.CircosPlot(G)
c.draw()
plt.show()

############################# Task 1 (Exploratory data analysis)
type(G)
len(G.nodes())
len(G.edges())

############################ Task 2 (Plotting using nxviz)
# Create the CircosPlot object: c
c = CircosPlot(G,node_color='bipartite',node_grouping='bipartite',node_order='centrality')

# Draw c to the screen
c.draw()

# Display the plot
plt.show()


############################ Bipartite Graph ##############################
# A graph that is partitioned into two sets
# nodes are only connected to nodes in other portitions
# contrast : 'unipartitie'
# Degree Centrality : measure nodes importance
# number of possible neighbors depend on graph type


import networkx as nx
G = nx.Graph()

numbers = range(3)
G.add_nodes_from(numbers, bipartite='customers')

letters = ['a','b']
G.add_nodes_from(letters, bipartite = 'products')

cust_nodes = [n for n,d in G.nodes(data=True) if d['bipartite']=='customers']
nx.bipartite.degree_centrality(G,cust_nodes)


############################## Task 1 (The bipartite keyword)
# Define get_nodes_from_partition()
def get_nodes_from_partition(G,partition):
    # Initialize an empty list for nodes to be returned
    nodes = []
    # Iterate over each node in the graph G
    for n in G.nodes():
        # Check that the node belongs to the particular partition
        if G.nodes[n]['bipartite'] == partition:
            # If so, append it to the list of nodes
            nodes.append(n)
    return nodes

# Print the number of nodes in the 'projects' partition
print(len(get_nodes_from_partition(G, 'projects')))

# Print the number of nodes in the 'users' partition
print(len(get_nodes_from_partition(G, 'users')))

############################## Task 2 (Degree centrality distribution of user nodes)
# Import matplotlib
import matplotlib.pyplot as plt

# Get the 'users' nodes: user_nodes
user_nodes = get_nodes_from_partition(G,'users')

# Compute the degree centralities: dcs
dcs = nx.degree_centrality(G)

# Get the degree centralities for user_nodes: user_dcs
user_dcs = [dcs[n] for n in user_nodes]

# Plot the degree distribution of users_dcs
plt.yscale('log')
plt.hist(user_dcs, bins=20)
plt.show()

############################ Task 3 (Degree centrality distribution of project nodes)
# Get the 'projects' nodes: project_nodes
project_nodes = get_nodes_from_partition(G,'projects')

# Compute the degree centralities: dcs
dcs = nx.degree_centrality(G)

# Get the degree centralities for project_nodes: project_dcs
project_dcs = [dcs[n] for n in project_nodes]

# Plot the degree distribution of project_dcs
plt.yscale('log')
plt.hist(project_dcs, bins=20)
plt.show()


########################### Bipartite & Recommendation System ##############################
G.nodes(data=True)
G.edges()
user_nbr1 = G.neighbors('user1')
user_nbr2 = G.neighbors('user2')

set(user_nbr1).intersection(user_nbr2) # find instersection 
set(user_nbr1).difference(user_nbr2) # find difference

########################### Task 1 (Shared nodes in other partition)
def shared_partition_nodes(G,node1,node2):
    # Check that the nodes belong to the same partition
    assert G.nodes[node1]['bipartite'] == G.nodes[node2]['bipartite']

    # Get neighbors of node 1: nbrs1
    nbrs1 = G.neighbors(node1)
    # Get neighbors of node 2: nbrs2
    nbrs2 = G.neighbors(node2)

    # Compute the overlap using set intersections
    overlap = set(nbrs1).intersection(nbrs2)
    return overlap

# Print the number of shared repositories between users 'u7909' and 'u2148'
print(len(shared_partition_nodes(G,'u7909','u2148')))

########################### Task 2 (User similarity metric)
def user_similarity(G, user1, user2, proj_nodes):
    # Check that the nodes belong to the 'users' partition
    assert G.nodes[user1]['bipartite'] == 'users'
    assert G.nodes[user2]['bipartite'] == 'users'

    # Get the set of nodes shared between the two users
    shared_nodes = shared_partition_nodes(G,user1,user2)

    # Return the fraction of nodes in the projects partition
    return len(shared_nodes) / len(proj_nodes)

# Compute the similarity score between users 'u4560' and 'u1880'
project_nodes = get_nodes_from_partition(G,'projects')
similarity_score = user_similarity(G,'u4560','u1880',project_nodes)

print(similarity_score)

############################ Task 3 (Find similar users)
from collections import defaultdict

def most_similar_users(G, user, user_nodes, proj_nodes):
    # Data checks
    assert G.nodes[user]['bipartite'] == 'users'

    # Get other nodes from user partition
    user_nodes = set(user_nodes)
    user_nodes.remove(user)

    # Create the dictionary: similarities
    similarities = defaultdict(list)
    for n in user_nodes:
        similarity = user_similarity(G, user, n, proj_nodes)
        similarities[similarity].append(n)

    # Compute maximum similarity score: max_similarity
    max_similarity = max(similarities.keys())

    # Return list of users that share maximal similarity
    return similarities[max_similarity]

user_nodes = get_nodes_from_partition(G, 'users')
project_nodes = get_nodes_from_partition(G, 'projects')

print(most_similar_users(G, 'u4560', user_nodes, project_nodes))

############################ Task 4 (Recommend repositories)
def recommend_repositories(G,from_user,to_user):
    # Get the set of repositories that from_user has contributed to
    from_repos = set(G.neighbors(from_user))
    # Get the set of repositories that to_user has contributed to
    to_repos = set(G.neighbors(to_user))

    # Identify repositories that the from_user is connected to that the to_user is not connected to
    return from_repos.difference(to_repos)

# Print the repositories to be recommended
print(recommend_repositories(G,'u7909','u2148'))


