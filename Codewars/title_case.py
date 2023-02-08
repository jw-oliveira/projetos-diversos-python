def title_case(title, minor_words=''):

    capitalized = []
    minor_list = []

    title = title.lower()    

    for minor_word in minor_words.split():
        minor_list.append(minor_word.lower())
      
    for word in title.split():        
        if word in minor_list:            
            capitalized.append(word)
        elif word not in minor_words.split():
            capitalized.append(word.capitalize())

    if len(capitalized) > 0:
        capitalized[0] = capitalized[0].capitalize()

    capitalized_text = ' '.join(capitalized)

    return capitalized_text