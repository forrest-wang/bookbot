import sys
from stats import get_word_count, get_char_count, get_sorted_list

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    char_counts = get_char_count(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_contents)} total words")
    print("--------- Character Count -------")

    char_count_list = get_sorted_list(char_counts)
    for char_count in char_count_list:
        curr_char = char_count["char"]
        if curr_char.isalpha() == False:
            continue
        
        print(f"{curr_char}: {char_count["num"]}")
    print("============= END ===============")

main()