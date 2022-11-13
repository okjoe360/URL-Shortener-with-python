from flask import Flask,redirect,url_for,render_template,request
from app.db import db, User
from app.fxn import short_generator

app=Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db.init_app(app)



@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        link = request.form['link']
        short = short_generator()
        short_link = User(url=link, short=short)
        db.session.add(short_link)
        db.session.commit()
        return render_template('index.html', link=link, short=short)
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    links = User.query.order_by(User.date_created).all()
    return render_template('about.html', links=links)



@app.route('/<slug>',methods=['GET'])
def shortlink(slug):
    link = User.query.filter_by(short=slug).first_or_404()
    return redirect(link.url)

