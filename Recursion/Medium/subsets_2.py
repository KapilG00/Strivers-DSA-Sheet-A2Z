# TC: O(n * 2^n)
# SC: O(n * 2^n)
# Brute-force
def subsets_2(
    arr: list[int], idx: int, subset_arr: list[int], subsets_set: set[tuple[int]]
) -> None:

    # base case
    if idx == len(arr):
        subsets_set.add(tuple(subset_arr))
        return

    # take
    subset_arr.append(arr[idx])
    subsets_2(arr, idx + 1, subset_arr, subsets_set)

    # not take
    subset_arr.pop()
    subsets_2(arr, idx + 1, subset_arr, subsets_set)


def main_1(arr: list[int]) -> list[list[int]]:
    subsets_set = set()
    subsets_2(arr, 0, [], subsets_set)

    return [list(subset) for subset in subsets_set]


# TC: O(2^n)
# SC: O(n)
# Optimal
def subsets_2_optimal(
    arr: list[int], idx: int, subset_arr: list[int], subsets_arr: list[list[int]]
) -> None:
    subsets_arr.append(subset_arr.copy())

    for i in range(idx, len(arr)):
        # skip duplicates
        if i > idx and arr[i] == arr[i - 1]:
            continue

        subset_arr.append(arr[i])
        subsets_2_optimal(arr, i + 1, subset_arr, subsets_arr)
        subset_arr.pop()


def main_2(arr: list[int]) -> list[list[int]]:
    subsets_arr = []
    subsets_2_optimal(arr, 0, [], subsets_arr)
    return subsets_arr


if __name__ == "__main__":
    print(main_2([1, 2, 2]))
