def alphabet_position(text):
    char_number = {'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7,
    'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M': 13, 'N':14, 'O': 15, 'P':16,
    'Q': 17, 'R':18, 'S':19, 'T':20, 'U':21, 'W':22, 'V':23, 'X':24, 'Y':25,
     'Y':26, 'Z':27}
    characters = []
    characters_position = []

    for char in text:
        characters.append(char.upper())

    for char in characters:
        try:
            characters_position.append(str(char_number[char]))
        except:
            pass

    numbers = ' '.join(characters_position)
    
    return numbers