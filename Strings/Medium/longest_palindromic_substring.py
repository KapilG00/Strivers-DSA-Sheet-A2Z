# TC: O(n^2)
# SC: O(n)
def longest_palindromic_substring(s: str) -> str:
    res = ""
    res_len = 0

    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            print("INSIDE ODD LENGTH WHILE LOOP", s[i])
            if (right-left+1) > res_len:
                res = s[left:right+1]
                res_len = right-left+1
            left -= 1
            right += 1

        # Even length palindromes
        left, right = i, i+1    

        while left >= 0 and right < len(s) and s[left] == s[right]:
            print("INSIDE EVEN LENGTH WHILE LOOP", s[i])
            if (right-left+1) > res_len:
                res = s[left:right+1]
                res_len = right-left+1
            left -= 1
            right += 1    

    return res


if __name__ == "__main__":
    print(longest_palindromic_substring("babad"))
    print(longest_palindromic_substring("cbbd"))