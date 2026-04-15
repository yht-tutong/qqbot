import botpy
from botpy import Client
from botpy.types.message import Message
from botpy.types.guild import GuildPayload, GuildMembers
from botpy.types.channel import ChannelPayload
from botpy.types.reaction import Reaction
from botpy.types.message import DmsPayload
from botpy.types.audio import AudioControl
from botpy.types.announce import Announce
from botpy.types.pins_message import PinsMessage
from botpy.types.schedule import Schedule
from botpy.types.emoji import Emoji
import asyncio
import time

class APIClient:
    """API客户端类"""
    
    def __init__(self, client):
        """初始化API客户端
        
        Args:
            client: botpy.Client实例
        """
        self.client = client
        self.api = client.api
        self.retry_times = 3
        self.timeout = 30
    
    async def retry(func):
        """重试装饰器"""
        async def wrapper(self, *args, **kwargs):
            retries = 0
            while retries < self.retry_times:
                try:
                    return await func(self, *args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries >= self.retry_times:
                        raise
                    self.client.logger.error(f"API调用失败，重试中 ({retries}/{self.retry_times}): {e}")
                    await asyncio.sleep(1)
        return wrapper
    
    # 消息相关API
    async def send_message(self, channel_id, content, embed=None, ark=None, image=None):
        """发送消息
        
        Args:
            channel_id: 频道ID
            content: 消息内容
            embed: 嵌入消息
            ark: ARK消息
            image: 图片
        
        Returns:
            消息对象
        """
        try:
            return await self.api.post_message(
                channel_id=channel_id, 
                content=content, 
                embed=embed, 
                ark=ark, 
                image=image
            )
        except Exception as e:
            self.client.logger.error(f"发送消息失败: {e}")
            raise
    
    async def send_dms(self, guild_id, user_id, content):
        """发送私信
        
        Args:
            guild_id: 频道ID
            user_id: 用户ID
            content: 消息内容
        
        Returns:
            私信对象
        """
        try:
            return await self.api.post_dms(
                guild_id=guild_id, 
                user_id=user_id, 
                content=content
            )
        except Exception as e:
            self.client.logger.error(f"发送私信失败: {e}")
            raise
    
    # 频道相关API
    async def get_guild(self, guild_id):
        """获取频道信息
        
        Args:
            guild_id: 频道ID
        
        Returns:
            频道对象
        """
        try:
            return await self.api.get_guild(guild_id=guild_id)
        except Exception as e:
            self.client.logger.error(f"获取频道信息失败: {e}")
            raise
    
    async def get_channels(self, guild_id):
        """获取子频道列表
        
        Args:
            guild_id: 频道ID
        
        Returns:
            子频道列表
        """
        try:
            return await self.api.get_channels(guild_id=guild_id)
        except Exception as e:
            self.client.logger.error(f"获取子频道列表失败: {e}")
            raise
    
    async def get_channel(self, channel_id):
        """获取子频道信息
        
        Args:
            channel_id: 子频道ID
        
        Returns:
            子频道对象
        """
        try:
            return await self.api.get_channel(channel_id=channel_id)
        except Exception as e:
            self.client.logger.error(f"获取子频道信息失败: {e}")
            raise
    
    async def create_channel(self, guild_id, name, type, position=None):
        """创建子频道
        
        Args:
            guild_id: 频道ID
            name: 子频道名称
            type: 子频道类型
            position: 子频道位置
        
        Returns:
            子频道对象
        """
        try:
            return await self.api.create_channel(
                guild_id=guild_id, 
                name=name, 
                type=type, 
                position=position
            )
        except Exception as e:
            self.client.logger.error(f"创建子频道失败: {e}")
            raise
    
    async def update_channel(self, channel_id, name=None, position=None):
        """修改子频道
        
        Args:
            channel_id: 子频道ID
            name: 子频道名称
            position: 子频道位置
        
        Returns:
            子频道对象
        """
        try:
            return await self.api.update_channel(
                channel_id=channel_id, 
                name=name, 
                position=position
            )
        except Exception as e:
            self.client.logger.error(f"修改子频道失败: {e}")
            raise
    
    async def delete_channel(self, channel_id):
        """删除子频道
        
        Args:
            channel_id: 子频道ID
        
        Returns:
            操作结果
        """
        try:
            return await self.api.delete_channel(channel_id=channel_id)
        except Exception as e:
            self.client.logger.error(f"删除子频道失败: {e}")
            raise
    
    # 成员相关API
    async def get_guild_member(self, guild_id, user_id):
        """获取频道成员信息
        
        Args:
            guild_id: 频道ID
            user_id: 用户ID
        
        Returns:
            成员对象
        """
        try:
            return await self.api.get_guild_member(
                guild_id=guild_id, 
                user_id=user_id
            )
        except Exception as e:
            self.client.logger.error(f"获取频道成员信息失败: {e}")
            raise
    
    async def get_guild_members(self, guild_id, limit=100, after=None):
        """获取频道成员列表
        
        Args:
            guild_id: 频道ID
            limit: 成员数量限制
            after: 分页标记
        
        Returns:
            成员列表
        """
        try:
            return await self.api.get_guild_members(
                guild_id=guild_id, 
                limit=limit, 
                after=after
            )
        except Exception as e:
            self.client.logger.error(f"获取频道成员列表失败: {e}")
            raise
    
    async def delete_guild_member(self, guild_id, user_id, reason=None):
        """删除频道成员
        
        Args:
            guild_id: 频道ID
            user_id: 用户ID
            reason: 删除原因
        
        Returns:
            操作结果
        """
        try:
            return await self.api.delete_guild_member(
                guild_id=guild_id, 
                user_id=user_id, 
                reason=reason
            )
        except Exception as e:
            self.client.logger.error(f"删除频道成员失败: {e}")
            raise
    
    # 表情表态相关API
    async def post_reaction(self, channel_id, message_id, emoji_type, emoji_id):
        """发表表情表态
        
        Args:
            channel_id: 频道ID
            message_id: 消息ID
            emoji_type: 表情类型
            emoji_id: 表情ID
        
        Returns:
            操作结果
        """
        try:
            return await self.api.post_reaction(
                channel_id=channel_id, 
                message_id=message_id, 
                emoji_type=emoji_type, 
                emoji_id=emoji_id
            )
        except Exception as e:
            self.client.logger.error(f"发表表情表态失败: {e}")
            raise
    
    async def delete_reaction(self, channel_id, message_id, emoji_type, emoji_id, user_id=None):
        """删除表情表态
        
        Args:
            channel_id: 频道ID
            message_id: 消息ID
            emoji_type: 表情类型
            emoji_id: 表情ID
            user_id: 用户ID，不填则删除自己的表态
        
        Returns:
            操作结果
        """
        try:
            return await self.api.delete_reaction(
                channel_id=channel_id, 
                message_id=message_id, 
                emoji_type=emoji_type, 
                emoji_id=emoji_id, 
                user_id=user_id
            )
        except Exception as e:
            self.client.logger.error(f"删除表情表态失败: {e}")
            raise
    
    async def get_reaction_users(self, channel_id, message_id, emoji_type, emoji_id, limit=20, after=None):
        """获取表情表态用户列表
        
        Args:
            channel_id: 频道ID
            message_id: 消息ID
            emoji_type: 表情类型
            emoji_id: 表情ID
            limit: 数量限制
            after: 分页标记
        
        Returns:
            用户列表
        """
        try:
            return await self.api.get_reaction_users(
                channel_id=channel_id, 
                message_id=message_id, 
                emoji_type=emoji_type, 
                emoji_id=emoji_id, 
                limit=limit, 
                after=after
            )
        except Exception as e:
            self.client.logger.error(f"获取表情表态用户列表失败: {e}")
            raise
