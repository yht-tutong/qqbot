import os
import logging
from logging.handlers import RotatingFileHandler
import time
import traceback

class Logger:
    """日志系统类"""
    
    def __init__(self, config):
        """初始化日志系统
        
        Args:
            config: 日志配置
        """
        self.config = config
        self.logger = None
        self.setup_logger()
    
    def setup_logger(self):
        """设置日志系统"""
        # 创建日志目录
        log_dir = self.config.get('file_path', 'logs/')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # 生成日志文件名，包含时间戳
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        base_name = self.config.get('file_name', 'bot.log')
        name, ext = os.path.splitext(base_name)
        log_file = f"{log_dir}{name}_{timestamp}{ext}"
        
        # 创建logger
        self.logger = logging.getLogger('QQBot')
        self.logger.setLevel(self.config.get('level', 'INFO'))
        
        # 清除已有的处理器
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)
        
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.config.get('level', 'INFO'))
        
        # 创建文件处理器，支持轮转
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=self.config.get('max_bytes', 10485760),  # 10MB
            backupCount=self.config.get('backup_count', 5),
            encoding='utf-8'  # 设置编码为utf-8，避免乱码
        )
        file_handler.setLevel(self.config.get('level', 'INFO'))
        
        # 设置格式
        log_format = self.config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        # 添加处理器
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        
        # 禁用日志传播，避免日志重复
        self.logger.propagate = False
        
        # 记录启动信息
        self.logger.info(f"日志系统初始化完成，日志文件: {log_file}")
    
    def log_exception(self, exc_info):
        """记录异常信息
        
        Args:
            exc_info: 异常信息
        """
        if self.logger:
            self.logger.critical("机器人崩溃，详细信息如下:")
            self.logger.critical(''.join(traceback.format_exception(*exc_info)))
    
    def get_logger(self):
        """获取logger实例
        
        Returns:
            logging.Logger: logger实例
        """
        return self.logger
    
    def debug(self, msg, *args, **kwargs):
        """记录debug级别的日志"""
        if self.logger:
            self.logger.debug(msg, *args, **kwargs)
    
    def info(self, msg, *args, **kwargs):
        """记录info级别的日志"""
        if self.logger:
            self.logger.info(msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        """记录warning级别的日志"""
        if self.logger:
            self.logger.warning(msg, *args, **kwargs)
    
    def error(self, msg, *args, **kwargs):
        """记录error级别的日志"""
        if self.logger:
            self.logger.error(msg, *args, **kwargs)
    
    def critical(self, msg, *args, **kwargs):
        """记录critical级别的日志"""
        if self.logger:
            self.logger.critical(msg, *args, **kwargs)

# 全局日志实例
logger_instance = None

def get_logger(config=None):
    """获取全局日志实例
    
    Args:
        config: 日志配置
    
    Returns:
        Logger: 日志实例
    """
    global logger_instance
    if logger_instance is None and config:
        logger_instance = Logger(config)
    return logger_instance
