def dfs_iter_matrix(graph, start_node, total_nodes):
    visited = [False] * total_nodes
    stack = []
    node_traversal_order = []

    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        if visited[current_node] == False:
            visited[current_node] = True
            node_traversal_order.append(current_node)
            neighbor = 0
            while neighbor < total_nodes:
                if graph[current_node][neighbor] == 1 and visited[neighbor] == False:
                    stack.append(neighbor)
                neighbor += 1

    return node_traversal_order




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
order_visited = dfs_iter_matrix(matrix, start, total_nodes)
print(order_visited)