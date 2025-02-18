import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 色のリストを用意
colors = ['blue', 'orange', 'green']

network_directories_name = [
    "aves-barn-swallow-contact-network.edges",
    "bio-DM-LC.edges",
    "les_miserables.edges",
    "mammalia-dolphin-florida-overall.edges"
]

for network_directory_name in network_directories_name:
    graph_name = network_directory_name.removesuffix(".edges")

    # データセットフォルダのパス
    data_folder = f"./output/modularity/{network_directory_name}"

    # **モジュラリティのヒストグラム**
    plt.figure(figsize=(6, 4))
    
    for idx, filename in enumerate(os.listdir(data_folder)):
        if filename.endswith(".csv"):
            filepath = os.path.join(data_folder, filename)
            print(f"Processing file: {filepath}")

            df = pd.read_csv(filepath)
            modularity_values = df["Modularity"].dropna().tolist()

            # ヒストグラムのプロット（ファイルごとに異なる色）
            plt.hist(modularity_values, bins=30, range=(-1, 1), alpha=0.4, color=colors[idx % len(colors)], edgecolor='black', label=filename.removesuffix(".csv"))

    plt.xlabel("Modularity")
    plt.ylabel("Frequency")
    plt.legend()  # 凡例を追加
    plt.grid(True)
    
    # グラフを保存
    plt.savefig(f"./output/histogram/modularity/{graph_name}.png", format="png", dpi=300, bbox_inches="tight")
    plt.close()

    # **コミュニティ数のヒストグラム**
    plt.figure(figsize=(6, 4))
    
    for idx, filename in enumerate(os.listdir(data_folder)):
        if filename.endswith(".csv"):
            filepath = os.path.join(data_folder, filename)
            print(f"Processing file: {filepath}")

            df = pd.read_csv(filepath)
            community_counts = df["Community Count"].dropna().tolist()

            # ヒストグラムのプロット（ファイルごとに異なる色）
            plt.hist(community_counts, bins=30, alpha=0.5, color=colors[idx % len(colors)], edgecolor='black', label=filename.removesuffix(".csv"))

    plt.xlabel("Community Count")
    plt.ylabel("Frequency")
    plt.legend()  # 凡例を追加
    plt.grid(True)
    
    # グラフを保存
    plt.savefig(f"./output/histogram/community/{graph_name}.png", format="png", dpi=300, bbox_inches="tight")
    plt.close()
