import unittest
import json
import os
from converter import Converter
from main import app, read_data


class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_read_data(self):
        data = read_data()
        self.assertIsInstance(data, list)
        self.assertTrue(all(isinstance(book, dict) for book in data))

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Booklist', response.data)

    def test_output_json_file_exists(self):
        converter = Converter(csv_file='books.csv', json_file='output.json')
        converter.read_csv()
        converter.export_json()
        self.assertTrue(os.path.exists('output.json'))

    def test_output_json_file_content(self):
        converter = Converter(csv_file='books.csv', json_file='output.json')
        converter.read_csv()
        converter.export_json()

        with open('output.json', 'r') as file:
            data = json.load(file)
            self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
