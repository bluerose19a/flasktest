from flask import Flask, redirect, render_template, request  # Flaskクラスをインポート
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   # Flaskクラスのインスタンス生成
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    article = db.Column(db.Text(), nullable=False)

@app.before_first_request
def init():
    db.create_all()
    
    
@app.route('/',methods=["GET"])  # routeデコレーター:どのURLで関数を呼び出すか
def index():
    posts = Post.query.all()
    return render_template('card.html',posts=posts)  # flaskにしてほしい処理を書く


@app.route('/',methods=["POST"])  # routeデコレーター:どのURLで関数を呼び出すか
def posting():
    name = request.form.get('name')
    article = request.form.get('article')
    new_post = Post(name=name,article=article)
    db.session.add(new_post)
    db.session.commit()
    return redirect('/')



if __name__ == "__main__":  # nameとはモジュール名、
    app.run(debug=True)  # デバッグモード:本番環境ではfalseにする
# にこにこ掲示板