- [ ] Done with help 
- [x] Done on own

- [ ] [[Trees#[Invert Binary Tree (226)](https://leetcode.com/problems/invert-binary-tree/description/) |Invert Binary Tree - 08/04/2023]]
- [ ] [[Trees#[Maximum Depth of Binary Tree (104)](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) |Maximum Depth of Binary Tree - 08/04/2023]]



---
## [Invert Binary Tree (226)](https://leetcode.com/problems/invert-binary-tree/description/)
###### *08/04/2023*

###### Psuedo Code
``` 
# recursively iterate through the tree
# as we swap parent brings children, so we just have to treat each new subtree as its own swap
```

###### Python Solution
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
	if root == None:
		return None
	
	temp = root.right
	root.right = root.left
	root.left = temp

	self.invertTree(root.left)
	self.invertTree(root.right)
	
	return root
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(height) = O(n)
```


---
## [Maximum Depth of Binary Tree (104)](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)
###### *08/04/2023*

###### Psuedo Code
``` 
# recursive compare the current max depth vs the depth of the current
```

###### Python Solution
```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
	if root == None:
		return 0

	left = self.maxDepth(root.left)
	right = self.maxDepth(root.right)

	return max(left, right) + 1

```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(height) = O(n)
```


---