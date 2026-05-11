def get_mst_and_cost(adj_matrix):
    n = len(adj_matrix)
    if n <= 1:
        return 0, []

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] > 0:
                edges.append((adj_matrix[i][j], i, j))
                
    edges.sort()
    parent = list(range(n))
    
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
        
    def unite(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    min_cost = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if unite(u, v):
            min_cost += weight
            mst_edges.append((u, v))
            if len(mst_edges) == n - 1:
                break
                
    return min_cost, mst_edges