def swap_vowels(text) :
    word = ''
    for ch in text :
        if ch.lower() in "aeiou":
            word += '*'
        else :
            word += ch
    return word
print(swap_vowels("hello world"))   # h*ll* w*rld
print(swap_vowels("Python"))        # Pyth*n
