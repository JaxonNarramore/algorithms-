def merge_sort(list):
    if len(list) > 1:
        middle_list = len(list) // 2
        right_list = list[:middle_list]
        left_list = list[:middle_list]

        merge_sort(right_list)
        merge_sort(left_list)


def sort(left_list, right_list):
    sorted_list = []
    l = 0
    r = 0

    while l < len(left_list) and r < len(right_list):
        if left_list[l] < right_list[r]:
            sorted_list.append(left_list[l])
            l += 1
        else:
            sorted_list.append(right_list[r])
            r += 1

    while l < len(left_list):
        sorted_list.append(left_list[l])
        l += 1

    while r < len(right_list):
        sorted_list.append(right_list[r])
        r += 1

    return sorted_list


list_to_sort = [20, 55, 67, 2, 5, 78, 99, 105, 63, 77, 25, 21]
print(merge_sort(list_to_sort))
