
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ckx.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
db = SQLAlchemy(app)


class Kullanici(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement = True)
    mail = db.Column(db.String(100), nullable = False )
    feedback = db.Column(db.String(30), nullable = False)



# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def feedback_form():
    if request.method == 'POST':
        mail = request.form["email"]
        feedback = request.form["text"]

        kullanıcı = Kullanici(mail=mail, feedback=feedback)
        db.session.add(kullanıcı)
        db.session.commit()
        return redirect("/")

def process_form():
    button_python = request.form.get('button_python')
    if button_python:
        return render_template('index.html', button_python=button_python)
    


if __name__ == "__main__":
    app.run(debug=True)
