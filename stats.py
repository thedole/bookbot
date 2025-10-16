def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    lowered_string = string.lower()
    dict = {}

    for char in lowered_string:
        if char not in dict:
            dict[char] = 0
        dict[char] += 1
    
    return dict

def sort_character_dictionary(characters):
    character_list = []

    for character, count in characters.items():
        character_list.append({"char": character, "num": count})

    sort_on = lambda item: item["num"]

    character_list.sort(key=sort_on, reverse=True)

    return character_list