from flask import Flask,render_template,request,flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
import smtplib
from wtforms import ValidationError
app = Flask(__name__)
mail= Mail(app)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'papiashvil@gmail.com'
app.config['MAIL_PASSWORD'] = 'fsdqudsdyqcvxrch'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

class ContactForm(FlaskForm):
    name=StringField('სახელი', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    text = StringField('ტექსტი',validators=[DataRequired()])
    submit = SubmitField('გაგზავნა')



@app.route('/')
def homepage():

    return render_template("homepage.html",check="home")


@app.route('/contact', methods=['GET', 'POST'])
def send_mail():
    form = ContactForm()
    data = request.args
    user_name = data.get("name")
    user_mail = data.get("email")
    user_text = data.get("text")
    msg = Message(user_name, sender='papiashvil@gmail.com', recipients=['papiashvil@gmail.com',user_mail])
    msg.body = user_name+" "+user_mail+" "+user_text
    msg.title = 'title'
    mail.send(msg)
    flash('Blog Post Created')






    return render_template('contact.html', form=form, check="contact")






if __name__ =='__main__':
    app.run(port=5000,debug = True)
