#!/usr/bin/env python3
"""QQ机器人主入口"""

from src.config import get_config
from src.logger import get_logger
from src.bot import QQBot
import sys
import traceback

def main():
    """主函数"""
    try:
        # 加载配置
        config = get_config()
        qqbot_config = config.get_qqbot_config()
        
        # 检查配置
        if not qqbot_config.get('appid') or not qqbot_config.get('token'):
            print("错误: 配置文件中缺少 appid 或 token")
            return
        
        # 初始化机器人
        bot = QQBot(qqbot_config)
        
        # 运行机器人
        bot.run()
        
    except KeyboardInterrupt:
        print("\n机器人已手动停止")
    except Exception as e:
        print(f"机器人运行出错: {e}")
        traceback.print_exc()
        # 记录崩溃日志
        logger = get_logger(config.get_logger_config())
        if logger:
            logger.log_exception(sys.exc_info())
        return

if __name__ == "__main__":
    main()
