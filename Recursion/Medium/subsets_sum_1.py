# TC: O(2^n)
# SC: O(2^n)
def subsets_sum_1(
    arr: list[int], idx: int, subset_sum: int, subsets_sum_arr: list[int]
) -> list[int]:

    # base case
    if idx == len(arr):
        subsets_sum_arr.append(subset_sum)
        return

    # take
    subset_sum += arr[idx]
    subsets_sum_1(arr, idx + 1, subset_sum, subsets_sum_arr)

    # not take
    subset_sum -= arr[idx]
    subsets_sum_1(arr, idx + 1, subset_sum, subsets_sum_arr)


def calculate_sum_of_each_subset(arr: list[list[int]]) -> list[int]:
    sums_arr = []
    subsets_sum_1(arr, 0, 0, sums_arr)
    sums_arr.sort()
    return sums_arr


if __name__ == "__main__":
    arr = [5, 2, 1]
    print(calculate_sum_of_each_subset(arr))
