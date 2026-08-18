from typing import List


# TC: O(2^n)
# SC: O(len(binary_strings_arr)); if we consider recursive call stack space then O(n*len(binary_strings_arr))
def generate_all_binary_strings(n: int, binary_strings_arr: List[str], binary_string: str) -> List[str]:
    # Base case
    if len(binary_string) == n:
        binary_strings_arr.append(binary_string)
        return

    generate_all_binary_strings(n, binary_strings_arr, binary_string + "0")

    if not binary_string or binary_string[-1] != "1":
        generate_all_binary_strings(n, binary_strings_arr, binary_string + "1")

    return binary_strings_arr

        

if __name__ == "__main__":
    print(generate_all_binary_strings(3, [], ""))
    print(generate_all_binary_strings(2, [], ""))   