def is_palindrome_iterative(word):
    if word == '':
        return False
    reversed_word = ''
    for letter in word:
        reversed_word = f'{letter}{reversed_word}'
    if word == reversed_word:
        return True
    return False
