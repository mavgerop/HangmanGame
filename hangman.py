import random

with open('words.txt', 'r', encoding="utf8") as f:
    word = random.choice(f.readlines()).rstrip()

tries = 6
letters = []
# print(word)
def hide():
    hidden = ''
    for letter in word:
        if letter in letters:
            hidden += letter
        else:
            hidden += '-'
    return hidden

while tries > 0:
    hidden_word = hide()
    if hidden_word == word:
        print('Συγχαρητήρια το βρήκατε!')
        print('Η λέξη ήταν {word}')
        exit()
        
    print(hidden_word)
    letter = input('Γραμμα; ')
    if letter in letters:
        print('Εχετε δοκιμάσει ήδη αυτό το γράμμα')
        continue

    letters.append(letter)
    if letter in word:
        print('Το γράμμα υπάρχει!')
    else:
        print('Το γράμμα δε βρέθηκε!')
        tries -= 1
    print(f"Απομένουν {tries} προσπαθειες")

print('Χάσατε!')
print(f'Η λέξη ήταν: {word}')


