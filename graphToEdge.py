import networkx as nx

# les_miserablesグラフを取得
def lesMiserables():
    return nx.les_miserables_graph()

# .edge形式でグラフを書き出す
def write_graph_to_edge_file(graph, file_path):
    with open(file_path, 'w') as f:
        for u, v, data in graph.edges(data=True):
            weight = data.get('weight', 1)  # 重みを取得（デフォルトは1）
            f.write(f"{u} {v} {weight}\n")

# メイン処理
if __name__ == "__main__":
    # グラフを取得
    graph = lesMiserables()

    # ノード、エッジ、重みを.edge形式で保存
    output_file = "dataset/les_miserables.edges"
    write_graph_to_edge_file(graph, output_file)

    print(f"グラフデータが {output_file} に保存されました。")
