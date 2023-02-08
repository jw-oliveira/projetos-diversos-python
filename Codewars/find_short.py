def find_short(sentence):
    words = sentence.split()
    min = 0
    
    for index in range(len(words)):
        if index == 0:
            min = len(words[0])        
        
        if min > len(words[index]):
            min = len(words[index])

    return min  