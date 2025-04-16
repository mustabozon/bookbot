from stats import get_num_words
from stats import count_char


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_char(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
