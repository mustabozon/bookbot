def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        words_num = len(words)

    print(f"{words_num} words found in the document")        


get_book_text("books/frankenstein.txt")
