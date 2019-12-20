# coding:utf-8
from flask import Flask
import config
from app import app

app = Flask(__name__)
app.config.from_object(config.py)

# 通过配置文件加载配置
@app.route("/")
def index():
    # appid_content = current_app.config.get("appId")
    return "hello flask"  + app.config['appId']
 
if __name__ == '__main__':
    app.run()