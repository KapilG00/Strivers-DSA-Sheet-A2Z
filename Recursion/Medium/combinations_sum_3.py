# TC: O(K * 2^9)
# SC: O(number of combinations * K)
def combinations_sum_3(
    N: int,
    K: int,
    idx: int,
    combination_arr: list[int],
    combinations_arr: list[list[int]],
) -> None:

    # If the sum is zero and the number of elements is K.
    if N == 0 and len(combination_arr) == K:
        combinations_arr.append(combination_arr.copy())

    # To exclude cases/combinations where we exceed the size of K and when N<=0
    # e.g. if N=5 & K=2 and our "i" is 5.
    # Since it is our first element we reached the condition N=0,
    # but our combination is of length 1,
    # and the required length of the correct combination needs to be equal to K.
    if N <= 0 or len(combination_arr) > K:
        return

    for i in range(idx, 10):
        if i <= N:
            combination_arr.append(i)
            combinations_sum_3(N - i, K, i + 1, combination_arr, combinations_arr)
            combination_arr.pop()
        else:
            break


def main(N: int, K: int) -> list[list[int]]:
    combinations_arr = []
    combination_arr = []
    combinations_sum_3(N, K, 1, combination_arr, combinations_arr)
    return combinations_arr


if __name__ == "__main__":
    N = 7
    K = 3
    print(main(N, K))
