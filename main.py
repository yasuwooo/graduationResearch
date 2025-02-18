import os
import networkx as nx
import fnmatch
from experiment.experiment import experiment

def read_edge_file(filepath):
    """指定された.edgeファイルを読み込み、グラフを作成"""
    G = nx.Graph()
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                node1, node2, weight = parts
                if node1 != node2:
                    G.add_edge(node1, node2, weight=float(weight))
            else:
                print(f"Invalid line format in {filepath}: {line.strip()}")
    return G

# データセットフォルダのパス
data_folder = "./dataset"

# フォルダ内のすべての.edgeファイルを探索
for filename in os.listdir(data_folder):
    if filename.endswith(".edges"):
        filepath = os.path.join(data_folder, filename)
        
        if fnmatch.fnmatch(filename, 'rec*'):  # 'rec'で始まるファイル名をマッチ
            print(f"Skipping file: {filename}")
            continue  # スキップ
        if fnmatch.fnmatch(filename, "power*"):
            print(f"Skipping file: {filename}")
            continue
        
        print(f"Processing file: {filename}")

        # グラフを読み込む
        graph = read_edge_file(filepath)
        # print(f"Nodes: {graph.nodes()}")
        # print(f"Edges: {graph.edges(data=True)}")
        
        experiment(graph, filename, "nomal")
        experiment(graph, filename, "probability")
        experiment(graph, filename, "weighted")

        


