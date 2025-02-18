from scipy.io import mmread

# MTXファイルを読み込む
mtx_file = "dataset/power-1138-bus.mtx"
output_file = "dataset/power-1138-bus.edges"

# MTX形式の読み込み
matrix = mmread(mtx_file)

# エッジリストを生成 (非ゼロ要素をエッジとして扱う)
with open(output_file, 'w') as f:
    for i, j, v in zip(matrix.row, matrix.col, matrix.data):
        # ノードは1始まりで書き出す場合に+1
        # 対角線の場合，無視する
        if i != j :
          f.write(f"{i + 1} {j + 1} {v}\n")

print(f"EDGES形式のファイルが {output_file} として保存されました。")
