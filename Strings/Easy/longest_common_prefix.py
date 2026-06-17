

def longest_common_prefix(string_arr: str) -> str:
    longest_common_prefix_str = ""
    string_arr.sort()
    n = len(string_arr)

    for i in range(min(len(string_arr[0]), len(string_arr[n-1]))):
        if string_arr[0][i] == string_arr[n-1][i]:
            longest_common_prefix_str += string_arr[0][i]
        
    return longest_common_prefix_str

        
if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"])) 
    print(longest_common_prefix(["interview", "internet", "internal", "interval"]))
    print(longest_common_prefix(["dendi", "miracle", "puppey", "notail"]))
