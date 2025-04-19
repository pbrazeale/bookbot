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

def char_sort(char_dict):
    def sort_on(dict):
        return dict["count"]
    sorted = []
    for char in char_dict:
        if char.isalpha():
            sorted.append({"char": char, "count": char_dict[char]})
    
    sorted.sort(reverse=True, key=sort_on)
    # print(sorted)


def char_count(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    char_sort(char_count)

