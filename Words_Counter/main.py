print(f'='*30)
print(f'{"SENTENCE WORDS COUNTER":^30}')
print(f'='*30)

sentence = str(input('Enter the sentence: ')).split()

if not sentence:
    print("You didn't enter a valid sentence.")
else:
    print(f'This sentence has {len(sentence)} words and {len(''.join(sentence))} characters.')