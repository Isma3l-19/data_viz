from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
#from paginate_pandas import paginate
from werkzeug.utils import secure_filename

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
  #route for the uploaded data
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
        #Data processing based on file extension
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            #Unsupported file format
            return render_template('error.html', message="Unsupported file format. Only CSV, XLSX and XLS files are allowed.")
            
          #Processing complete, rendering the index.html
          #Passing DataFrame as JSON for potential usage in the template 
        return render_template('index.html', message="Dataset uploaded and processed successfuly!", data=df.to_json())
    except Exception as e:
            #Handle any exceptions during data processing
            return render_template('error.html', message=f"An error occured while processing the data: {str(e)}")
    else:
        return redirect(request.url)
    
@app.route("/view_data/<filename>", methods=['GET'])
def view_data(filename):
    # Construct the file path
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        return render_template("error.html", message="File not found")

    try:
        # Read the uploaded dataset file
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            # Unsupported file format
            return render_template("error.html", message="Unsupported file format. Only CSV, XLSX, and XLS files are allowed.")
        
        # Pagination logic
        page = request.args.get('page', 1, type=int)
        per_page = 10  # Number of rows per page
        offset = (page - 1) * per_page
        data = df.iloc[offset:offset + per_page]
        
        # Pass the data and pagination information to the view_data.html template
        return render_template("view_data.html", data=data.to_html(index=False), page=page)
    except Exception as e:
        # Handle any exceptions
        return render_template("error.html", message=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)