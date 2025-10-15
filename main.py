def get_book_text(filepath):
    if filepath == None or filepath == "":
        return None
    
    file_contents =""

    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()