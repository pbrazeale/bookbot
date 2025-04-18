def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    lines_list = text.split("\n")
    # print(lines_list)
    text_list = []
    for line in lines_list:
        line_list = line.split(" ")
        for word in line_list:
            if word != " " and word != "":
                text_list.append(word)

    # print(text_list)
    return len(text_list)



def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

main()
