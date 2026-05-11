import matplotlib.pyplot as plt
import networkx as nx

from lab7 import get_mst_and_cost

matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

cost, mst_edges = get_mst_and_cost(matrix)


G = nx.Graph()
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        if matrix[i][j] > 0:
            G.add_edge(i, j, weight=matrix[i][j])

pos = nx.spring_layout(G, seed=42) 

plt.figure(figsize=(10, 7))

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800, edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

all_edges = G.edges()
nx.draw_networkx_edges(G, pos, edgelist=all_edges, edge_color='lightgray', style='dashed', width=1.5)

nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=4)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, label_pos=0.5)

plt.title(f"План інтернетизації Венеції\nЗагальна довжина кабелів: {cost} км", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

plt.show()