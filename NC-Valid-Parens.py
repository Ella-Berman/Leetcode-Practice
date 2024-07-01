class Solution:
  def isValid(self, s: str) -> bool:
      if not s:
          return True

      parens = {"}":"{", ")":"(", "]":"[",}

      stack = []

      for char in s:
          if char in parens.values():
              stack.append(char)
          else:
              # handle empty stack
              open = stack.pop() if stack else " "
              if parens.get(char) is not open:
                  return False

      if stack:
          return False
      else:
          return True