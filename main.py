from stats import get_num_words, get_num_char,sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath)as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(get_book_text(book_path))} total words")
        print("--------- Character Count -------")
        list_of_dicts = sort_dictionary(get_num_char(get_book_text(book_path)))
        for i in list_of_dicts:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")

main()