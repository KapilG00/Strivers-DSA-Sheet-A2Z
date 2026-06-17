
# def func(s1: str, s2: str) -> bool:
#     n, m = len(s1), len(s2)
#     hashmap_1_2 = {}
#     hashmap_2_1 = {}
#     is_isomorphic = True

#     for i in range(n):
#         char1 = s1[i] 
#         char2 = s2[i]

#         if (char1 in hashmap_1_2 and hashmap_1_2[char1] != char2) or \
#            (char2 in hashmap_2_1 and hashmap_2_1[char2] != char1):
#             is_isomorphic = False
#             break

#         hashmap_1_2[s1[i]] = s2[i]
#         hashmap_2_1[s2[i]] = s1[i]    

#     return is_isomorphic        

def check_isomorphic_string(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    char_map_1 = [0] * 256
    char_map_2 = [0] * 256

    for i in range(len(str1)):
        if char_map_1[ord(str1[i])] != char_map_2[ord(str2[i])]:
            return False

        char_map_1[ord(str1[i])] = i+1
        char_map_2[ord(str2[i])] = i+1
        print("char map 1: ", char_map_1)
        print("char map 2: ", char_map_2)
        print()    

    return True


if __name__ == "__main__":
    print(check_isomorphic_string("paper", "title"))



# if __name__ == "__main__":
#     print(func("paper", "title"))
#     print(func("foo", "bar"))
#     print(func("ab", "aa"))