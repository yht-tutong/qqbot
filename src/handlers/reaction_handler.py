from botpy.types.reaction import Reaction

class ReactionHandler:
    """表情表态处理器类"""
    
    def __init__(self, client):
        """初始化表情表态处理器
        
        Args:
            client: 机器人客户端实例
        """
        self.client = client
        self.logger = client.logger
    
    async def handle_message_reaction_add(self, reaction: Reaction):
        """处理消息被添加表情表态事件
        
        Args:
            reaction: 表情表态对象
        """
        try:
            user_id = reaction['user_id']
            channel_id = reaction['channel_id']
            message_id = reaction['target']['id']
            emoji_id = reaction['emoji']['id']
            emoji_type = reaction['emoji']['type']
            
            self.logger.info(f"用户 {user_id} 在频道 {channel_id} 的消息 {message_id} 上添加了表情表态: 类型={emoji_type}, ID={emoji_id}")
        except Exception as e:
            self.logger.error(f"处理消息被添加表情表态事件失败: {e}")
    
    async def handle_message_reaction_remove(self, reaction: Reaction):
        """处理消息被移除表情表态事件
        
        Args:
            reaction: 表情表态对象
        """
        try:
            user_id = reaction['user_id']
            channel_id = reaction['channel_id']
            message_id = reaction['target']['id']
            emoji_id = reaction['emoji']['id']
            emoji_type = reaction['emoji']['type']
            
            self.logger.info(f"用户 {user_id} 在频道 {channel_id} 的消息 {message_id} 上移除了表情表态: 类型={emoji_type}, ID={emoji_id}")
        except Exception as e:
            self.logger.error(f"处理消息被移除表情表态事件失败: {e}")
