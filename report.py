def print_report(word_count, char_dic):
    print(
        f"""
        ============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------
        Found {word_count} total words
        --------- Character Count -------
        """
    )
    for char in char_dic:
        print(f"{char_dic[char]["char"]}: {char_dic[char]["count"]}")
    
    print("============= END ===============")