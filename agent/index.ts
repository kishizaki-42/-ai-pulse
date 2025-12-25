import { query } from "@anthropic-ai/claude-agent-sdk";

async function runAgent() {
  console.log("🚀 AI Pulse Agent 起動中...");
  const startTime = new Date().toISOString();

  for await (const message of query({
    prompt: "Skill ツールで /news-collector を実行し、実際にニュースを収集してください。config/whitelist.json のURLを巡回し、data/current.json に保存するまで完了してください。",
    options: {
      allowedTools: ["WebFetch", "Read", "Write", "Skill"],
      settingSources: ["project"],
      permissionMode: "acceptEdits",
      cwd: process.cwd(),
      model: "claude-haiku-4-5-20251001",
    },
  })) {
    if (message.type === "assistant" && message.message?.content) {
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log(block.text);
        } else if ("name" in block) {
          console.log(`🔧 Tool: ${block.name}`);
        }
      }
    } else if (message.type === "result") {
      console.log(`✅ 完了: ${message.subtype}`);
    }
  }

  const endTime = new Date().toISOString();
  console.log(`🏁 AI Pulse Agent 終了 (開始: ${startTime}, 終了: ${endTime})`);
}

runAgent().catch((error) => {
  console.error("❌ エラー:", error);
  process.exit(1);
});
