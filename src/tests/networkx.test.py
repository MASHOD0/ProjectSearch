import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()

G.add_node("A")
G.add_node("B")

G.add_edge("A", "B")
G.add_node("C")
G.add_edge("B", "C")

nx.draw(G, with_labels=True)
plt.show()