# TC: O(n)
# SC: O(1)
def roman_numerals_to_integer(s: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    integer_value = 0
    idx = len(s)-1

    while idx >= 0: # Here we are traversing from right to left.
        # If "I" before "V" or "X" decreament the current value by 1.
        if s[idx] == "I" and idx != len(s)-1  and (s[idx+1] == "V" or s[idx+1] == "X"):
            integer_value -= 1
        
        # If "X" before "L" or "C" decreament the current value by 10.
        elif s[idx] == "X" and (s[idx+1] == "L" or s[idx+1] == "C"):
            integer_value -= 10
        
        # If "C" before "D" or "M" decreament the current value by 100.
        elif s[idx] == "C" and (s[idx+1] == "D" or s[idx+1] == "M"):
            integer_value -= 100

        else:
            integer_value += roman_dict[s[idx]]

        print("integer value:", integer_value)

        idx -= 1


    return integer_value    

# TC: O(n)
# SC: O(1)
def roman_numerals_to_integer(s: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    integer_value = 0
    idx = len(s)-1

    for idx in range(idx): # Here, we are traversing from left to right.
        if roman_dict[s[idx]] < roman_dict[s[idx+1]]:
            integer_value -= roman_dict[s[idx]]
        else:
            integer_value += roman_dict[s[idx]]

        print("integer value:", integer_value)    

    return integer_value + roman_dict[s[-1]]




if __name__ == "__main__":
    print(roman_numerals_to_integer("LVIII"))
    print(roman_numerals_to_integer("MCMXCIV"))