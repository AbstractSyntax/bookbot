def get_num_words(book_text):
    return len(book_text.split())

def get_num_char(book_text):
    dict_of_char = {}
    for c in book_text.lower():
        if c in dict_of_char:
            dict_of_char[c] += 1
        else:
            dict_of_char[c] = 1
    return dict_of_char

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    list_of_dicts = []
    for dict in dictionary:
        list_of_dicts.append({"char":dict, "num":dictionary[dict]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts