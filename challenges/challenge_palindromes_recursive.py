def reverse(word, low_index, high_index):
    if low_index == high_index:
        return word
    word = word[0:low_index] + word[high_index] + word[low_index:high_index]
    return reverse(word, low_index + 1, high_index)


def is_palindrome_recursive(word, low_index, high_index):
    if word is None or word == '':
        return False
    reversed_word = reverse(word, low_index, high_index)
    if reversed_word == word:
        return True
    return False
