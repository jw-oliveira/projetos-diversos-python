def replace_word(string, to_replace, replacemnt):

    print(string.replace(to_replace, replacemnt))


string = str(input('Enter the phrase: '))
to_replace = str(input('Enter the word to be changed: '))
replacement = str(input('Enter the new word: '))

replace_word(string, to_replace, replacement)
