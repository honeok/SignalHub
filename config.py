import os

class Config:
    # 数据库配置
    DB_TYPE = os.environ.get('DB_TYPE', 'sqlite')  # 默认使用 sqlite
    
    # Web访问密码配置
    WEB_PASSWORD = os.environ.get('WEB_PASSWORD', '')  # 默认无密码
    
    # MySQL配置
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', 3306)
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'password')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'logs')
    
    # SQLite配置
    SQLITE_DB_PATH = os.environ.get('SQLITE_DB_PATH', 'instance/logs.db') 