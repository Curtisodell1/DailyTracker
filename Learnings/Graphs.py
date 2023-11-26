#graph problems presented by Structy and other sources


#The goal of this problem is to return the number of connected nodes in a graph 
def connected_components_count(graph):
    #here we are defining two variables one to determine 
    #if a node has been visited and keep track of how many there are
    visited = set()
    count = 0

    #using an iterative approach do a depth first search on the nodes
    for node in graph:
        #for each node we'll run the function 'explore' giving us 
        #upon running through explore function we will increment 'count' only if we have received a return value of True
        if explore(graph, node, visited) == True:
            count += 1
    return count

#we'll use current as the current node to see if it exists within our visited set
def explore(graph, current, visited):
    if current in visited: 
        #returning false will exit us from exploring this node if it has already been visited (used to stop repeat visits)
        return False
    #if we haven't visited it we'll add it to our set and explore all neighbors
    visited.add(current)
    
    #again, we are running a depth first search so going as deeply as possible on the tree
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True

