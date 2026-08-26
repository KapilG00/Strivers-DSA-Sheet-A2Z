# TC: O(n*2^n)
# SC: O(n*2^n)
def print_all_possible_subsequences_of_string(s: str) -> list[str]:
    list_of_subsequences = [s[0]]

    for char in s[1:]:
        temp_subsequences = []

        for subsequence in list_of_subsequences:
            temp_subsequences.append(subsequence + char)

        list_of_subsequences.extend(temp_subsequences)
        list_of_subsequences.append(char)

    return list_of_subsequences        



if __name__ == "__main__":
    print(print_all_possible_subsequences_of_string("abc"))
    print(print_all_possible_subsequences_of_string("aa"))