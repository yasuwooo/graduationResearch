# RAKアルゴリズム(重みなし)
import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# RAKアルゴリズムの実装
# コミュニティの分割数split_numより小さくなったら終了
def rak_algorithm(G):
    # ノードごとの初期ラベル設定
    labels = {node: node for node in G.nodes()}
    
    i=0
    while(True):
        i += 1
        print(f"iter count:{i}\n")
        updated = False
        nodes = list(G.nodes())
        random.shuffle(nodes)  # ノードのランダムシャッフル
        
        for node in nodes:
            neighbor_labels = [labels[neighbor] for neighbor in G.neighbors(node)]
            if not neighbor_labels:
                continue

            # 最頻ラベルを取得
            label_counts = Counter(neighbor_labels)
            max_count = max(label_counts.values())
            most_frequent_labels = [label for label, count in label_counts.items() if count == max_count]
            most_frequent_label = random.choice(most_frequent_labels)            
            
            # ラベルが変わった場合に更新
            if labels[node] != most_frequent_label:
                labels[node] = most_frequent_label
                updated = True
                
        # 変化なしなら辞める
        if not updated:
            print("stable end\n")
            break
    return labels

# サンプルネットワークの作成
# G = nx.barabasi_albert_graph(150, 2) # バラバシ・アルバートモデル
# G = nx.stochastic_block_model([50, 50], [[0.8, 0.05], [0.05, 0.8]])
# G = nx.random_geometric_graph(100, 0.3)
# G = nx.watts_strogatz_graph(100, 6, 0.1)
# G = nx.karate_club_graph()  # 有名な空手クラブのネットワークデータ
G = nx.les_miserables_graph()
labels = rak_algorithm(G)
print(labels)

# コミュニティごとにノードの色分け
unique_labels = set(labels.values())
color_map = {label: idx for idx, label in enumerate(unique_labels)}
node_colors = [color_map[labels[node]] for node in G.nodes()]

# 結果の描画
plt.figure(figsize=(10, 7))
nx.draw(G, with_labels=True, node_color=node_colors, cmap=plt.cm.jet)
plt.title("RAK Algorithm Community Detection")
plt.show()