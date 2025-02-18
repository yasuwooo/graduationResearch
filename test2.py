import networkx as nx
from algo.weightedRak_weighted import rak_algorithm_weighted
from tool.communityOutput import output

# ファイルを読み込む
file_path = "dataset/aves-barn-swallow-contact-network.edges"

# 空のグラフを作成
G = nx.Graph()

# ファイルを読み込みながらエッジを追加
with open(file_path, 'r') as f:
    for line in f:
        source, target, weight = line.strip().split()
        G.add_edge(int(source), int(target), weight=float(weight))  # エッジの重みを設定

# グラフ情報を確認
print(f"ノード数: {G.number_of_nodes()}")
print(f"エッジ数: {G.number_of_edges()}")

# 重み付きエッジの表示
print("エッジ（重み付き）:")
for u, v, data in G.edges(data=True):
    print(f"{u} -- {v} [weight={data['weight']}]")

# RAKアルゴリズムの適用
labels = rak_algorithm_weighted(G)
print("Labels:", labels)

output(G, labels)
