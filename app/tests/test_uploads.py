import unittest
from io import StringIO

from main import app, allowed_file, upload_dataset

class UploadTest(unittest.TestCase):

    def test_allowed_extensions(self):
        # Test allowed extensions
        self.assertTrue(allowed_file('test.csv'))
        self.assertTrue(allowed_file('data.xlsx'))
        self.assertFalse(allowed_file('report.txt'))

    def test_upload_empty_file(self):
        # Test empty file upload
        with app.test_client() as client:
            data = {'dataset': (StringIO(''), 'test.csv')}
            response = client.post('/upload_dataset', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 302)  # Redirect

    def test_upload_invalid_filename(self):
        # Test upload with invalid filename
        with app.test_client() as client:
            data = {'dataset': (StringIO('This is some data'), '')}
            response = client.post('/upload_dataset', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 302)  # Redirect

    def test_upload_valid_csv(self):
        # Test upload valid CSV file
        with app.test_client() as client:
            data = {'dataset': (StringIO('col1,col2\ndata1,data2'), 'test.csv')}
            response = client.post('/upload_dataset', data=data, follow_redirects=True)
            self.assertIn(b'Dataset uploaded and processed successfuly!', response.data)

