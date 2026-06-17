from typing import List

def func(arr: List[str]) -> str:
    result = []

    arr.sort()

    first_ele = arr[0]
    last_ele = arr[-1]
    
    for i in range(min(len(first_ele), len(last_ele))):
        if first_ele[i] != last_ele[i]:
            return "".join(result)
        result.append(first_ele[i])
        print("Result: ", result)

    return "".join(result)    




if __name__ == "__main__":
    print(func(["flower", "flow", "flight"]))
    print(func(["apple", "banana", "grape", "mango"]))