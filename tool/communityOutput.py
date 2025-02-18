import networkx as nx
import matplotlib.pyplot as plt
import os


# コミュニティごとにノードの色分け
def output(G, labels, output_file):
    unique_labels = set(labels.values())
    color_map = {label: idx for idx, label in enumerate(unique_labels)}
    node_colors = [color_map[labels[node]] for node in G.nodes()]

    # 結果の描画
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)  # レイアウトの設定
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        cmap=plt.cm.jet,
        edge_color='gray',
        node_size=500,
        font_size=10,
    )
    plt.title("Network Visualization")
    
    # 出力ファイルのディレクトリを作成（存在しない場合のみ）
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)
    
    
    # 保存と表示
    # 保存して閉じる
    plt.savefig(output_file, format='png')
    print(f"Network visualization saved to {output_file}")
    plt.close()  # 表示を閉じる
