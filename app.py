from flask import Flask,render_template,send_file

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template("homepage.html")

@app.route('/about')
def about():

    return render_template("postGallery.html")

@app.route('/templates/header.html')
def header():

    return send_file("templates/header.html")

@app.route('/templates/slider.html')
def slider():

    return send_file("templates/slider.html")

@app.route('/templates/postAbout.html')
def post_about():

    return send_file("templates/postAbout.html")

@app.route('/templates/postGallery.html')
def post_gallery():

    return send_file("templates/postGallery.html")


@app.route('/templates/postService.html')
def post_service():

    return send_file("templates/postService.html")











if __name__ =='__main__':
    app.run(port=5000,debug = True)
