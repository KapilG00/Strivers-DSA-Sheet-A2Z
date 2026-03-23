def check_palindrome(input_str: str, idx: int) -> bool:
    # base case.
    if idx >= (len(input_str)/2):
        return True
    
    # compare two opposite side characters of string.
    if input_str[idx] != input_str[len(input_str)-1-idx]:
        return False
    
    # recursice call.
    return check_palindrome(input_str, idx+1)

    
if __name__ == "__main__":
    print(check_palindrome("ABCDCBA", 0))
    print(check_palindrome("1233214", 0))