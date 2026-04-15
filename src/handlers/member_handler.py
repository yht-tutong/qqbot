from botpy.types.guild import GuildMembers

class MemberHandler:
    """成员处理器类"""
    
    def __init__(self, client):
        """初始化成员处理器
        
        Args:
            client: 机器人客户端实例
        """
        self.client = client
        self.logger = client.logger
        self.api = client.api_client
    
    async def handle_guild_member_add(self, member: GuildMembers):
        """处理成员加入频道事件
        
        Args:
            member: 成员对象
        """
        try:
            username = member['user']['username']
            user_id = member['user']['id']
            self.logger.info(f"成员加入: {username} (ID: {user_id})")
            
            # 可以在这里添加欢迎消息
            # 注意：需要获取频道的系统消息频道ID
            # await self.api.send_message(
            #     channel_id="系统消息频道ID",
            #     content=f"欢迎 {username} 加入频道！"
            # )
        except Exception as e:
            self.logger.error(f"处理成员加入事件失败: {e}")
    
    async def handle_guild_member_update(self, member: GuildMembers):
        """处理成员信息更新事件
        
        Args:
            member: 成员对象
        """
        try:
            username = member['user']['username']
            user_id = member['user']['id']
            self.logger.info(f"成员信息更新: {username} (ID: {user_id})")
        except Exception as e:
            self.logger.error(f"处理成员信息更新事件失败: {e}")
    
    async def handle_guild_member_remove(self, member: GuildMembers):
        """处理成员退出频道事件
        
        Args:
            member: 成员对象
        """
        try:
            username = member['user']['username']
            user_id = member['user']['id']
            self.logger.info(f"成员退出: {username} (ID: {user_id})")
        except Exception as e:
            self.logger.error(f"处理成员退出事件失败: {e}")
