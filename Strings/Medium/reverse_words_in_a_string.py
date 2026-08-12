
# TC: O(n)
# SC: ~ O(n)
def reverse_words_in_string(s: str) -> str:
    word = ""
    words_list = []

    for i in range(len(s)):
        # If not space, add character to word.
        if s[i] != " ":
            word += s[i]
        # If space and we have collected a word.
        elif word:
            words_list.append(word)
            word = ""

    # Add the last word.
    if word:
        words_list.append(word)

    words_list.reverse()

    return " ".join(words_list)   

# TC: O(n)
# SC: O(1)
def reverse_words_in_string(s: str) -> str:
    idx = len(s)-1
    reversed_string = ""

    # Traversing in the reverse order.
    while idx >= 0:
        # Skip the spaces.
        while idx >= 0 and s[idx] == " ":
            idx -= 1

        # Check if the "idx" is out of bounds.
        if idx < 0:
            break

        # end index of a word.
        end = idx

        # Traverse until we either reach at the start of the string
        # or we found a space.
        while idx >= 0 and s[idx] != " ":
            idx -= 1

        # We found the start and end index of our string.
        # Now build our word using string slicing.
        word = s[idx+1:end+1]

        # Add space in our reversed string if our reversed string is not empty
        # i.e. we found a word and we need to insert it  but before that, we need
        # to make sure every word is separated by a single space, and we add space
        # only when our reversed string is not empty.
        if reversed_string != "":
            reversed_string += " "

        # Add our found word in our reversed string.
        reversed_string += word

    return reversed_string            



if __name__ == "__main__":
    print(reverse_words_in_string("welcome to the jungle"))
    print(reverse_words_in_string("  amazing coding  skills "))