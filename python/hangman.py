def hangman() :
    word = 'Georgia'
    full_word = word.lower()
    letter_list = []
    while len(full_word) > len(letter_list) :
        letter_list.append('_')
    print(letter_list)
    lives = 6
    while '_' in letter_list and lives > 0:
        guess_letter = input('What letter would you like to guess?: ')
        if guess_letter in full_word:
            for i in range(len(full_word)):
                if full_word[i] == guess_letter:
                    letter_list[i] = guess_letter
        else:
            lives -= 1
            print(f'Nope! {lives} lives left')
        print(letter_list)
    if '_' in letter_list:
        print('You Lose!')
    else :
        print('You Win!')
hangman()
