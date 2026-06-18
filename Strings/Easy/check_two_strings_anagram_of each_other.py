# TC ->  O(n)
# SC -> O(k); here "k" is number of distinct characters.
# Brute-force approach.
def check_anagrams(str1: str, str2: str) -> bool:
    n, m = len(str1), len(str2)

    if n != m:
        return False

    hash_map_str1 = {}
    hash_map_str2 = {}

    for i in range(n):
        if str1[i] not in hash_map_str1:
            hash_map_str1[str1[i]] = 1
        else:
            hash_map_str1[str1[i]] += 1    

    for j in range(m):
        if str2[j] not in hash_map_str2:
            hash_map_str2[str2[j]] = 1
        else:
            hash_map_str2[str2[j]] += 1

    if hash_map_str1 == hash_map_str2:
        return True

    return False

# TC ->  O(nlogn)
# SC -> O(n)
# Brute-force approach.
def check_anagrams(str1: str, str2: str) -> bool:
    n, m = len(str1), len(str2)

    if n != m:
        return False
    
    sorted_str1_list = sorted(str1)
    sorted_str2_list = sorted(str2)

    for i in range(len(sorted_str1_list)):
        if sorted_str1_list[i] != sorted_str2_list[i]:
            return False
    
    return True

# TC ->  O(n)
# SC -> O(1)
# Optimal approach.
def check_anagrams(str1: str, str2: str) -> bool:
    n, m = len(str1), len(str2)

    if n != m:
        return False
    
    freq = [0] * 26

    for ele1 in str1:
        freq[ord(ele1) - ord('A')] += 1

    for ele2 in str2:
        freq[ord(ele2) - ord('A')] -= 1 

    for count in freq:
        if count != 0:
            return False

    return True    


if __name__ == "__main__":
    print(check_anagrams("CAT", "ACT"))
    print(check_anagrams("RULES", "LESRT"))