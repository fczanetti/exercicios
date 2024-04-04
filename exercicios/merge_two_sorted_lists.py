# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
# Return the head of the merged linked list.

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


l1 = [1, 2, 4, 18]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = []


def merge_lists(list1, list2):
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] <= l2[0]:
            l3.append(l1.pop(0))
        else:
            l3.append(l2.pop(0))
    if len(l1) > 0:
        l3.extend(l1)
    elif len(l2) > 0:
        l3.extend(l2)
    return l3


if __name__ == '__main__':
    print(merge_lists(l1, l2))
