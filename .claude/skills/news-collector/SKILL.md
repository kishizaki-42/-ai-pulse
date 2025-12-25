---
name: news-collector
description: AI 業界ニュースを収集・分類するスキル。「ニュースを収集して」「AI ニュースを取得して」「最新ニュースを集めて」などのタスクで使用。ホワイトリスト URL を巡回し、記事を分類して JSON 保存する。
---

# AI News Collector

## ワークフロー

1. `config/whitelist.json` からソース URL 一覧を取得
2. `data/current.json` を読み込み、既存記事を取得
3. 各 URL に WebFetch を実行
4. 記事メタデータを抽出（タイトル、URL、公開日時、ソース名）
5. カテゴリ分類・重要度判定（詳細は [classification.md](references/classification.md)）
6. 日本語でサマリー生成（形式は [summary_format.md](references/summary_format.md)）
7. ID 付与（形式: YYYYMMDD-NNN）
8. **既存記事 + 新規記事をマージ**して `data/current.json` に保存

## 重複回避

- `data/current.json` に既存の URL はスキップ
- 重複検出時はログに記録

## エラーハンドリング

- WebFetch 失敗時: Tavily MCP で再試行
- Tavily も失敗: ログ記録してスキップ
- メタデータ抽出失敗: 可能な範囲で抽出

## リソース

- **分類ルール**: [references/classification.md](references/classification.md)
- **サマリー形式**: [references/summary_format.md](references/summary_format.md)
- **出力スキーマ**: [assets/output_schema.json](assets/output_schema.json)
- **検証スクリプト**: `python scripts/validate_output.py`
