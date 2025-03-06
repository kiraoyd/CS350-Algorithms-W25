def dfs_wrapper(matrix, start, total_nodes):
    visited = [False] * (total_nodes)
    node_traversal_order = []

    #Make the first call to "visit" the start node
    dfs_recursive_matrix(matrix, start, total_nodes, visited, node_traversal_order)

    print(node_traversal_order) #after we return all the way back, we should have visited all nodes

def dfs_recursive_matrix(graph, current_node, total_nodes, visited, node_traversal_order):
    if current_node >= total_nodes:
        return

    visited[current_node] = True
    node_traversal_order.append(current_node)

    neighbor = 0
    while neighbor < total_nodes:
        if graph[current_node][neighbor] == 1 and visited[neighbor] == False:
            dfs_recursive_matrix(matrix, neighbor, total_nodes, visited, node_traversal_order)
        neighbor += 1




#---MAIN CALLING ROUTINE---#

matrix = [
    [0,0,0,0,0,0,0,0,0,0,1],
    [0,0,1,0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,1,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,1,1,0],
    [0,1,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0]
]

start = 5
total_nodes = 11
dfs_wrapper(matrix, start, total_nodes)
