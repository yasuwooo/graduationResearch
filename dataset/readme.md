# データセットの名前と種類をここに示す

## mammalia-dolphin-florida-overall.edges

### 説明

- 概略 動物ネットワーク
- 頂点タイプ 動物、哺乳類、イルカ
- エッジタイプ 交流
- 形式 無指向性
- エッジの重み 加重
- 種 ツルシオプス・トランカトゥス
- 分類群,クラス 哺乳類
- 人口 放し飼いの
- 地理的位置 アメリカ合衆国フロリダ州シーダーキー
- データ収集 調査スキャン
- インタラクションタイプ 空間的近接性
- 相互作用の定義 獲物の捕獲、または長時間の潜水や浮上間の方向転換を伴う特殊な摂食行動によって示される獲物の持続的な探索行為によって特徴付けられる相互作用。
- エッジウェイトタイプ 頻度
- データ収集期間 124 日
- 時間範囲（1 日以内） 5 分
- 説明 4 つのネットワーク: 行動を考慮しない全体的なネットワークと、それぞれの行動に対応する社会化ネットワーク、移動ネットワーク、採餌ネットワーク。
- 引用 ガズダ、ステファニー、他「フロリダ州シーダーキーのバンドウイルカ（Tursiops truncatus）の活動タイプ別にネットワークを描写することの重要性」王立協会オープンサイエンス 2.3（2015）：140263。

### 謝辞と引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```

---

## aves-barn-swallow-contact-network.edges

### 説明

- 概略 動物ネットワーク
- 頂点タイプ 動物、鳥、ツバメ
- エッジタイプ 交流
- 形式 無指向性
- エッジの重み 加重
- 種 ツバメ
- 分類群, クラス 鳥類
- 人口 放し飼いの
- 地理的位置 米国コロラド州ボルダー郡
- データ収集 ロガー
- インタラクションタイプ 身体接触
- 相互作用の定義 0.1m 以内の相互作用
- エッジウェイトタイプ 頻度
- データ収集期間 11 日間
- 時間解決（1 日以内） 1 秒
- 時間範囲（1 日以内） 6 時間
- 説明 2 つのネットワークは、2 つの空間的近接性（身体接触相互作用とその他の空間的近接相互作用）における相互作用の数によって重み付けされたエッジで構築されました。
- 引用 Levin, Iris I.、他「ストレス反応、腸内微生物多様性、性的シグナルは社会的相互作用と相関している。」Biology Letters 12.6 (2016): 20160352。

### 謝辞, 引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```

---

## power-1138-bus.mtx

### 注意

このファイルの拡張子は.mtx なので疎行列
対角線成分をカットするか，何かしらの変形，処理をしなくてはいけない

#### 追記

- .edge 拡張子に変換した
- 拡張子を変換する際，自己ループを意味する対角線を削除した

### 説明

[サイト](https://math.nist.gov/MatrixMarket/data/Harwell-Boeing/psadmit/1138_bus.html)

### 謝辞，引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```

---

## rec-amazon.ratings.edges

### 注意

二部グラフです!!
タイムスタンプがあるからそれを削除しなくてはいけない

### 説明

- 概略 ユーザーによる製品評価
- 頂点タイプ ユーザー、製品
- エッジタイプ 評価
- 形式 二分法
- エッジの重み 加重
- メタデータ 不完全、時間
- 説明 3 列目は評価 (エッジの重み) を表し、4 列目はその評価のエッジのタイムスタンプを表します。

### 謝辞と引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```

---

## rec-epinions.edges

### 説明

- 概略 Epinions の信頼
- 頂点タイプ ユーザー
- エッジタイプ 信頼

### 謝辞と引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```

---

## rec-movielens.edges

### 説明

- 概略 ユーザーによる映画の評価
- 頂点タイプ ユーザー、映画
- エッジタイプ 評価
- 形式 二分法
- エッジの重み 加重
- 説明 3 番目の列は評価 (エッジの重み) を表します。

### 謝辞と引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```

---

## bio-DM-LC.edges

### 説明

- ソース WormNet。http: //www.inetbio.org/wormnet/ を参照。
- 短い 遺伝子機能の関連性
- 頂点タイプ 遺伝子
- エッジタイプ ライン
- 形式 無指向性
- エッジの重み 加重
- 説明 WormNet: 修正ベイズ積分によってすべてのデータ タイプ固有のネットワーク (CE-CX、CE-GN、CE-GT、CE-HT、CE-LC、CE-PG、DM-CX、DM-HT、DM-LC、DR-CX、HS-CX、HS-HT、HS-LC、SC-CC、SC-CX、SC-HT、SC-LC、SC-TS) を統合したネットワーク。

### 謝辞と引用

> ```
> @inproceedings{nr,
>   title={The Network Data Repository with Interactive Graph Analytics and Visualization},
>   author={Ryan A. Rossi and Nesreen K. Ahmed},
>   booktitle={AAAI},
>   url={https://networkrepository.com},
>   year={2015}
> }
> ```
