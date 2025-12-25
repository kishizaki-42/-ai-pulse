# 分類ルール

## カテゴリ判定

| カテゴリ | 判定条件 | キーワード例 |
|----------|----------|-------------|
| Model | LLM、基盤モデル、学習手法、モデルアーキテクチャ、ベンチマーク結果 | GPT, Claude, Gemini, LLaMA, transformer, training, fine-tuning, RLHF, benchmark |
| Service | API、SDK、製品、サービス、料金、機能追加 | API, SDK, pricing, release, launch, feature, integration, developer |
| Other | 上記以外 | partnership, hiring, event, policy, regulation, funding |

### 判定の優先順位

1. タイトルに Model キーワードが含まれる → Model
2. タイトルに Service キーワードが含まれる → Service
3. 本文の主題で判断
4. 不明な場合 → Other

## 重要度判定

| 重要度 | 判定条件 |
|--------|----------|
| high | 新モデル発表、メジャーバージョンリリース、大型買収（10億ドル超）、業界初の技術発表 |
| normal | 上記以外すべて |

### high の具体例

- 「GPT-5 発表」「Claude 4 リリース」
- 「OpenAI、$10B の資金調達」
- 「Google、新アーキテクチャを発表」
- 「Anthropic、Constitutional AI 2.0 を公開」

### normal の具体例

- API 価格改定
- マイナーバージョンアップ
- パートナーシップ発表
- イベント告知
