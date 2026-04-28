import heapq

def solve_gamsrv_with_capacity(n, m, clients, edges, capacities):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    def dijkstra(start_node):
        distances = [float('inf')] * (n + 1)
        distances[start_node] = 0
        pq = [(0, start_node)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > distances[u]: continue
            for v, weight in adj[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
        return distances

    min_max_latency = float('inf')
    num_clients = len(clients)
    client_set = set(clients)
    
    possible_servers = [
        i for i in range(1, n + 1) 
        if i not in client_set and capacities.get(i, 0) >= num_clients
    ]
    
    if not possible_servers:
        return -1

    for server in possible_servers:
        distances = dijkstra(server)
        current_max = max(distances[c] for c in clients)
        min_max_latency = min(min_max_latency, current_max)
        
    return min_max_latency