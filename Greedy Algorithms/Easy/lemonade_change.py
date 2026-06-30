from typing import List


# TC -> O(n)
# SC -> O(1)
def lemonade_change(bills: List[int]) -> bool:
    counter_5, counter_10 = 0, 0

    for bill in bills:
        if bill == 5:
            counter_5 += 1
        elif bill == 10:
            if counter_5 > 0:
                counter_5 -= 1
                counter_10 += 1
            else:
                return False
        else:
            if counter_5 > 0 and counter_10 > 0:
                counter_5 -= 1
                counter_10 -= 1
            elif counter_5 >= 3:
                counter_5 -= 3
            else:
                return False        

    return True
           
  
 
if __name__ == "__main__":
    print(lemonade_change([5, 5, 5, 10, 20]))
    print(lemonade_change([5, 5, 10, 10, 20]))