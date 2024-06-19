# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return True if the string matches the given abbreviation. Return False otherwise.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example  #1:
# Input: word = "internationalization", abbr = "i12iz4n"
# Expected Output: True
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

# Example #2:
# Input: word = "apple", abbr = "a2e"
# Expected Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".

# 1) Initialize two pointers, word_ptr and abbr_ptr, to 0.
# 2) While both pointers are within the bounds of their respective strings:
#     a) If the current character in abbr is a digit:
#         i) Check for leading zeros and return False if present.
#         ii) Convert the digit(s) to a number and move word_ptr forward by that number.
#     b) If the current character in abbr is not a digit:
#         i) Compare the character in word with the character in abbr.
#         ii) If they do not match, return False.
#     c) Move both pointers forward.
# 3) Return True if both pointers have reached the end of their respective strings; otherwise, return False.


def valid_word_abbreviation(word, abbr):
    word_ptr = 0
    abbr_ptr = 0
    word_len = len(word)
    abbr_len = len(abbr)

    while abbr_ptr < abbr_len and word_ptr < word_len:
        if abbr[abbr_ptr].isdigit():
            if abbr[abbr_ptr] == '0':
                return False  # Leading zeros are not allowed
            num = 0
            while abbr_ptr < abbr_len and abbr[abbr_ptr].isdigit():
                num = num * 10 + int(abbr[abbr_ptr])
                abbr_ptr += 1
            word_ptr += num
        else:
            if word[word_ptr] != abbr[abbr_ptr]:
                return False
            word_ptr += 1
            abbr_ptr += 1

    return word_ptr == word_len and abbr_ptr == abbr_len

# Assume N represents the length of the word and M represents the length of the abbreviation.

# Time Complexity: O(N + M) because we need to traverse both the word and the abbreviation.
# Space Complexity: O(1) because we only use a constant amount of extra space.
            