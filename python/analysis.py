def analyze(text) :
    letters = 0
    digits = 0
    spaces = 0
    symbols = 0
    for i in text :
        if i.isalpha() :
            letters += 1
        elif i.isdigit() :
            digits += 1
        elif i.isspace() :
            spaces += 1
        else :
            symbols += 1
    print(f'Letters: {letters}\nDigits: {digits}\nSpaces: {spaces}\nSymbols: {symbols}')
analyze("Hi there 123!")
# Letters: 7
# Digits: 3
# Spaces: 2
# Symbols: 1
