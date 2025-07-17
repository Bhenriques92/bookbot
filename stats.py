def get_num_words(text):
    return len(text.split())

def sort_on(items):
    return items["num"]

def get_num_character(text):
    character={}
    character_list=[]
    text=text.lower()
    for charac in text:
        if charac in character:
            character[charac] += 1
        else:
            character[charac] = 1
    for key, value in character.items():
        character_list.append({"char": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list


