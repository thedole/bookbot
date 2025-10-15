from stats import count_words

def get_book_text(filepath):
    if filepath == None or filepath == "":
        return None
    
    file_contents =""

    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = count_words(frankenstein)
    print(f"Found {num_words} total words")

main()