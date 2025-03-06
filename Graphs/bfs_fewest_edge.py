def bfs_fe_matrix(graph, start_node, target_node, total_nodes):

    if target_node > total_nodes or start_node > total_nodes:
        return -1 #error flag, nodes requested out of bounds of matrix

    visited = [False] * total_nodes
    queue = []

    visited[start_node] = True
    queue.append(start_node)

    found_target = False
    level = 0 #just the start node

    #continue BFS traversal as long as the target has not been reached
    while queue and not found_target:
        nodes_in_level = len(queue) #if we only pop nodes one level at a time, the queue will only ever contain nodes for one level

        #loop only through the nodes at a single level, and only until target found
        count = 0
        while count < nodes_in_level and not found_target:
            #normal BFS processing....
            current_node = queue.pop(0)
            neighbor = 0
            #process all neighbors of current node, or process until target found
            while neighbor < total_nodes and not found_target:
                if graph[current_node][neighbor] == 1 and visited[neighbor] == False:
                    queue.append(neighbor)
                    #was this neighbor our target?
                    if neighbor == target_node:
                        found_target = True #terminate all loops, process ends
                    visited[neighbor] = True
                neighbor += 1

            count += 1

        level += 1

    if found_target:
        return level
    else:
        return -2 #error flag, target not in graph

#MAIN CALLING ROUTINE
adjacency_matrix = [
    [0,1,1,1,0,0],
    [1,0,1,0,0,0],
    [1,1,0,1,1,0],
    [1,0,1,0,0,0],
    [0,0,1,0,0,1],
    [0,0,0,0,1,0]
]

levels = bfs_fe_matrix(adjacency_matrix, 0, 5,6)
print(levels)

