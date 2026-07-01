from typing import List


# TC -> O(n*logn + m*logm), Both the arrays are sorted in increasing order.
# SC -> O(1)
# Optimal approach
def assign_cookies(students: List[int], cookies: List[int]) -> int:
    students.sort()
    cookies.sort()

    studentIndex = 0
    cookieIndex = 0

    # Try to assign cookies until any one list is fully processed
    while studentIndex < len(students) and cookieIndex < len(cookies):
        # If the cookie satisfies the student's greed
        if cookies[cookieIndex] >= students[studentIndex]:
            studentIndex += 1
        # Move to next cookie in both cases
        cookieIndex += 1

    # Number of students satisfied is equal to studentIndex
    return studentIndex        

           
  
 
   

if __name__ == "__main__":
    print(assign_cookies([1,2,3], [1,1]))
    print(assign_cookies([1,2], [1,2,3]))
    print(assign_cookies([1,2], [2]))
    print(assign_cookies([2,2,3], [1,1]))