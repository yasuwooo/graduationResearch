# rec-amazon-ratings.edgesがcsv形式であったため、エッジリスト(edge)形式に変換する

inputFilePath = "dataset/rec-amazon-ratings.edges"
outputFilePath = "dataset/rec-amazon-ratings-copy.edges"

# 読み込みファイルを開く
with open(inputFilePath, 'r') as inputFile:
  # 書き込みファイルを開く
  with open(outputFilePath, 'w') as  outputFile:
    for line in inputFile:
      source, target, weight, time = line.strip().split(",")
      # 時間の情報は使わないので，削除する
      outputFile.write(f"{source} {target} {weight}\n")
  print(f"{inputFilePath}ファイルが EDGE形式で{outputFilePath} として保存されました。")
