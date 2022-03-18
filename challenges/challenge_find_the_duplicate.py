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


def find_duplicate(nums):
    if nums is None or len(nums) == 1:
        return False
    quicksort(nums, 0, len(nums) - 1)
    previous_number = 'Not a number'
    for num in nums:
        if type(num) is not int or num < 0:
            return False
        if num == previous_number:
            return num
        previous_number = num
    return False
