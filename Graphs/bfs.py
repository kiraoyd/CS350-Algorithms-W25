def bfs_matrix(graph, start_node, total_nodes):
    visited = [False] * total_nodes
    queue = []
    node_traversal_order = [] #tracks the order we visit the nodes

    visited[start_node] = True
    queue.append(start_node)
    node_traversal_order.append(start_node)

    while queue:
        current_node = queue.pop(0)

        neighbor = 0
        while neighbor < total_nodes:
            if graph[current_node][neighbor] == 1 and visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True
                node_traversal_order.append(neighbor)
            neighbor += 1

    return node_traversal_order

#MAIN CALLING ROUTINE
adjacency_matrix = [
    [0,0,0,0,0,1],
    [0,0,1,1,0,0],
    [0,1,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [1,0,0,1,1,0]
]

order_visited = bfs_matrix(adjacency_matrix, 2, 6)
print(order_visited)


