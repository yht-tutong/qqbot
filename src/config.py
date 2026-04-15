import yaml
import os

class ConfigManager:
    """配置管理类"""
    
    def __init__(self, config_file='config/config.yaml'):
        """初始化配置管理器
        
        Args:
            config_file: 配置文件路径
        """
        self.config_file = config_file
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = yaml.safe_load(f)
                print(f"配置文件加载成功: {self.config_file}")
            else:
                print(f"配置文件不存在: {self.config_file}")
        except Exception as e:
            print(f"加载配置文件失败: {e}")
    
    def get(self, key, default=None):
        """获取配置值
        
        Args:
            key: 配置键，支持嵌套，如 'qqbot.appid'
            default: 默认值
        
        Returns:
            配置值或默认值
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_qqbot_config(self):
        """获取QQ机器人配置
        
        Returns:
            dict: QQ机器人配置
        """
        return self.get('qqbot', {})
    
    def get_logger_config(self):
        """获取日志配置
        
        Returns:
            dict: 日志配置
        """
        return self.get('logger', {})
    
    def get_commands_config(self):
        """获取命令配置
        
        Returns:
            dict: 命令配置
        """
        return self.get('commands', {})
    
    def get_other_config(self):
        """获取其他配置
        
        Returns:
            dict: 其他配置
        """
        return self.get('other', {})
    
    def update_config(self, key, value):
        """更新配置
        
        Args:
            key: 配置键
            value: 配置值
        """
        keys = key.split('.')
        config = self.config
        
        for i, k in enumerate(keys[:-1]):
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        
        # 保存到文件
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.config, f, default_flow_style=False, allow_unicode=True)
            print(f"配置更新成功: {key} = {value}")
        except Exception as e:
            print(f"保存配置失败: {e}")

# 全局配置实例
config_instance = None

def get_config(config_file='config/config.yaml'):
    """获取全局配置实例
    
    Args:
        config_file: 配置文件路径
    
    Returns:
        ConfigManager: 配置管理实例
    """
    global config_instance
    if config_instance is None:
        config_instance = ConfigManager(config_file)
    return config_instance
