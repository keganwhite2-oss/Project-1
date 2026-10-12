def encode(text, shift) :
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   result = ''
   for ch in text.lower():
      if ch.isalpha():
         position = alphabet.index(ch)
         new_position = (position + shift) % 26 # hint: % 26 handles the wrap-around
         result += alphabet[new_position]
      else:
         result += ch
   return result
print(encode("hello", 3))          # khoor
print(encode("xyz", 3))            # abc
print(encode("hi there!", 1))      # ij uifsf!
