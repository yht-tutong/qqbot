from botpy.types.message import Message
from ..api.client import APIClient

class MessageHandler:
    """消息处理器类"""
    
    def __init__(self, client):
        """初始化消息处理器
        
        Args:
            client: 机器人客户端实例
        """
        self.client = client
        self.api = APIClient(client)
        self.logger = client.logger
    
    async def handle_at_message(self, message: Message):
        """处理@消息
        
        Args:
            message: 消息对象
        """
        try:
            self.logger.info(f"收到@消息: {message.content} 来自: {message.author.username}")
            self.logger.info(f"消息ID: {message.id}, 频道ID: {message.channel_id},  guildID: {message.guild_id}")
            
            # 去除@机器人的部分
            content = message.content.replace(f"<@!{self.client.appid}>", "").strip()
            self.logger.info(f"处理后的消息内容: {content}")
            
            if not content:
                # 回复默认消息
                self.logger.info("准备回复默认消息")
                await self.api.send_message(
                    channel_id=message.channel_id,
                    content="你好！我是QQ机器人，有什么可以帮助你的吗？"
                )
                self.logger.info("默认消息回复成功")
            else:
                # 处理命令
                self.logger.info(f"准备处理命令: {content}")
                await self.handle_command(message, content)
                self.logger.info("命令处理完成")
        except Exception as e:
            self.logger.error(f"处理@消息失败: {e}")
            import traceback
            self.logger.error(''.join(traceback.format_exc()))
    
    async def handle_direct_message(self, message: Message):
        """处理私信消息
        
        Args:
            message: 消息对象
        """
        try:
            self.logger.info(f"收到私信: {message.content} 来自: {message.author.username}")
            
            # 回复私信
            await self.api.send_dms(
                guild_id=message.guild_id,
                user_id=message.author.id,
                content=f"你好！我收到了你的私信: {message.content}"
            )
        except Exception as e:
            self.logger.error(f"处理私信消息失败: {e}")
    
    async def handle_command(self, message: Message, content: str):
        """处理命令
        
        Args:
            message: 消息对象
            content: 命令内容
        """
        try:
            # 简单的命令处理
            if content == "help" or content == "帮助":
                await self.api.send_message(
                    channel_id=message.channel_id,
                    content="可用命令:\n" 
                    "!help - 查看帮助\n" 
                    "!info - 查看频道信息\n" 
                    "!channels - 查看子频道列表\n" 
                    "!hello - 打招呼"
                )
            elif content == "hello" or content == "你好":
                await self.api.send_message(
                    channel_id=message.channel_id,
                    content=f"你好！{message.author.username}，很高兴认识你！"
                )
            elif content == "info" or content == "信息":
                # 获取频道信息
                guild = await self.api.get_guild(guild_id=message.guild_id)
                await self.api.send_message(
                    channel_id=message.channel_id,
                    content=f"频道名称: {guild['name']}\n" 
                    f"频道ID: {guild['id']}\n" 
                    f"成员数量: {guild['member_count']}\n" 
                    f"创建时间: {guild['joined_at']}"
                )
            elif content == "channels" or content == "频道":
                # 获取子频道列表
                channels = await self.api.get_channels(guild_id=message.guild_id)
                channel_names = [channel['name'] for channel in channels]
                await self.api.send_message(
                    channel_id=message.channel_id,
                    content=f"子频道列表: {', '.join(channel_names)}"
                )
            else:
                # 未知命令
                await self.api.send_message(
                    channel_id=message.channel_id,
                    content=f"未知命令: {content}\n请使用 !help 查看可用命令"
                )
        except Exception as e:
            self.logger.error(f"处理命令失败: {e}")
            await self.api.send_message(
                channel_id=message.channel_id,
                content="处理命令时发生错误，请稍后再试"
            )
