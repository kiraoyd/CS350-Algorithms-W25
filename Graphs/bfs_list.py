def bfs_list(graph_list, start_node, total_nodes):
    visited = [False] * total_nodes
    queue = []
    node_traversal_order = [] #tracks the order we visit the nodes

    queue.append(start_node)
    visited[start_node] = True
    node_traversal_order.append(start_node)

    while queue:
        current_node = queue.pop(0)
        neighbors = graph_list[current_node]
        index = 0
        while index < len(neighbors):
            neighbor = neighbors[index]
            if visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True
                node_traversal_order.append(neighbor)

            index += 1

    return node_traversal_order


#----MAIN CALLING ROUTINE----#
adjacency = {
    0: [5],
    1: [2,3],
    2: [1,3,4],
    3: [1,2,4,5],
    4: [2,3,5],
    5: [0,3,4]
}

number = 6
order_visited = bfs_list(adjacency, 2, number)
print(f"\nThrough BFS run on an adjacency list, we visited all the verticies, where the index value of the list represents the vertex: {order_visited}")
