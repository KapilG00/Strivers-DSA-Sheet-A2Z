from typing import List


# TC ->  O(n+klog k); where n is the length of the string and k is unique characters in given string.
# SC -> O(k)
def sort_string_characters_by_freq(s: str) -> List[str]:
    n = len(s)
    char_freq = []
    char_freq_map = {}

    for i in range(n):
        if s[i] not in char_freq_map:
            char_freq_map[s[i]] = 1
        else:
            char_freq_map[s[i]] += 1

    for key, value in char_freq_map.items():
        char_freq.append((key, value))
    
    char_freq.sort(key=lambda item: (-item[1], item[0])) #  # frequency descending, character ascending
    
    """
    Suppose, char_freq = [('a', 3), ('c', 1), ('b', 3), ('d', 2)].

    Python internally does something conceptually similar to:

    [
        ((-3, 'a'), ('a', 3)),
        ((-1, 'c'), ('c', 1)),
        ((-3, 'b'), ('b', 3)),
        ((-2, 'd'), ('d', 2))
    ]

    Now, python sort() compares tuples lexicographically (left to right).

    Sorts by the first tuple (the key):

    (-3, 'a')
    (-3, 'b')
    (-2, 'd')
    (-1, 'c')

    and then returns the original values in that order:

    [
        ('a', 3),
        ('b', 3),
        ('d', 2),
        ('c', 1)
    ]

    """

    result = []

    for char, freq in char_freq:
        if freq > 0:
            result.append(char)

    return result

# TC ->  O(n+klog k); where n is the length of the string and k is the constant 26 for the alphabet.
# SC -> O(k)
def sort_string_characters_by_freq(s: str) -> List[str]:
        # Create a list of tuples to store frequency and character
        freq = [(0, chr(i + ord('a'))) for i in range(26)]

        # Count the frequency of each character in the string
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] = (freq[index][0] + 1, ch)

        # Sort by frequency in descending order, then by character in ascending order
        freq.sort(key=lambda x: (-x[0], x[1]))

        # Collect characters that have non-zero frequency
        result = [ch for f, ch in freq if f > 0]
        return result



if __name__ == "__main__":
    print(sort_string_characters_by_freq("tree"))
    print(sort_string_characters_by_freq("raaaajj"))
    print(sort_string_characters_by_freq("circumnavigate"))