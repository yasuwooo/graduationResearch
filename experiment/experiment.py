from algo.weightedRak_labelNum import rak_algorithm_nomal
from algo.weightedRak_probability import rak_algorithm_probability
from algo.weightedRak_weighted import rak_algorithm_weighted
from measure.modularity import calculate_modularity
from tool.communityOutput import output

def experiment(graph, filename, mode):
  for iteration in range(100):
            print(f"Iteration: {iteration}")
            # RAKアルゴリズムの適用
            if(mode == "nomal"):
              labels = rak_algorithm_nomal(graph)
            elif (mode == "probability"):
              labels = rak_algorithm_probability(graph)
            elif (mode == "weighted"):
              labels = rak_algorithm_weighted(graph)
            # print(f"RAK Labels: {labels}")

            # モジュラリティの計算
            modularity = calculate_modularity(graph, labels, f"./output/modularity/{filename}/{mode}.csv", iteration)
            print(f"Modularity: {modularity}")

            # 結果の描画，保存
            output(graph, labels, f"./output/image/{filename}/{mode}/{iteration}.png")