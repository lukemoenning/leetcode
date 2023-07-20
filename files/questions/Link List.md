- [ ] [[Link List#[Reorder List (143)](https://leetcode.com/problems/reorder-list/description/) |Reorder List - 07/19/2023]]



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

---## [Reorder List (143)](https://leetcode.com/problems/reorder-list/description/)
###### *07/19/2023*

###### Psuedo Code
``` 

```

###### Python Solution
```python

```

###### Runtime Complexity
```
O(_)
```

###### Space Complexity
```
O(_)
```

---