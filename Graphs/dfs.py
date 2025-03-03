def dfs_iter_matrix(graph, start_node, total_nodes):
    visited = [False] * total_nodes
    stack = []
    path = []

    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        if visited[current_node] == False:
            visited[current_node] = True
            path.append(current_node)
            neighbor = 0
            while neighbor < total_nodes:
                if graph[current_node][neighbor] == 1 and visited[neighbor] == False:
                    stack.append(neighbor)
                neighbor += 1