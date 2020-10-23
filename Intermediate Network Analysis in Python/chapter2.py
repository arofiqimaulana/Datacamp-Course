############################### Concept of Projection ##################################
# useful to investigate the relationship between nodes one partition
import networkx as nx 
G = nx.read_edgeList('american-revolution.txt')
G.edges(data=True)[0:5

# Bipartite projection
cust_nodes = [n for n in G.nodes() if G.node[n]['bipartitie']=='customers']
G_cust = nx.bipartitie.projected_graph(G,cust_nodes)
G_cust.nodes()
G_cust.edges()

# Degree Centrality
nx.bipartitie.degree_centrality(G,cust_nodes) # we should define other partition
nx.degree_centrality(G)

############################## Task 1 (Reading graphs)
# Import networkx
import networkx as nx

# Read in the data: g
G = nx.read_edgelist('american-revolution.edgelist')

# Assign nodes to 'clubs' or 'people' partitions
for n, d in G.nodes(data=True):
    if '.' in n:
        G.nodes[n]['bipartite'] = 'people'
    else:
        G.nodes[n]['bipartite'] = 'clubs'
        
# Print the edges of the graph
print(G.edges())


############################# Task 2 (Exercise Computing projection)
# Prepare the nodelists needed for computing projections: people, clubs
# This exercise shows you two ways to do it, one with `data=True` and one without.
people = [n for n in G.nodes() if G.nodes[n]['bipartite'] == 'people']
clubs = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'clubs']

# Compute the people and clubs projections: peopleG, clubsG
peopleG = nx.bipartite.projected_graph(G,people)
clubsG = nx.bipartite.projected_graph(G,clubs)


########################### Task 3 (Plot degree centrality on projection)
import matplotlib.pyplot as plt

# Plot the degree centrality distribution of both node partitions from the original graph
plt.figure() 
original_dc = nx.bipartite.degree_centrality(G, people)  
# Remember that you can cast a dictionary values to a list.
plt.hist(original_dc.values(), alpha=0.5)
plt.yscale('log')
plt.title('Bipartite degree centrality')
plt.show()


# Plot the degree centrality distribution of the peopleG graph
plt.figure()
people_dc = nx.degree_centrality(peopleG)
plt.hist(people_dc.values())
plt.yscale('log')
plt.title('Degree centrality of people partition')
plt.show()

# Plot the degree centrality distribution of the clubsG graph
plt.figure()
clubs_dc = nx.degree_centrality(clubsG)
plt.hist(clubs_dc.values())
plt.yscale('log')
plt.title('Degree centrality of clubs partition')
plt.show()

########################### Bipartite Graph as matrix ##################################
# rows = nodes on one partition
# columns = nodes on other partition
# cell : 1 if edge present

cust_nodes = [n for n in G.nodes() if G.node[n]['bipartite']=='customers']
prod_nodes = [n for n in G.nodes() if G.node[n]['bipartite']=='products']

mat = nx.bipartite.biadjency_matrix(G,row_order=cust_nodes,column_order=prod_nodes) #sparse matrix

mat @ mat.T # Matrix multipication

########################### Task 1 (Compute adjacency matrix)
# Get the list of people and list of clubs from the graph: people_nodes, clubs_nodes
people_nodes = get_nodes_from_partition(G,'people')
clubs_nodes = get_nodes_from_partition(G,'clubs')

# Compute the biadjacency matrix: bi_matrix
bi_matrix = nx.bipartite.biadjacency_matrix(G, row_order=people_nodes, column_order=clubs_nodes)

# Compute the user-user projection: user_matrix
user_matrix = bi_matrix @ bi_matrix.T

print(user_matrix)

######################### Task 2 (Find shared membership: Transposition)
# Find out the names of people who were members of the most number of clubs
import numpy as np

# Find out the names of people who were members of the most number of clubs
diag = user_matrix.diagonal() 
indices = np.where(diag == diag.max())[0]  
print('Number of clubs: {0}'.format(diag.max()))
print('People with the most number of memberships:')
for i in indices:
    print('- {0}'.format(people_nodes[i]))

# Set the diagonal to zero and convert it to a coordinate matrix format
user_matrix.setdiag(0)
users_coo = user_matrix.tocoo()

# Find pairs of users who shared membership in the most number of clubs
indices2 = np.where(users_coo.data == users_coo.data.max())[0]
print('People with most number of shared memberships:')
for idx in indices2:
    print('- {0}, {1}'.format(people_nodes[users_coo.row[idx]], people_nodes[users_coo.col[idx]])) 

######################## Representasing network data with pandas ############################
G.nodes(data=True)

nodeList = []
for n,d in G.nodes(data=True):
    node_data = dict()
    node_data['n'] = n
    node_data.update(n)
    nodeList.append(node_data)

pd.DataFrame(nodeList)


########################### Task 1 (Make nodelist)
# Initialize a list to store each edge as a record: nodelist
nodelist = []
for n, d in G_people.nodes(data=True):
    # nodeinfo stores one "record" of data as a dict
    nodeinfo = {'person': n} 
    
    # Update the nodeinfo dictionary 
    nodeinfo.update(d)
    
    # Append the nodeinfo to the node list
    nodelist.append(nodeinfo)
    

# Create a pandas DataFrame of the nodelist: node_df
node_df = pd.DataFrame(nodelist)
print(node_df.head())

########################## Task 2 (Make edgelist)
# Initialize a list to store each edge as a record: edgelist
edgelist = []
for n1, n2, d in G_people.edges(data=True):
    # Initialize a dictionary that shows edge information: edgeinfo
    edgeinfo = {'node1':n1, 'node2':n2}
    
    # Update the edgeinfo data with the edge metadata
    edgeinfo.update(d)
    
    # Append the edgeinfo to the edgelist
    edgelist.append(edgeinfo)
    
# Create a pandas DataFrame of the edgelist: edge_df
edge_df = pd.DataFrame(edgelist)
print(edge_df.head())