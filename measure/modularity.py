import itertools
import csv
import os

def modularity(graph, labels_dict):
    """
    重み付きグラフのモジュラリティを計算する関数。
    Parameters:
    - graph (networkx.Graph): 重み付きネットワーク
    - labels_dict (dict): ノードをキー、所属コミュニティを値とする辞書
    Returns:
    - float: モジュラリティ Q の値
    """
    # 総エッジ重みの半分（自己ループを除外）
    m = sum(data['weight'] for u, v, data in graph.edges(data=True) if u != v) / 2

    # 各ノードの重み付き次数（事前計算してキャッシュ）
    node_strength = {node: sum(data['weight'] for _, _, data in graph.edges(node, data=True) if node != _) for node in graph.nodes()}

    # モジュラリティの計算
    Q = 0.0

    # すべてのノードペアを考慮（ただし、各ペアを 1 回のみカウント）
    for u, v in itertools.combinations(graph.nodes(), 2):  # (u, v) の全ペア
        if labels_dict[u] == labels_dict[v]:  # 同じコミュニティなら計算
            A_uv = graph[u][v]['weight'] if graph.has_edge(u, v) else 0.0
            k_u = node_strength[u]
            k_v = node_strength[v]
            Q += (A_uv - (k_u * k_v) / (2 * m))

    Q /= (2 * m)  # 正規化（無向グラフなので分母は 2m）
    return Q

def calculate_modularity(graph, labels_dict, output_file, iteration):
    """
    モジュラリティとコミュニティ数を計算し、CSVファイルに書き込む関数。
    """
    # 出力ファイルのディレクトリを作成（存在しない場合のみ）
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)
    
    # コミュニティの数を計算
    unique_labels = set(labels_dict.values())
    num_communities = len(unique_labels)

    # CSVファイルに結果を追記
    # ファイルが存在しない場合はヘッダーを追加
    write_header = not os.path.exists(output_file)
    with open(output_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Iteration", "Modularity", "Community Count"])
        Q = modularity(graph, labels_dict)
        writer.writerow([iteration, Q, num_communities])
    
    return Q
