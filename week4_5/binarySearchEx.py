def linearSearch(number_to_find, number_list):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1


def binarySearch(number_to_find, number_list):
    leftIndex = 0
    rightIndex = len(number_list) - 1

    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        midNumber = number_list[midIndex]

        if midNumber == number_to_find:
            return midIndex

        if midNumber < number_to_find:
            leftIndex = midIndex + 1
        if midNumber > number_to_find:
            rightIndex = midIndex - 1

    return -1


def binarySearchRecursive(number_to_find, number_list, left_index, right_index):
    if right_index < left_index:
        return -1
    midIndex = (left_index + right_index) // 2
    midNumber = number_list[midIndex]

    if midNumber == number_to_find:
        return midIndex

    if midNumber < number_to_find:
        left_index = midIndex + 1
    if midNumber > number_to_find:
        right_index = midIndex - 1
    return binarySearchRecursive(number_to_find, number_list, left_index, right_index)


if __name__ == "__main__":
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    numberToFind = 24

    # print(linearSearch(numberToFind, numbers))
    # print(binarySearch(19, numbers))
    # print(binarySearchRecursive(122, numbers, 0, len(numbers) - 1))
    print(binarySearchList(15, numbers))
