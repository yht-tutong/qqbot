import botpy
from botpy import Client
from botpy.types.message import Message
from botpy.types.guild import GuildPayload, GuildMembers
from botpy.types.channel import ChannelPayload
from botpy.types.reaction import Reaction
from .config import get_config
from .logger import get_logger
from .api.client import APIClient
from .handlers.message_handler import MessageHandler
from .handlers.guild_handler import GuildHandler
from .handlers.member_handler import MemberHandler
from .handlers.reaction_handler import ReactionHandler
import time

class QQBot(Client):
    """QQ机器人主类"""
    
    def __init__(self, config):
        """初始化机器人
        
        Args:
            config: 机器人配置
        """
        # 初始化事件订阅
        # 对于public类型的机器人，只订阅基本的公域消息事件
        intents = botpy.Intents(
            public_guild_messages=True,   # 公域消息事件
            guilds=True,                  # 频道事件
            guild_message_reactions=True,  # 消息相关互动事件
            direct_message=True,          # 私信事件
            interaction=True,             # 互动事件
            message_audit=True,           # 消息审核事件
            public_messages=True,         # 公域群/C2C消息事件
            audio_action=True             # 音频事件
        )
        
        super().__init__(intents=intents)
        
        # 配置
        self.config = config
        self.appid = config.get('appid')
        self.token = config.get('token')
        self.secret = config.get('secret')
        self.type = config.get('type', 'public')
        self.sandbox = config.get('sandbox', False)
        self.name = config.get('name', 'QQBot')  # 机器人名称
        self.aliases = config.get('aliases', [])  # 机器人通用名称
        
        # 设置botpy库的日志处理器
        self.setup_botpy_logger()
        
        # 初始化日志
        logger_config = get_config().get_logger_config()
        self.logger = get_logger(logger_config)
        self.logger.info("机器人初始化开始")
        
        # 初始化API客户端
        self.api_client = APIClient(self)
        
        # 初始化处理器
        self.message_handler = MessageHandler(self)
        self.guild_handler = GuildHandler(self)
        self.member_handler = MemberHandler(self)
        self.reaction_handler = ReactionHandler(self)
        
        # 启动时间
        self.start_time = time.time()
        
        # 实际设置botpy的日志处理器
        self.setup_botpy_logger()
        
        self.logger.info("机器人初始化完成")
    
    # 消息事件处理
    async def on_at_message_create(self, message: Message):
        """当收到@消息时触发"""
        await self.message_handler.handle_at_message(message)
    
    async def on_direct_message_create(self, message: Message):
        """当收到私信消息时触发"""
        await self.message_handler.handle_direct_message(message)
    
    # 频道事件处理
    async def on_guild_create(self, guild: GuildPayload):
        """当机器人加入频道时触发"""
        await self.guild_handler.handle_guild_create(guild)
    
    async def on_guild_update(self, guild: GuildPayload):
        """当频道信息更新时触发"""
        await self.guild_handler.handle_guild_update(guild)
    
    async def on_guild_delete(self, guild: GuildPayload):
        """当机器人退出频道时触发"""
        await self.guild_handler.handle_guild_delete(guild)
    
    async def on_channel_create(self, channel: ChannelPayload):
        """当子频道创建时触发"""
        await self.guild_handler.handle_channel_create(channel)
    
    async def on_channel_update(self, channel: ChannelPayload):
        """当子频道更新时触发"""
        await self.guild_handler.handle_channel_update(channel)
    
    async def on_channel_delete(self, channel: ChannelPayload):
        """当子频道删除时触发"""
        await self.guild_handler.handle_channel_delete(channel)
    
    # 成员事件处理
    async def on_guild_member_add(self, member: GuildMembers):
        """当成员加入频道时触发"""
        await self.member_handler.handle_guild_member_add(member)
    
    async def on_guild_member_update(self, member: GuildMembers):
        """当成员信息更新时触发"""
        await self.member_handler.handle_guild_member_update(member)
    
    async def on_guild_member_remove(self, member: GuildMembers):
        """当成员退出频道时触发"""
        await self.member_handler.handle_guild_member_remove(member)
    
    # 表情表态事件处理
    async def on_message_reaction_add(self, reaction: Reaction):
        """当消息被添加表情时触发"""
        await self.reaction_handler.handle_message_reaction_add(reaction)
    
    async def on_message_reaction_remove(self, reaction: Reaction):
        """当消息被移除表情时触发"""
        await self.reaction_handler.handle_message_reaction_remove(reaction)
    
    # 其他事件处理
    async def on_ready(self):
        """当机器人准备就绪时触发"""
        self.logger.info(f"机器人已就绪，启动时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time))}")
    
    def setup_botpy_logger(self):
        """设置botpy库的日志处理器，将botpy的日志记录到我们的自定义日志系统中"""
        import logging
        
        # 只有在logger初始化后才设置
        if hasattr(self, 'logger') and self.logger:
            # 获取botpy库的logger
            botpy_logger = logging.getLogger('botpy')
            
            # 创建一个自定义的日志处理器
            class BotpyLogHandler(logging.Handler):
                def __init__(self, parent_logger):
                    super().__init__()
                    self.parent_logger = parent_logger
                
                def emit(self, record):
                    # 标注清楚是botpy的日志
                    message = record.getMessage()
                    # 检查消息是否已经包含[botpy]前缀，避免重复
                    if not message.startswith('[botpy]'):
                        message = f"[botpy] {message}"
                    if record.levelno == logging.DEBUG:
                        self.parent_logger.debug(message)
                    elif record.levelno == logging.INFO:
                        self.parent_logger.info(message)
                    elif record.levelno == logging.WARNING:
                        self.parent_logger.warning(message)
                    elif record.levelno == logging.ERROR:
                        self.parent_logger.error(message)
                    elif record.levelno == logging.CRITICAL:
                        self.parent_logger.critical(message)
            
            # 清除botpy库已有的处理器
            for handler in botpy_logger.handlers:
                botpy_logger.removeHandler(handler)
            
            # 添加我们的自定义处理器
            self.botpy_log_handler = BotpyLogHandler(self.logger)
            botpy_logger.addHandler(self.botpy_log_handler)
            botpy_logger.setLevel(logging.INFO)
            # 禁用botpy库的日志传播，避免日志重复输出
            botpy_logger.propagate = False
            self.logger.info("已设置botpy库的日志处理器")
    
    async def on_error(self, error):
        """当发生错误时触发"""
        self.logger.error(f"机器人发生错误: {error}")
        # 记录详细的错误信息
        import traceback
        self.logger.error(''.join(traceback.format_exc()))
    
    def run(self):
        """运行机器人"""
        try:
            self.logger.info(f"机器人启动中... AppID: {self.appid}")
            super().run(appid=self.appid, secret=self.secret)
        except Exception as e:
            self.logger.critical(f"机器人启动失败: {e}")
            raise
