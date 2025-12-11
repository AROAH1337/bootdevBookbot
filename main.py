from stats import count_chars
from stats import report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as file:
        contents = file.read()
        return contents

def main():
    get_book_text(book_path)

#count_words(book_path)
book_text = get_book_text(book_path)
chars_count = count_chars(book_text)

report(chars_count, book_path)