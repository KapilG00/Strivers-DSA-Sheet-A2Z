from typing import List


# TC -> O(n^2)
# SC -> O(n^2)
# def longest_sub_arr_with_given_sum(arr: List[int], k: int) -> List[int]:
#     n = len(arr)
#     res_arr = []

#     for i in range(n):
#         current_count = arr[i]
#         if current_count == k:
#             res_arr.append([arr[i]]) # It handles the special case where a single element (like arr[i]) by itself equals the target sum k.
#         for j in range(i+1, n):
#             current_count += arr[j]
#             if current_count == k:
#                 internal_arr = arr[i:j+1]
#                 res_arr.append(internal_arr)
#             elif current_count > k:
#                 break

#     max_size_of_arr = 0
#     for ele in res_arr:
#         if len(ele) > max_size_of_arr:
#             max_size_of_arr = len(ele)

#     return max_size_of_arr   


# TC -> O(n^3)
# SC -> O(1)
# def longest_sub_arr_with_given_sum(arr: List[int], k: int) -> List[int]:
#     n = len(arr)
#     max_sub_arr_length = 0

#     for i in range(n):
#         for j in range(i, n):
#             sum = 0

#             for l in range(i, j+1):
#                 sum += arr[l]

#             if sum == k:
#                 if j-i+1 > max_sub_arr_length:
#                     max_sub_arr_length = j-i+1

#     return max_sub_arr_length                  

# TC -> O(n^2)
# SC -> O(1)
# def longest_sub_arr_with_given_sum(arr: List[int], k: int) -> List[int]:
#     n = len(arr)
#     max_sub_arr_length = 0

#     for i in range(n):
#         sum = 0
#         for j in range(i, n):
#             sum += arr[j]

#             if sum == k:
#                 if j-i+1 > max_sub_arr_length:
#                     max_sub_arr_length = j-i+1

#     return max_sub_arr_length



# TC -> O(nlogn)
# SC -> O(n)
# Using hashing.
# def longest_sub_arr_with_given_sum(arr: List[int], k: int) -> List[int]:
#     """This will work only if an array consists of only positive elements."""
#     n = len(arr)
#     sum_map = {}
#     sum = 0
#     max_length = 0

#     for i in range(n):
#         sum += arr[i]
#         if sum == k:
#             max_length = max(max_length, i+1)
#         prefix_sum = sum - k
#         if prefix_sum in sum_map:
#             length = i - sum_map[prefix_sum]
#             max_length = max(max_length, length)
#         sum_map[sum] = i

#     return max_length


# TC -> O(nlogn)
# SC -> O(n)
# Using 2-pointers.
def longest_sub_arr_with_given_sum(arr: List[int], k: int) -> List[int]:
    pass




if __name__ == "__main__":
    # print(longest_sub_arr_with_given_sum([2,3,5,1,9], 10))
    # print(longest_sub_arr_with_given_sum([2,3,5], 5))
    # print(longest_sub_arr_with_given_sum([2,3,5], 2))
    print(longest_sub_arr_with_given_sum([1,2,3,1,1,1,1], 3))