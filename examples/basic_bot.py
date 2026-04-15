#!/usr/bin/env python3
"""基本机器人示例"""

import sys
import os

# 添加父目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import get_config
from src.bot import QQBot

# 加载配置
config = get_config()
qqbot_config = config.get_qqbot_config()

# 初始化机器人
bot = QQBot(qqbot_config)

# 运行机器人
print("基本机器人示例启动中...")
bot.run()
