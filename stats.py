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