from typing import List


def count_substrings(s: str, k: int) -> List[str]:
    n = len(s)
    substrings_arr = []

    for i in range(n):
        for j in range(i, n):
            substrings_arr.append(s[i:j+1])

    substrings_count = 0

    for substring in substrings_arr:
        if len(set(substring)) == k:
            substrings_count += 1   
    return substrings_count   


# Using sliding windows needs to be done.




if __name__ == "__main__":
    print(count_substrings("pqpqs", 2))
    print(count_substrings("abcbaa", 3))