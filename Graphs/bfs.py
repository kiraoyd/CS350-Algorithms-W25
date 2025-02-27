def bfs_matrix(graph, start_node, total_nodes):
    visited = [False] * total_nodes
    queue = []

    visited[start_node] = True
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)

        neighbor = 0
        while neighbor < total_nodes:
            if graph[current_nodes][neighbor] == 1 and visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True
            neighbor += 1


def bfs_list(graph_list, start_node, total_nodes):
