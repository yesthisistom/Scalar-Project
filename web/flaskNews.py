__author__ = 'tv'


from libs.article import Article
from libs.sqlcreator import create_alchemy_engine

from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, redirect, url_for, flash, request

app = Flask(__name__)
app.secret_key = '0823##*_OJKH*Gjjuu&&&55(*&(*&(7^%%'

@app.route('/article/<id>')
def getArticle(id=None):
    if not id:
        return

    return render_template('article.html', article = [x for x in session.query(Article).filter(Article.id == id)][0])


@app.route("/", methods=['GET', 'POST'])
@app.route('/<page>')
def getNews(page=0):

    global session

    per_page = 10
    offset = int(page)*per_page

    print("Offset:", offset)
    if request.method == 'POST':
        print("Post")
        return render_template('index.html', articles=session.query(Article).
                               order_by(desc(Article.date)).limit(10).offset(offset), page=int(page))
    else:
        print("Get")
        return render_template('index.html', articles=session.query(Article).
                               order_by(desc(Article.date)).limit(10).offset(offset), page=int(page))


if __name__ == '__main__':
    engine = create_alchemy_engine()

    Session = sessionmaker(bind=engine)
    session = Session()

    app.debug = True
    app.run(host='0.0.0.0', port=8080)