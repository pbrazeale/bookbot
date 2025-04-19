import sys
from stats import word_count, char_count
from report import print_report

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    # print(f"{num_words} words found in the document")
    num_char = char_count(book_text)
    # print(num_char)
    print_report(num_words, num_char)

main()
