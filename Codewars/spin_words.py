def spin_words(sentence):
    words = sentence.split()
    new_words = []
        
    for index in range(len(words)):
        word = words[index]
        if len(word) >= 5:
            reversed_word = word[::-1]
            new_words.append(reversed_word)
        else:
            new_words.append(word)

    return ' '.join(new_words)