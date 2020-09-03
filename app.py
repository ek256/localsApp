from flask import Flask, render_template

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/")
def index():
    return render_template('homePage.html')
