import os
import fnmatch
import pandas as pd
import matplotlib.pyplot as plt

network_directory_name = "mammalia-dolphin-florida-overall.edges"
graph_name = network_directory_name.removesuffix(".edges")

# データセットフォルダのパス
data_folder = f"./output/modularity/{network_directory_name}"

# グラフの準備（サイズ変更：論文向けサイズ設定）
plt.figure(figsize=(6, 4))  # 単列用（1カラム）の標準サイズ

# フォルダ内のすべての.csvファイルを探索
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(data_folder, filename)        
        print(f"Processing file: {filepath}")
        
        df = pd.read_csv(filepath)

        # コミュニティの数を値ごとの出現回数をカウント
        community_counts = df["Community Count"].value_counts().sort_index()
        
        # グラフのラベル名をXXX.csvから.csvを除去して作成
        graph_label = filename.removesuffix(".csv")

        # ヒストグラムのプロット
        plt.plot(community_counts.index, community_counts.values, marker='o', linestyle='-', label=graph_label)

# グラフの設定
plt.ylim(0, 100)
plt.xlabel("Community")
plt.ylabel("Count")
plt.legend()
plt.grid()

# グラフを保存
plt.savefig(f"./output/histogram/community/{graph_name}.png", format="png", dpi=300, bbox_inches="tight")
