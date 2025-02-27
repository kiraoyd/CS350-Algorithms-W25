def bfs_list(graph_list, start_node, total_nodes):
    visited = [False] * total_nodes
    queue = []

    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.pop(0)
        neighbors = graph_list[current_node]
        index = 0
        while index < len(neighbors):
            neighbor = neighbors[index]
            if visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True

            index += 1
