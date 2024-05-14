# Interactive Data Visualization App

This is a Flask web application for interactive data visualization. Users can upload datasets in CSV, XLSX, or XLS format, view the uploaded data, and generate interactive plots using Plotly.

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask application by executing `python main.py`.
4. Open a web browser and navigate to `http://localhost:5000` to access the application.

## Features

### Upload Dataset

Users can upload datasets in CSV, XLSX, or XLS format using the upload form on the homepage.

### View Uploaded Files

Users can view a list of all uploaded files. Each file is displayed as a clickable link that directs the user to view the data.

### View Uploaded Data

Users can view the data of an uploaded file in a paginated table format. Pagination allows users to navigate through large datasets.

### Delete Uploaded File

Users can delete an uploaded file directly from the interface by clicking the delete button next to the file in the list of uploaded files.

### Flash Messages

Flash messages are displayed to provide feedback to the user after certain actions, such as successful file upload or deletion.

## Integrating Plotly

Plotly integration will allow users to generate interactive plots from their uploaded data.

## Directory Structure

- `app/`: Contains the Flask application files.
    - `data/`: Directory for storing uploaded datasets.
    - `static/`: Static files such as CSS and JavaScript.
    - `templates/`: HTML templates for rendering pages.
- `main.py`: Main Flask application file.
- `requirements.txt`: List of Python dependencies.

## Contributors

- Ismael Nyambu

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
