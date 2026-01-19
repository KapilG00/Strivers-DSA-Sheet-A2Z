from typing import List


def check_isomorphic_string(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    str1_to_str2_mapping = {}
    str2_to_str1_mapping = {}

    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        
        if ((c1 in str1_to_str2_mapping and str1_to_str2_mapping[c1] != c2)
        or (c2 in str2_to_str1_mapping and str2_to_str1_mapping[c2] != c1)):
            return False
         
        str1_to_str2_mapping[c1] = c2
        str2_to_str1_mapping[c2] = c1
    
    return True




if __name__ == "__main__":
    print(check_isomorphic_string("paper", "title"))
    print(check_isomorphic_string("foo", "bar"))
