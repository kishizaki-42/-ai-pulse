# AI Pulse

AI 業界のニュースを自動収集するエージェント

## プロジェクト概要

Claude Agent SDK の技術検証を目的とした単一エージェントシステム。毎朝 AI 業界のニュースを自動収集・分析する。

## 基本ルール

- すべての出力は日本語
- 記事 ID: `YYYYMMDD-NNN` 形式
- 重複回避: `data/current.json` の既存 URL をスキップ

## 分類ルール

詳細は @.claude/skills/news-collector/references/classification.md を参照
