# TC -> O(n)
# SC -> O(n)
def reverse_words_in_string(string: str) -> str:
    splitted_str_list = string.split()
    reverse_words_list = splitted_str_list[::-1] # reverse a list
    return " ".join(reverse_words_list)    

# TC -> O(n)
# SC -> O(n)
def reverse_words_in_string(string: str) -> str:
    n = len(string)
    temp_string = ""
    res = ""
    left = 0
    right = n-1

    while left <= right:
        char = string[left]
        if char != " ":
            temp_string += char
        else:
            if temp_string != "":
                if res != "":
                    res = temp_string + " " + res
                else:
                    res = temp_string
                temp_string = ""    
        left += 1

    if temp_string != "":
        if res != "":
            res = temp_string + " " + res
        else:
            res = temp_string

    return res        


if __name__ == "__main__":
    print(reverse_words_in_string("this is an amazing program"))