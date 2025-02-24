Discord AI Bot 設置與使用說明
============================

# 1. 至Discord developers創建Bot
https://discord.com/developers/docs/reference

# 2. 環境設定步驟
--------------
## 2.1 建立虛擬環境

    # 進入專案目錄
    cd path/to/project_root

    # 建立虛擬環境
    python -m venv venv

    # 啟動虛擬環境
    # Windows:
    venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate

## 2.2 安裝依賴套件

    # pip install -r requirements.txt

## 2.3 設定環境變數

    建立 .env 檔案並填入以下內容：
    
    # Discord Bot Token (必填)
    DISCORD_TOKEN=你的Discord_Bot_Token

    # Claude API Key (選填)
    CLAUDE_API_KEY=你的Claude_API_Key

    # Gemini API Key (選填)
    GEMINI_API_KEY=你的Gemini_API_Key

    # Deepseek API Key (選填)
    DEEPSEEK_API_KEY=你的Deepseek_API_Key


# 3. 啟動流程
----------
## 3.1 完整的 CMD 指令

    # 1. 進入專案目錄
    cd path/to/project_root

    # 2. 啟動虛擬環境
    venv\Scripts\activate

    # 3. 啟動 Bot
    python -m discord_ai_bot.main


# 4. Bot 指令說明
-------------
- !bumi [訊息] - 與 AI 對話
- !switch [模型名稱] - 切換 AI 模型
  可用模型：claude, gemini, deepseek
- !clear - 清除對話歷史
- !status - 顯示目前狀態


# 5. 注意事項
----------
## 5.1 API Keys 設定：
    - Discord Bot Token 必須填寫
    - 其他 AI 模型的 API Key 至少需要一個
    - 所有 API Keys 都需要在 .env 檔案中設定

## 5.2 模型使用：
    - 預設使用 deepseek 模型
    - 可以使用 !switch 指令切換模型
    - 每個頻道都有獨立的對話歷史

## 5.3 環境要求：
    - Python 3.8 或以上版本
    - 需要穩定的網路連接
    - 確保所有依賴套件都正確安裝

## 5.4 常見問題處理：
    - 如果 Bot 無法啟動，檢查 Token 是否正確
    - 如果模型無法使用，確認對應的 API Key 是否有效
    - 如果出現權限錯誤，檢查 Bot 在 Discord 中的權限設定


# 6. 快速啟動範例
-------------
假設專案位於 C:\User\DiscordBot\project_root

## 1. 開啟 CMD 並進入專案目錄
F:
cd C:\User\DiscordBot\project_root

## 2. 啟動虛擬環境
venv\Scripts\activate

## 3. 啟動 Bot
python -m discord_ai_bot.main 
