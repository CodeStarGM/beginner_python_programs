# A SILLY (-_-) GAME CREATED BY CODESTARGM JUST FOR LEARNING PURPOSE!
import time
eated_words = []

print(
"""
+================================+
| Welcome to Vowel Killer Game,  |
| Enter any word you like        |
| But Remember I hate vowels     |
| type carefully or else you're  |
| gonna lost your vowel friend.  |
| Created by CodeStarGM          |
+================================+
""")

user_word = input('Enter Any Word You Like: ')
words = user_word.upper()

for l in words:
    time.sleep(1)
    if l == 'A':
        eated_words += 'A'
        continue
    elif l == 'E':
        eated_words += 'E'
        continue
    elif l == 'I':
        eated_words += 'I'
        continue
    elif l == 'O':
        eated_words += 'O'
        continue
    elif l == 'U':
        eated_words += 'U'
        continue
    else:
        print(l)

print(
"""
+================================+
| I Told Ya! I hate vowels       |
| So! I killed your              |
| vowel friend/ friends          |
| you can pick his dead body     |
| Below..!                       |
+================================+
""")
print("x(-_-)x \n" ,eated_words)





