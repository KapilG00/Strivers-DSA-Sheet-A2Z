# TC: O(n^2)
# SC: O(1) or O(number of distinct characters in a given string)
def sum_of_beauty_of_all_substrings(s: str):
    sum_of_beauty = 0

    for i in range(len(s)):
        map = {}
        for j in range(i, len(s)):
            map[s[j]] = map.get(s[j], 0) + 1

            values = map.values()
            max_freq = max(values)
            min_freq = min(values)

            sum_of_beauty += (max_freq-min_freq)

    return sum_of_beauty



if __name__ == "__main__":
    print(sum_of_beauty_of_all_substrings("xyx"))
    print(sum_of_beauty_of_all_substrings("aabcbaa"))