import os
import fnmatch
import pandas as pd
import matplotlib.pyplot as plt

network_directories_name = ["aves-barn-swallow-contact-network.edges", "bio-DM-LC.edges", "les_miserables.edges", "mammalia-dolphin-florida-overall.edges"]

for network_directory_name in network_directories_name:
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
        
            # 統計量を計算
            mean_modularity = df["Modularity"].mean()
            max_modularity = df["Modularity"].max()
            min_modularity = df["Modularity"].min()
        
            # モジュラリティの平均値に最も近いモジュラリティのイテレーションを求める
            iteration = df.iloc[(df["Modularity"] - mean_modularity).abs().argmin()]["Iteration"]
        
            # 結果の表示
            print(f"モジュラリティの平均値: {mean_modularity}")
            print(f"モジュラリティの最大値: {max_modularity}")
            print(f"モジュラリティの最小値: {min_modularity}")
            print(f"平均値に最も近いモジュラリティのイテレーション: {iteration}") 
        
            # モジュラリティの値ごとの出現回数をカウント
            modularity_counts = df["Modularity"].value_counts().sort_index()
        
            # グラフのラベル名をXXX.csvから.csvを除去して作成
            graph_label = filename.removesuffix(".csv")

            # ヒストグラムのプロット
            plt.plot(modularity_counts.index, modularity_counts.values, marker='o', linestyle='-', label=graph_label)

    # グラフの設定
    plt.xlim(-1, 1)
    plt.ylim(0, 100)
    plt.xlabel("Modularity")
    plt.ylabel("Count")
    plt.legend()
    plt.grid()

    # グラフを保存
    plt.savefig(f"./output/analyze/modularity/{graph_name}.png", format="png", dpi=300, bbox_inches="tight")
    
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
    plt.savefig(f"./output/analyze/community/{graph_name}.png", format="png", dpi=300, bbox_inches="tight")

