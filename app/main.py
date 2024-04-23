# basic flask application to server our routes

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'app/data/uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/upload_dataset", methods=['POST'])
def upload_dataset():
    if 'dataset' not in request.files:
        return redirect(request.url)
    file = request.files['dataset']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    else:
        return redirect(request.url)    

if __name__ == "__main__":
    app.run(debug=True)