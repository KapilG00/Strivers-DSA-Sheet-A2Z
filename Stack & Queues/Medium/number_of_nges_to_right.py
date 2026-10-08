def merge(
    pairs_arr: list[int], low: int, mid: int, high: int, nge_arr: list[int]
) -> None:
    left = low
    right = mid + 1
    temp_arr = []

    while left <= mid and right <= high:
        if pairs_arr[left][0] < pairs_arr[right][0]:
            nge_arr[pairs_arr[left][1]] += high - right + 1
            temp_arr.append((pairs_arr[left][0], pairs_arr[left][1]))
            left += 1
        else:
            temp_arr.append((pairs_arr[right][0], pairs_arr[right][1]))
            right += 1

    while left <= mid:
        temp_arr.append((pairs_arr[left][0], pairs_arr[left][1]))
        left += 1

    while right <= high:
        temp_arr.append((pairs_arr[right][0], pairs_arr[right][1]))
        right += 1

    for i in range(low, high + 1):
        pairs_arr[i] = temp_arr[i - low]


def merge_sort(pairs_arr, low, high, nge_arr) -> None:
    if low == high:
        return

    mid = (low + high) // 2

    merge_sort(pairs_arr, low, mid, nge_arr)
    merge_sort(pairs_arr, mid + 1, high, nge_arr)

    merge(pairs_arr, low, mid, high, nge_arr)


def number_of_nges_to_right(arr: list[int], q: int, ind: list[int]) -> list[int]:
    n = len(arr)
    pairs_arr = []
    nge_arr = [0] * n

    for i in range(n):
        pairs_arr.append((arr[i], i))

    merge_sort(pairs_arr, 0, n - 1, nge_arr)

    final = []

    for i in range(q):
        final.append(nge_arr[ind[i]])

    return final


if __name__ == "__main__":
    print(number_of_nges_to_right([3, 4, 2, 7, 5, 8, 10, 6], 2, [0, 5]))
