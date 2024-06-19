# Given the heads of two singly linked lists of integers, merge their nodes to make one list, taking nodes alternately between the two lists. If either list runs out of elements before the other, all nodes from the list with remaining nodes should be appended onto the end of the merged list. Return the head of the merged list.

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
# Input: head_a = 1, head_b = 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 3

def shuffle_merge(head_a, head_b):
  # handle empty lists
  if not head_a:
    return head_b
  elif not head_b:
    return head_a

  # Initialize the merged list with the first node of list A
  merged_head = head_a
  cur_a = head_a.next
  cur_b = head_b
  cur_merged = merged_head

  # Alternate appending nodes from each list
  chooseB = True
  while cur_a and cur_b:
    if chooseB:
      cur_merged.next = cur_b
      cur_b = cur_b.next
    else:
      cur_merged.next = cur_a
      cur_a = cur_a.next
    cur_merged = cur_merged.next
    chooseB = not chooseB # Switch between List A and List B

  # Append the remaining nodes from either list
  cur_merged.next = cur_a if cur_a else cur_b

  return merged_head

  

