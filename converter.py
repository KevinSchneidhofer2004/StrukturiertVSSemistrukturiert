import csv
import json

with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    content = [row for row in reader]

for book in content:
    modified_book = {key.strip(): value for key, value in book.items()}
    book.clear()
    book.update(modified_book)

for book in content:
    book['ISBN'] = ''
    book['Review'] = ''

with open('output.json', 'w') as jsonfile:
    json.dump(content, jsonfile, indent=4, ensure_ascii=False)
