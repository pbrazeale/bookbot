from stats import word_count, char_count
from report import print_report

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    # print(f"{num_words} words found in the document")
    num_char = char_count(book_text)
    # print(num_char)
    print_report(num_words, num_char)

main()
