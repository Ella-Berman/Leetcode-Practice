# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

# Example #1:
# Input: s = "()"
# Expected Output: True

# Example #2:
# s = "()[]{}"
# Expected Output: True

# Example #3: 
# s = "(())"
# Expected Output: True

# Example #4:
# s = "(]"
# Expected Output: False

# Method: Use a stack and a dictionary
# Note: handle popping from empty stack
def isValid(self, s: str) -> bool:
  if not s:
      return True

  stack = []
  bracket_dict = {")":"(", "]":"[", "}":"{"}

  for char in s:
      if char in bracket_dict.values():
          stack.append(char)
      elif char in bracket_dict.keys():
          open = stack.pop() if stack else "#"
          if bracket_dict[char] != open:
              return False
      else: 
          return False

  return not stack
  
  

