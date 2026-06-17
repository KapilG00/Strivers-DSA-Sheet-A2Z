
# TC -> O(n)
# SC -> O(1)
def largest_odd_number_in_string(string: str) -> str:
    n = len(string)
    idx = -1

    for i in range(n-1,-1,-1): # Iterating in reverse (end -> start).
        if (int(string[i]) % 2) == 1:
            idx = i
            break
    # Skipping any leading zeroes.    
    j = 0
    while j <= idx and string[j] == '0':
        j += 1
    print(idx, j)    
    return string[j:idx+1]    


if __name__ == "__main__":
    print(largest_odd_number_in_string("5347"))
    print(largest_odd_number_in_string("0214638"))