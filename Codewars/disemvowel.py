def disemvowel(string):
    without_vowel = []
    vowel = 'AaEeIiOoUu'
    for char in string:
        if char not in vowel:
            without_vowel.append(char)
    
    return ''.join(without_vowel)
    

print(disemvowel('Casa na Árvore'))