from flask import Flask,render_template
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
@app.route('/')
def index():

    return render_template('index.html')


if __name__ =='__main__':
    app.run(port=5000,debug = True)
