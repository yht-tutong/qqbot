# QQ机器人项目

## 项目介绍

这是一个基于 [botpy](https://github.com/tencentcloud/botpy) 库开发的QQ机器人项目，支持多种事件处理和API调用功能。

## 功能特性

- 支持频道消息、私信消息处理
- 支持频道事件、成员事件、表情表态事件处理
- 提供丰富的API客户端，方便调用QQ开放平台接口
- 完善的日志系统，支持不同级别的日志记录
- 支持命令前缀配置和冷却时间设置

## 项目结构

```
qqbot/
├── config/             # 配置文件目录
│   └── config.yaml     # 机器人配置文件
├── examples/           # 示例代码目录
│   └── basic_bot.py    # 基础机器人示例
├── src/                # 源代码目录
│   ├── api/            # API客户端
│   │   └── client.py   # API调用实现
│   ├── handlers/       # 事件处理器
│   │   ├── guild_handler.py     # 频道事件处理
│   │   ├── member_handler.py    # 成员事件处理
│   │   ├── message_handler.py   # 消息事件处理
│   │   └── reaction_handler.py  # 表情表态事件处理
│   ├── bot.py          # 机器人主类
│   ├── config.py       # 配置管理
│   └── logger.py       # 日志管理
├── main.py             # 主入口文件
└── README.md           # 项目文档
```

## 安装步骤

1. 克隆项目到本地

```bash
git clone https://github.com/yht-tutong/qqbot/master.git
cd qqbot
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 配置机器人信息

编辑 `config/config.yaml` 文件，填写你的机器人信息：

```yaml
qqbot:
  appid: "你的appid"
  token: "你的token"
  secret: "你的secret"
  type: "public"  # public 或 private
  sandbox: true  # 沙箱模式
  name: "机器人名称"
  aliases: ["别名1", "别名2"]
```

## 使用方法

### 启动机器人

```bash
python main.py
```

### 事件处理

机器人会自动处理以下事件：

- 频道消息事件（@机器人）
- 私信消息事件
- 频道创建、更新、删除事件
- 子频道创建、更新、删除事件
- 成员加入、更新、退出事件
- 表情表态添加、删除事件

### API调用

可以通过 `api_client` 调用各种API：

```python
# 发送消息
await bot.api_client.send_message(channel_id, content)

# 发送私信
await bot.api_client.send_dms(guild_id, user_id, content)

# 获取频道信息
guild = await bot.api_client.get_guild(guild_id)

# 获取子频道列表
channels = await bot.api_client.get_channels(guild_id)

# 获取频道成员列表
members = await bot.api_client.get_guild_members(guild_id)
```

## 配置说明

### 机器人配置

- `appid`: 机器人的AppID
- `token`: 机器人的Token
- `secret`: 机器人的Secret
- `type`: 机器人类型，public或private
- `sandbox`: 是否开启沙箱模式
- `name`: 机器人英文名称
- `aliases`: 机器人通用名称列表

### 日志配置

- `level`: 日志级别（DEBUG, INFO, WARNING, ERROR, CRITICAL）
- `format`: 日志格式
- `file_path`: 日志文件路径
- `file_name`: 日志文件名
- `max_bytes`: 日志文件最大大小（字节）
- `backup_count`: 日志文件备份数量

### 命令配置

- `prefix`: 命令前缀
- `help_command`: 帮助命令
- `admin_commands`: 管理员命令列表

### 其他配置

- `timeout`: API调用超时时间（秒）
- `retry_times`: API调用重试次数
- `cooldown`: 命令冷却时间（秒）

## 注意事项

1. 请确保在 `config.yaml` 文件中正确填写机器人的AppID、Token和Secret
2. 沙箱模式下，机器人只能在测试频道中使用
3. 生产环境中请将 `sandbox` 设置为 `false`
4. 定期检查日志文件，及时发现和解决问题

## 贡献

欢迎提交Issue和Pull Request，共同改进这个项目。

## 许可证

MIT License
