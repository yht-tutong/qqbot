from botpy.types.guild import GuildPayload
from botpy.types.channel import ChannelPayload

class GuildHandler:
    """频道处理器类"""
    
    def __init__(self, client):
        """初始化频道处理器
        
        Args:
            client: 机器人客户端实例
        """
        self.client = client
        self.logger = client.logger
    
    async def handle_guild_create(self, guild: GuildPayload):
        """处理机器人加入频道事件
        
        Args:
            guild: 频道对象
        """
        try:
            self.logger.info(f"机器人加入频道: {guild['name']} (ID: {guild['id']})")
            # 可以在这里添加欢迎消息或其他初始化操作
        except Exception as e:
            self.logger.error(f"处理机器人加入频道事件失败: {e}")
    
    async def handle_guild_update(self, guild: GuildPayload):
        """处理频道信息更新事件
        
        Args:
            guild: 频道对象
        """
        try:
            self.logger.info(f"频道信息更新: {guild['name']} (ID: {guild['id']})")
        except Exception as e:
            self.logger.error(f"处理频道信息更新事件失败: {e}")
    
    async def handle_guild_delete(self, guild: GuildPayload):
        """处理机器人退出频道事件
        
        Args:
            guild: 频道对象
        """
        try:
            self.logger.info(f"机器人退出频道: {guild['name']} (ID: {guild['id']})")
        except Exception as e:
            self.logger.error(f"处理机器人退出频道事件失败: {e}")
    
    async def handle_channel_create(self, channel: ChannelPayload):
        """处理子频道创建事件
        
        Args:
            channel: 子频道对象
        """
        try:
            self.logger.info(f"创建子频道: {channel['name']} (ID: {channel['id']}) 类型: {channel['type']}")
        except Exception as e:
            self.logger.error(f"处理子频道创建事件失败: {e}")
    
    async def handle_channel_update(self, channel: ChannelPayload):
        """处理子频道更新事件
        
        Args:
            channel: 子频道对象
        """
        try:
            self.logger.info(f"更新子频道: {channel['name']} (ID: {channel['id']})")
        except Exception as e:
            self.logger.error(f"处理子频道更新事件失败: {e}")
    
    async def handle_channel_delete(self, channel: ChannelPayload):
        """处理子频道删除事件
        
        Args:
            channel: 子频道对象
        """
        try:
            self.logger.info(f"删除子频道: {channel['name']} (ID: {channel['id']})")
        except Exception as e:
            self.logger.error(f"处理子频道删除事件失败: {e}")
