from flask import Flask, render_template
import json
import random
from converter import Converter

app = Flask(__name__)

data_file = 'output.json'


def read_data():
    converter = Converter(csv_file='books.csv', json_file='output.json')
    converter.read_csv()
    converter.export_json()

    with open(data_file, 'r') as file:
        data = json.load(file)

    for book in data:
        book.setdefault('title', book.get('Titel', ''))
        book.setdefault('author', book.get('Autor', ''))
        book.setdefault('color', generate_random_color())

    return data


def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


@app.route('/')
def index():
    books = read_data()
    return render_template('index.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
