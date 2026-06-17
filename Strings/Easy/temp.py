

def func(s: str) -> str:
    # str_int = int(s)
    idx = -1
    n = len(s)

    for i in range(n-1,-1,-1):
        if (int(s[i]) % 2) == 1:
            idx = i
            break

    j = 0

    while j <= idx and s[j] == "0":
        j += 1

    return s[j:idx+1]        



if __name__ == "__main__":
    print(func("5347"))
    print(func("0214638"))
    print(func("00138"))