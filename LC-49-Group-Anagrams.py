# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# strs[i] consists of lowercase English letters.


# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Method: create a dictionary where the keys are the sorted versions of words in the list and
# each value is a list of words that, when sorted, match the key.

#def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
def groupAnagrams(strs):
  sorted_dict = {}
  for word in strs:
      word_key = "".join(sorted(word))
      if sorted_dict.get(word_key):
          sorted_dict[word_key].extend([word])
      else:
          sorted_dict[word_key] = [word]

  output = []

  for key in sorted_dict:
      output.append(sorted_dict.get(key))

# # Alternate syntax for above
# for key, value in sorted_dict.items():
#     output.append(value)

  return output