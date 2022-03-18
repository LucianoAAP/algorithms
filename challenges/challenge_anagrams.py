def quicksort(list, low, high):
    if len(list) == 1:
        return list

    if low < high:
        partition_index = partition(list, low, high)
        quicksort(list, low, partition_index - 1)
        quicksort(list, partition_index + 1, high)


def partition(list, low, high):
    i = low - 1
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    quicksort(first_list, 0, len(first_string) - 1)
    quicksort(second_list, 0, len(second_string) - 1)
    sorted_first_string = ''.join(first_list)
    sorted_second_string = ''.join(second_list)

    if sorted_first_string == sorted_second_string:
        return True

    return False
