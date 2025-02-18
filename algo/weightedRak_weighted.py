import random
from collections import Counter

# RAKアルゴリズム（非同期的なラベル更新を実現）
# すべてのノードで重みを考慮して考えるとき
# 隣接するノードのラベルの合計が，一番大きいものを選ぶ
# 一番大きいものが複数ある場合，ランダムで決める
def rak_algorithm_weighted(G):
    # ノードごとの初期ラベル設定
    labels = {node: node for node in G.nodes()}
    
    iteration = 0
    while iteration<100: # 100回の反復で終了
        iteration += 1
        updated = False
        nodes = list(G.nodes())
        random.shuffle(nodes)  # ノードのランダムシャッフル
        
        for node in nodes:
            # 隣接ノードのラベルと重みの取得
            weighted_labels = Counter()
            for neighbor in G.neighbors(node):
                weight = G[node][neighbor].get('weight', 1.0)  # 重みを取得（デフォルトは1.0）
                weighted_labels[labels[neighbor]] += weight  # 古いラベルを基に重みを加算
            
            # 重みがない(隣接するノードがない)場合はスキップ
            if not weighted_labels:
                continue

            # 重みの合計が最も大きいラベルを取得
            max_weight = max(weighted_labels.values())
            most_frequent_labels = [label for label, weight in weighted_labels.items() if weight == max_weight]
            most_frequent_label = random.choice(most_frequent_labels)  # 重みの合計が同率の場合はランダム選択
            
            # ラベルが変わった場合に更新
            if labels[node] != most_frequent_label:
                labels[node] = most_frequent_label
                updated = True
        
        # 変化がない場合、アルゴリズムを終了
        if not updated:
            print(f"RAK Algorythm Iteration: {iteration}")
            print("Converged. Stopping...")
            break
    
    return labels
