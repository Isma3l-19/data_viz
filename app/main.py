from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'app/data/uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'ismael123456789'

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
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif filename.endswith('.xlsx') or filename.endswith('.xls'):
                df = pd.read_excel(file_path)
            else:
                return render_template('error.html', message="Unsupported file format. Only CSV, XLSX and XLS files are allowed.")
            
            return render_template('index.html', message="Dataset uploaded and processed successfully!", data=df.to_json())
        except Exception as e:
            return render_template('error.html', message=f"An error occurred while processing the data: {str(e)}")
    else:
        return redirect(request.url)

@app.route("/view_data/<filename>", methods=['GET'])
def view_data(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return render_template("error.html", message="File not found")

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            return render_template("error.html", message="Unsupported file format. Only CSV, XLSX, and XLS files are allowed.")
                
        page = request.args.get('page', 1, type=int)
        per_page = 10  # Number of rows per page
        offset = (page - 1) * per_page
        data = df.iloc[offset:offset + per_page]
        
        columns = df.columns.tolist()
        total_pages = (len(df) // per_page) + (1 if len(df) % per_page else 0)
        
        return render_template("view_data.html", data=data, columns=columns, page=page, total_pages=total_pages, filename=filename)
    except Exception as e:
        return render_template("error.html", message=f"An error occurred: {str(e)}")
    
@app.route("/list_files", methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    num_files = len(files)
    
    return render_template("file_list.html", num_files=num_files, files=files)

@app.route("/delete_file/<filename>", methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash("File deleted successfully", "success")
        return redirect(url_for('list_files'))
    else:
        flash("File not found", "error")
        return redirect(url_for('list_files'))

@app.route("/generate_plot", methods=['POST'])
def generate_plot():
    filename = request.json['filename']
    x_axis = request.json['x_axis']
    y_axis = request.json['y_axis']

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        data = {
            "x": df[x_axis].tolist(),
            "y": df[y_axis].tolist()
        }

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
