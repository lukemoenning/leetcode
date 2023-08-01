- [ ] Done with help 
- [x] Done on own

- [ ] [[Linked List#[Reorder List (143)](https://leetcode.com/problems/reorder-list/description/)|Reorder List - 07/19/2023]]
- [x] [[Linked List#[Reverse Linked List (206)](https://leetcode.com/problems/reverse-linked-list/description/) |Reverse Linked List - 07/30/2023]]
- [ ] [[Linked List#[Merge Two Sorted Lists (21)](https://leetcode.com/problems/merge-two-sorted-lists/description/) |Merge Two Sorted Lists - 07/31/2023]]
- [x] [[Linked List#[Linked List Cycle (141)](https://leetcode.com/problems/linked-list-cycle/description/) |Linked List Cycle - 07/31/2023]]



---
## [Reorder List (143)](https://leetcode.com/problems/reorder-list/description/)
###### *07/19/2023*

###### Psuedo Code
``` 
# find the middle
# reverse the second half
# "zip" the two new halves together
```

###### Python Solution
```python
def reorderList(self, head: Optional[ListNode]) -> None:
	"""
	Do not return anything, modify head in-place instead.
	"""
	if not head or not head.next:
		return 

	midpoint = self.findMid(head)
	half = self.reverseLL(midpoint)
	self.zipLL(head, half)

def findMid(self, head: Optional[ListNode]) -> ListNode:
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	mid = slow.next
	slow.next = None
	return mid

def reverseLL(self, head: Optional[ListNode]) -> ListNode:
	prev = None
	current = head
	while current:
		temp = current.next
		current.next = prev
		prev = current
		current = temp
	return prev

def zipLL(self, left: ListNode, right: ListNode) -> None:
	while left and right:
		temp_left = left.next
		temp_right = right.next
		left.next = right
		right.next = temp_left
		left = temp_left
		right = temp_right
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(1)
```


---
## [Reverse Linked List (206)](https://leetcode.com/problems/reverse-linked-list/description/)
###### *07/30/2023*

###### Psuedo Code
``` 
# use a current a prev tracker
# point current to previous for each node in the list
```

###### Python Solution
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
	if not head:
		return None

	current = head
	prev = None
	while current:
		temp = current.next
		current.next = prev
		prev = current
		current = temp

	return prev
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(1)
```


---
## [Merge Two Sorted Lists (21)](https://leetcode.com/problems/merge-two-sorted-lists/description/)
###### *07/31/2023*

###### Psuedo Code
``` 
# brute force, iterate through both adding smaller to a new list
# optimized space, create a header pointer and previous pointer, iterate through and set prev.next to the smallest then increment the smallest, make sure to append the rest of the longer list to the end
```

###### Python Solution
```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

	head_pointer = ListNode()
	prev = head_pointer

	while list1 and list2:
		if list1.val < list2.val:
			prev.next = list1
			prev = list1
			list1 = list1.next

		else:
			prev.next = list2
			prev = list2
			list2 = list2.next

	if list1:
		prev.next = list1
	if list2:
		prev.next = list2

	return head_pointer.next
```

###### Runtime Complexity
```
O(n+m)
```

###### Space Complexity
```
O(1)
```


---
## [Linked List Cycle (141)](https://leetcode.com/problems/linked-list-cycle/description/)
###### *07/31/2023*

###### Psuedo Code
``` 
    # brute force, add each node to a set, if the current node is already in the set we have a cycle
    # optimized space with floyd's cycle finding algorithm, fast and slow pointer
```

###### Python Solution
```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
	if not head:
		return False

	slow = head
	fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if slow == fast:
			return True
	
	return False
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(1)
```


---