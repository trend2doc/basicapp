# Flaskクラスをimportする
from flask import Flask

# Flaskクラスをインスタンス化する
app = Flask(__name__)


# URL「/」にPython関数をマッピングする
@app.route("/")
def index():
    return "Hello World!"
