import csv
import json


class Converter:
    def __init__(self, csv_file='books.csv', json_file='output.json'):
        self.csv_file = csv_file
        self.json_file = json_file
        self.content = []

    def read_csv(self):
        with open(self.csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.content = [row for row in reader]

    def export_json(self):
        for book in self.content:
            modified_book = {}

            for key, value in book.items():
                stripped_key = key.strip()
                modified_book[stripped_key] = value

            book.clear()
            book.update(modified_book)

        for book in self.content:
            book['ISBN'] = ''
            book['Review'] = ''

        with open(self.json_file, 'w') as jsonfile:
            json.dump(self.content, jsonfile, indent=4, ensure_ascii=False)
