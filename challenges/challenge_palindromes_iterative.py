def is_palindrome_iterative(word):
    if word is None or word == '':
        return False
    reversed_word = ''
    for letter in word:
        reversed_word = letter + reversed_word
    if word == reversed_word:
        return True
    return False
