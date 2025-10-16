import sys
from stats import count_words
from stats import count_characters
from stats import sort_character_dictionary

def get_book_text(filepath):
    if filepath == None or filepath == "":
        return None
    
    file_contents =""

    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book = get_book_text(path)
    num_words = count_words(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    character_count = count_characters(book)
    character_list = sort_character_dictionary(character_count)
    for character_dict in character_list:
        if character_dict["char"].isalpha():
            print(f"{character_dict["char"]}: {character_dict["num"]}")
    
    print("============= END ===============")
main()