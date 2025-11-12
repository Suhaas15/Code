from collections import defaultdict, deque

# Step 1: Topological Sort using Kahn's Algorithm
def topological_sort(vertices, adj_list):
    # in_degree keeps track of the number of incoming edges for each vertex
    in_degree = {v: 0 for v in vertices}
    for u in adj_list:
        for v in adj_list[u]:
            in_degree[v] += 1
    
    # Queue to store vertices with in-degree of 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return topo_order

# Step 2: Shortest Path in DAG
def shortest_path_dag(vertices, adj_list, source):
    # Topological sort of the graph
    topo_order = topological_sort(vertices, adj_list)
    
    # Initialize distances with infinity
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0
    
    # Process each vertex in topological order
    for u in topo_order:
        if dist[u] != float('inf'):  # Only process if vertex u has been reached
            for v, weight in adj_list[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    return dist

