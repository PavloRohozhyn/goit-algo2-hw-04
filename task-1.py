import networkx as nx
import pandas as pd

G = nx.DiGraph() # graph

edges = [
    ("Terminal 1", "Sklad 1", 25),
    ("Terminal 1", "Sklad 2", 20),
    ("Terminal 1", "Sklad 3", 15),
    ("Terminal 2", "Sklad 3", 15),
    ("Terminal 2", "Sklad 4", 30),
    ("Terminal 2", "Sklad 2", 10),
    ("Sklad 1", "Magazyn 1", 15),
    ("Sklad 1", "Magazyn 2", 10),
    ("Sklad 1", "Magazyn 3", 20),
    ("Sklad 2", "Magazyn 4", 15),
    ("Sklad 2", "Magazyn 5", 10),
    ("Sklad 2", "Magazyn 6", 25),
    ("Sklad 3", "Magazyn 7", 20),
    ("Sklad 3", "Magazyn 8", 15),
    ("Sklad 3", "Magazyn 9", 10),
    ("Sklad 4", "Magazyn 10", 20),
    ("Sklad 4", "Magazyn 11", 10),
    ("Sklad 4", "Magazyn 12", 15),
    ("Sklad 4", "Magazyn 13", 5),
    ("Sklad 4", "Magazyn 14", 10),
] # edges
G.add_weighted_edges_from(edges, weight="capacity")
G.add_node("Source") # source
G.add_node("Sink") # sink
G.add_edge("Source", "Terminal 1", capacity=float("inf")) # source + terminal1
G.add_edge("Source", "Terminal 2", capacity=float("inf")) # source + terminal2
# store + sink
for i in range(1, 15):
    G.add_edge(f"Magazyn {i}", "Sink", capacity=float("inf"))
#Edmonds-Karp algo
flow_value, flow_dict = nx.maximum_flow(G, "Source", "Sink", flow_func=nx.algorithms.flow.edmonds_karp)
# Result
rows = []
for ter in ["Terminal 1", "Terminal 2"]:
    for sklad in flow_dict[ter]:
        if flow_dict[ter][sklad] > 0:
            #print(ter)
            for mag in flow_dict[sklad]:
                if flow_dict[sklad][mag] > 0:
                    rows.append({
                        "Terminal": ter,
                        "Magazyn": mag,
                        "Actual Flow (units)": flow_dict[sklad][mag]
                    })

df_result = pd.DataFrame(rows)
print(df_result)
print(f"\nMax flow: {flow_value} units") # done
