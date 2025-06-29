# 競馬データ分析プロジェクト

## 概要

このプロジェクトは競馬のデータベースから取得したデータを機械学習を用いて分析し、的中率および回収率の高い馬券戦略を導くことを目的としています。

## 機能

### Must-have Condition（必須機能）

1. **データ取得**
   - PostgreSQLデータベースからレース情報、馬ごとレース情報、前走ID情報を取得
   - 2019年～2024年のデータを対象

2. **特徴量データ作成**
   - レース情報と馬の情報を組み合わせた特徴量データを作成
   - 前走情報を含む複雑な特徴量構造
   - 欠損データの補完と固定長データの作成

3. **学習データと検証データへの分割**
   - race_id単位でランダムに80%学習データ、20%検証データに分割

4. **機械学習（Transformer）**
   - Transformerアーキテクチャによる勝率予測モデル
   - Positional Encodingによる時系列情報の反映
   - 各出走馬の1着確率を予測

5. **検証と結果の表示・出力**
   - 予測精度の計算と表示
   - 予測勝率と実際の着順の相関分析
   - 結果のCSVファイル出力

## 技術スタック

- **プログラミング言語**: Python 3.8+
- **データベース**: PostgreSQL 17
- **ORM**: SQLAlchemy
- **機械学習**: TensorFlow/Keras
- **データ処理**: pandas, numpy
- **テスト**: pytest

## プロジェクト構造

```
testPJ2/
├── data/                   # 出力データファイル
├── db/                     # データベース関連
│   ├── connector.py        # DB接続（変更不可）
│   ├── get_race_data.sql   # レース情報取得SQL（変更不可）
│   ├── get_umagoto_race.sql # 馬ごとレース情報取得SQL（変更不可）
│   ├── get_zensou_id.sql   # 前走ID情報取得SQL（変更不可）
│   └── schema.sql          # データベーススキーマ（変更不可）
├── logs/                   # ログファイル
├── models/                 # 機械学習モデル
├── prompt/                 # プロンプト記録
│   └── prompt.txt
├── src/                    # ソースコード
│   ├── domain/             # ドメイン層
│   │   ├── entities.py     # エンティティ
│   │   ├── repositories.py # リポジトリインターフェース
│   │   └── services.py     # ドメインサービス
│   ├── application/        # アプリケーション層
│   │   ├── services.py     # アプリケーションサービス
│   │   └── usecases.py     # ユースケース
│   └── infrastructure/     # インフラストラクチャ層
│       ├── database.py     # データベースアクセス
│       ├── storage.py      # ストレージ
│       └── dependency_injection.py # 依存性注入
├── tests/                  # テスト
│   ├── test_entities.py    # エンティティテスト
│   └── test_services.py    # サービステスト
├── visualization/          # 可視化（将来拡張）
├── main.py                 # メイン実行ファイル
├── requirements.txt        # 依存関係
└── README.md              # このファイル
```

## アーキテクチャ

このプロジェクトはクリーンアーキテクチャ（レイヤードアーキテクチャ）を採用しています：

- **ドメイン層**: ビジネスロジックとエンティティ
- **アプリケーション層**: ユースケースとアプリケーションサービス
- **インフラストラクチャ層**: データアクセスと外部サービス連携

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. データベース設定

PostgreSQLデータベースに接続し、`db/schema.sql`を実行してテーブルを作成してください。

### 3. 環境変数の設定

データベース接続情報を設定してください（`db/connector.py`を参照）。

## 実行方法

### メイン実行

```bash
python main.py
```

### テスト実行

```bash
pytest tests/ -v
```

## データ仕様

### レース情報
- `race_id`: レースを一意に識別するID
- `keibajo_code`: 競馬場コード（01～10がJRA）
- `track_code`: トラックコード（01～29）
- `kyori`: 距離
- `babacd`: 馬場状態コード（1:良、2:やや重、3:重、4:不良）
- `tosu`: 出走頭数（最大18頭）
- `grade_code`: 重賞コード（1～5、1が最高グレード）
- `mu`: レースレーティング

### 馬ごとレース情報
- `horse_id`: 馬のID
- `umaban`: 馬番号
- `odds`: 単勝オッズ
- `ninki`: 人気順
- `race_order`: 着順
- その他多数の特徴量

### 前走ID情報
- `pre1_race_id`～`pre5_race_id`: 前走～5走前のレースID

## 機械学習モデル

### Transformerアーキテクチャ
- Multi-Head Attention
- Positional Encoding
- Feed Forward Network
- Layer Normalization

### 学習目標
- 各出走馬の1着確率を予測
- 実際の1着馬の確率が高くなるように学習

## 出力結果

### CSVファイル
- `data/prediction_results.csv`: 予測結果
  - `race_id`: レースID
  - `horse_id`: 馬ID
  - `predicted_win_probability`: 予測勝率
  - `actual_race_order`: 実際の着順
  - `odds`: オッズ
  - `predicted_rank`: 予測順位

### 評価指標
- 予測精度（1着予測の正解率）
- 予測勝率と実際の着順の相関
- 予測順位と実際の着順の順位相関

## 開発ガイドライン

### コーディング規約
- PEP 8準拠
- 型ヒントの使用
- Sphinx形式のDocstring
- snake_case（変数・関数）、PascalCase（クラス）

### テスト戦略
- pytestによる単体テスト
- モックを使用した外部依存の排除
- C0/C1カバレッジ100%目標

## 注意事項

- `db/`フォルダ内のファイルは絶対に変更しないでください
- データベース接続情報は適切に管理してください
- 大量データの処理時はメモリ使用量に注意してください

## ライセンス

このプロジェクトは個人利用を目的としています。

## 更新履歴

- 2024年12月19日: 初回リリース（Must-have Condition実装） 