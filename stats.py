def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    lowercase = book_text.lower()
    char_counts = {}
    for i in range(1, len(lowercase)):
        char_counts[lowercase[i]] = char_counts.get(lowercase[i], 0) + 1
    return char_counts

def get_sorted_list(char_counts):
    char_count_list = []
    for key, value in char_counts.items():
        char_count_list.append({"char": key, "num": value})
    char_count_list.sort(key=lambda char_count_dict: char_count_dict["num"], reverse=True)
    return char_count_list