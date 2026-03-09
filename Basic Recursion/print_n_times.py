def print_n_times(quote: str, num: int, print_times: int) -> int:
    if num == print_times:
        return 1
    
    print(quote)
    
    print_n_times(quote, num+1, print_times)



if __name__ == "__main__":
    quote = "Some people dont think simple enough!!"
    print(print_n_times(quote, 0, 4))