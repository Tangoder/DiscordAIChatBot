import discord
from discord.ext import commands
from typing import Dict, Optional
from ..config.config import BotConfig
from ..models.base import BaseAIModel
from ..models.claude import ClaudeAIModel
from ..models.gemini import GeminiAIModel
from ..models.deepseek import DeepseekAIModel

class AIBot(commands.Bot):
    def __init__(self, config: BotConfig):
        intents = discord.Intents.default()
        intents.message_content = True  # 只保留必要的 intent
        intents.guilds = True          # 確保有 guilds intent
        
        super().__init__(command_prefix=config.command_prefix,
                        intents=intents)
        
        self.config = config
        self.chat_histories: Dict[int, list] = {}  # 儲存每個頻道的對話歷史
        self.models: Dict[str, BaseAIModel] = {}
        
        # 調試輸出
        print("Config values:")
        print(f"- claude_api_key: {bool(config.claude_api_key)}")
        print(f"- gemini_api_key: {bool(config.gemini_api_key)}")
        print(f"- deepseek_api_key: {bool(config.deepseek_api_key)}")
        
        # 初始化AI模型
        if config.claude_api_key:
            print("Initializing Claude model...")
            self.models['claude'] = ClaudeAIModel(config.claude_api_key)
        if config.gemini_api_key:
            print("Initializing Gemini model...")
            self.models['gemini'] = GeminiAIModel(config.gemini_api_key)
        if config.deepseek_api_key:
            print("Initializing Deepseek model...")
            try:
                self.models['deepseek'] = DeepseekAIModel(config.deepseek_api_key)
                print("Deepseek model initialized successfully")
            except Exception as e:
                print(f"Error initializing Deepseek model: {str(e)}")
            
        print("Available models:", list(self.models.keys()))
        
        self.current_model = config.default_model
        
        # 註冊指令
        self.add_commands()
        
    def add_commands(self):
        @self.command(name="bumi")
        async def chat(ctx: commands.Context, *, message: str):
            """與AI進行對話"""
            async with ctx.typing():
                try:
                    # 取得當前使用的模型
                    model = self.models.get(self.current_model)
                    if not model:
                        await ctx.send("目前沒有可用的AI模型")
                        return
                    
                    # 取得對話歷史
                    history = self.chat_histories.get(ctx.channel.id, [])
                    
                    # 生成回應
                    response = await model.generate_response(message, history)
                    
                    # 更新對話歷史
                    history.append({"role": "user", "content": message})
                    history.append({"role": "assistant", "content": response})
                    
                    # 限制歷史記錄長度
                    if len(history) > self.config.max_history * 2:
                        history = history[-self.config.max_history * 2:]
                    
                    self.chat_histories[ctx.channel.id] = history
                    
                    await ctx.send(response)
                    
                except Exception as e:
                    await ctx.send(f"發生錯誤: {str(e)}")
        
        @self.command(name="switch")
        async def switch_model(ctx: commands.Context, model_name: str):
            """切換AI模型"""
            if model_name not in self.models:
                await ctx.send(f"找不到模型: {model_name}")
                return
                
            self.current_model = model_name
            await ctx.send(f"已切換至 {model_name} 模型")
        
        @self.command(name="clear")
        async def clear_history(ctx: commands.Context):
            """清除當前頻道的對話歷史"""
            if ctx.channel.id in self.chat_histories:
                del self.chat_histories[ctx.channel.id]
                await ctx.send("已清除對話歷史")
            else:
                await ctx.send("沒有對話歷史可清除")
        
        @self.command(name="status")
        async def show_status(ctx: commands.Context):
            """顯示當前bot狀態"""
            status = f"當前使用模型: {self.current_model}\n"
            status += f"可用模型: {', '.join(self.models.keys())}\n"
            status += f"對話歷史長度: {len(self.chat_histories.get(ctx.channel.id, []))}"
            await ctx.send(status)

    async def on_ready(self):
        print(f'Bot已登入為 {self.user.name}')
        print(f'Bot ID: {self.user.id}')
        print('已加入的伺服器:')
        for guild in self.guilds:
            print(f'- {guild.name} (id: {guild.id})')

    async def on_guild_join(self, guild):
        print(f'加入了新的伺服器: {guild.name} (id: {guild.id})') 