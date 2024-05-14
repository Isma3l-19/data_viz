# Interactive Data Visualization App

This is a Flask web application for interactive data visualization. Users can upload datasets in CSV, XLSX, or XLS format, view the uploaded data, and generate interactive plots using Plotly.

![Screenshot](app/static/images/landing%20page.png)

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository to your local machine;
    ```bash
    git clone https://github.com/Isma3l-19/data_viz.git
2. cd Dataviz
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Run the Flask application by executing `python main.py`.
5. Open a web browser and navigate to `http://localhost:5000` to access the application.

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

Plotly integration allows users to generate interactive plots from their uploaded data.

## Directory Structure

- `app/`: Contains the Flask application files.
    - `data/`: Directory for storing uploaded datasets.
    - `static/`: Static files such as CSS and JavaScript.
    - `templates/`: HTML templates for rendering pages.
- `main.py`: Main Flask application file.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributers are welcomed! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch('git checkout -b feature/YourFeature') .
3. Commit your changes('git commit -am "Add some feature"').
4. Push to the branch ('git push origin feature/YourFeature').
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
