"""Print all possible subsequences of a string."""


def power_set(s: str, subsequences_list: list[str], subsequence_str: str, idx: int) -> list[str]:
    n = len(s)
    
    # Base case
    if idx == n:
        if subsequence_str:
            subsequences_list.append(subsequence_str)
        return    

    # Take
    power_set(s, subsequences_list, subsequence_str+s[idx], idx+1)
    
    # Not take
    power_set(s, subsequences_list, subsequence_str, idx+1)

    return subsequences_list




if __name__ == "__main__":
    print(power_set("abc", [], "", 0))
