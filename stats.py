def get_num_words(string):
    return len(string.split())

def count_characters(string):
    character_dict = {}
    for letter in string:
        if letter.lower() in character_dict:
            character_dict[letter.lower()] += 1
        else:
            character_dict[letter.lower()] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list_of_dicts = []
    for item in dict:
        if item.isalpha():
            mini = {"character": item, "count": dict[item]}
            list_of_dicts.append(mini)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts