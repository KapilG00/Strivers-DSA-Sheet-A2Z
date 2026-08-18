from typing import List


# TC: O(Cn*n); where Cn is a catalan number
# Formula: Cn = C0Cn-1 + C1Cn-2 + .... + Cn-1C0
# SC: O(len(parantheses_array)); if we consider recursive call stack space then O(n*len(parantheses_array))
def generate_parantheses(n: int, parantheses_array: List[str], parantheses_string: str, open_braces_count: int, close_braces_count: int) -> List[str]:
    # base case
    if len(parantheses_string) == 2*n:
        parantheses_array.append(parantheses_string)
        return

    if open_braces_count < n:
        generate_parantheses(n, parantheses_array, parantheses_string + "(", open_braces_count+1, close_braces_count)

    if close_braces_count < open_braces_count:
        generate_parantheses(n, parantheses_array, parantheses_string + ")", open_braces_count, close_braces_count+1)    

    return parantheses_array



if __name__ == "__main__":
    print(generate_parantheses(3, [], "", 0, 0))