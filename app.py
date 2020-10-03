from flask import Flask,render_template,request,flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from flask_googletrans import translator

import smtplib
from wtforms import ValidationError
app = Flask(__name__)
ts = translator(
    app=app,
    cache=True, # To enable caching by default is disabled
    fail_safe=False, # returns original text if fetching translation failed
    skip_app=False, # to skip checking app for .init_app()
    file_name='gt_cache.json', # To change the default name of the cache file
    route=False # opens up a route on /gtran/<fromL>/<toL>/<text> to fetch translation as json response {translation: 'text ...'}
)
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
    user_name = StringField('Username',render_kw={"placeholder": "სახელი"},
                            validators=[DataRequired("შეიყვანეთ სახელი")])
    user_mail = StringField('EMail',render_kw={"placeholder": "Email"},
                            validators=[Email(), DataRequired()])
    user_text = StringField('Text',render_kw={"placeholder": "ტექსტი"},
                            validators=[DataRequired("შეიყვანეთ ტექსტი")])
    submit = SubmitField('Submit')

@app.route('/')
def homepage():
    form = ContactForm()
    return render_template("homepage.html")


@app.route('/contact', methods=['GET', 'POST'])
def send_mail():
    user_name=None
    user_mail=None
    user_text=None
    form = ContactForm()
    if form.validate_on_submit():
        user_name= form.user_name.data
        form.user_name.data = ''
        user_mail = form.user_mail.data
        form.user_mail.data = ''
        user_text = form.user_text.data
        form.user_text.data = ''
        msg = Message('title', sender='papiashvil@gmail.com', recipients=['papiashvil@gmail.com',user_mail])
        msg.body = f"Dear {user_name},\n your mail({user_text})was successfully sent to the company mail.\n\nBest Regards,\nZura "

        mail.send(msg)

    return render_template('contact.html',form=form)






if __name__ =='__main__':
    app.run(port=5000,debug = True)
