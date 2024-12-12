from flask import Flask, request, render_template, jsonify
from datetime import datetime, timedelta
import csv
from io import StringIO
import sqlite3
import pymysql
import os
from config import Config
from functools import wraps
from flask import session, redirect, url_for

app = Flask(__name__)

# 添加session配置
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(hours=2)  # session保持2小时

def get_db_connection():
    if Config.DB_TYPE == 'mysql':
        return pymysql.connect(
            host=Config.MYSQL_HOST,
            port=int(Config.MYSQL_PORT),
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE,
            charset='utf8mb4'
        )
    else:
        if not os.path.exists('instance'):
            os.makedirs('instance')
        return sqlite3.connect(Config.SQLITE_DB_PATH)

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    
    if Config.DB_TYPE == 'mysql':
        c.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                action VARCHAR(255) NOT NULL,
                timestamp VARCHAR(255) NOT NULL,
                country VARCHAR(255),
                os_info VARCHAR(255),
                cpu_arch VARCHAR(255)
            )
        ''')
    else:
        c.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                country TEXT,
                os_info TEXT,
                cpu_arch TEXT
            )
        ''')
    
    conn.commit()
    conn.close()

# 初始化数据库
init_db()

# 修改登录验证装饰器
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if Config.WEB_PASSWORD and not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# 添加登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if not Config.WEB_PASSWORD:
        return redirect(url_for('view_logs'))
        
    if request.method == 'POST':
        if request.form.get('password') == Config.WEB_PASSWORD:
            session.permanent = True  # 启用永久session
            session['logged_in'] = True
            return redirect(url_for('view_logs'))
        return render_template('login.html', error='密码错误')
    return render_template('login.html')

@app.route('/api/log', methods=['POST'])
def collect_log():
    try:
        data = request.get_json()
        
        # 验证必需字段
        required_fields = ['action', 'timestamp', 'country', 'os_info', 'cpu_arch']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # 存储到数据库
        conn = get_db_connection()
        c = conn.cursor()
        
        if Config.DB_TYPE == 'mysql':
            c.execute('''
                INSERT INTO logs (action, timestamp, country, os_info, cpu_arch)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                data['action'],
                data['timestamp'],
                data['country'],
                data['os_info'],
                data['cpu_arch']
            ))
        else:
            c.execute('''
                INSERT INTO logs (action, timestamp, country, os_info, cpu_arch)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                data['action'],
                data['timestamp'],
                data['country'],
                data['os_info'],
                data['cpu_arch']
            ))
        
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logs')
@login_required
def view_logs():
    conn = get_db_connection()
    c = conn.cursor()
    
    if Config.DB_TYPE == 'mysql':
        c.execute('SELECT * FROM logs ORDER BY id ASC')
    else:
        c.execute('SELECT * FROM logs ORDER BY id ASC')
    
    logs = c.fetchall()
    conn.close()
    
    # 将查询结果转换为字典列表
    logs_list = []
    for log in logs:
        logs_list.append({
            'id': log[0],
            'action': log[1],
            'timestamp': log[2],
            'country': log[3],
            'os_info': log[4],
            'cpu_arch': log[5]
        })
    
    return render_template('logs.html', logs=logs_list)

@app.route('/clear-logs', methods=['POST'])
def clear_logs():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        if Config.DB_TYPE == 'mysql':
            c.execute('DELETE FROM logs')
        else:
            c.execute('DELETE FROM logs')
        
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': '日志已清除'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 