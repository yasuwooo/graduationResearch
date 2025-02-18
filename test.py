import osmnx as ox
import networkx as nx
from algo.weightedRak_weighted import rak_algorithm_weighted

# Hamamatsu, Japan の道路ネットワークを取得
G = ox.graph_from_place("Hamamatsu, Japan", network_type="drive")

# グラフを無向グラフに変換（必要に応じて）
G_undirected = nx.Graph()

for u, v, data in G.edges(data=True):
    # エッジの長さ（距離）を重みとして使用
    weight = data.get("length", 1)  # デフォルトで1を設定
    if G_undirected.has_edge(u, v):
        # 既存のエッジがある場合、重みを最小値に設定
        G_undirected[u][v]["weight"] = min(G_undirected[u][v]["weight"], weight)
    else:
        G_undirected.add_edge(u, v, weight=weight)

# ノードとエッジの確認
print("Nodes:", G_undirected.nodes())
print("Edges with weights:", list(G_undirected.edges(data=True)))

# RAKアルゴリズムの適用
labels = rak_algorithm_weighted(G_undirected)
print("Labels:", labels)
