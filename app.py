from flask import Flask,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'User_numbers':      'sqlite:///users_mobile_number.db'
}
db = SQLAlchemy(app)

class User(db.Model):
    __bind_key__ = 'User_numbers' 
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(250))
    mobile_number = db.Column(db.String(250),unique=True, nullable=False)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
   if request.method == 'POST':
       country_code = request.form.get('countryCode')
       mobile_number = request.form.get('mobile-number')
       new_user = User(country_code=country_code, mobile_number=mobile_number)
       db.session.add(new_user)
       db.session.commit()
       return render_template('thank-you.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)    
