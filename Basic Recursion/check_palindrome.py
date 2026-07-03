def check_palindrome(input_str: str, idx: int) -> bool:
    n = len(input_str)
    # base case.
    if idx >= (n//2):
        return True
    
    # compare two opposite side characters of string.
    if input_str[idx] != input_str[n-idx-1]:
        return False
    
    # recursive call.
    return check_palindrome(input_str, idx+1)

    
if __name__ == "__main__":
    print(check_palindrome("ABCDCBA", 0))
    print(check_palindrome("1233214", 0))