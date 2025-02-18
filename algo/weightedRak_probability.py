import random
from collections import Counter

# RAKアルゴリズム（重みを考慮したラベル伝播、確率に基づく選択）
def rak_algorithm_probability(G):
    # ノードごとの初期ラベル設定
    labels = {node: node for node in G.nodes()}
    
    iteration = 0
    while iteration < 100:  # 最大100回の反復
        iteration += 1
        updated = False
        nodes = list(G.nodes())
        random.shuffle(nodes)  # ノードのランダムシャッフル
        
        for node in nodes:
            # 隣接ノードのラベルと重みを取得
            weighted_labels = Counter()
            total_weight = 0.0
            for neighbor in G.neighbors(node):
                weight = G[node][neighbor].get('weight', 1.0)  # 重み（デフォルトは1.0）
                weighted_labels[labels[neighbor]] += weight
                total_weight += weight
            
            # 隣接ノードがいない場合はスキップ
            if total_weight == 0:
                continue
            
            # 重みを確率として正規化
            for label in weighted_labels:
                weighted_labels[label] /= total_weight
            
            # 確率に基づいてラベルを選択
            random_value = random.random()
            cumulative_probability = 0.0
            selected_label = None
            for label, probability in weighted_labels.items():
                cumulative_probability += probability
                if random_value < cumulative_probability:
                    selected_label = label
                    break
            
            # ラベルの更新
            if selected_label and labels[node] != selected_label:
                labels[node] = selected_label
                updated = True
        
        # 更新がなければ終了
        if not updated:
            print(f"RAK Algorythm Iteration: {iteration}")
            print("Converged. Stopping...")
            break
    
    return labels
