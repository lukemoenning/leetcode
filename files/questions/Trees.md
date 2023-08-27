- [ ] Done with help 
- [x] Done on own

- [ ] [[Trees#[Invert Binary Tree (226)](https://leetcode.com/problems/invert-binary-tree/description/) |Invert Binary Tree - 08/04/2023]]
- [ ] [[Trees#[Maximum Depth of Binary Tree (104)](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) |Maximum Depth of Binary Tree - 08/04/2023]]
- [ ] [[Trees#[Diameter of Binary Tree (543)](https://leetcode.com/problems/diameter-of-binary-tree/description/) |Diameter of Binary Tree - 08/05/2023]]
- [ ] [[Trees#[Same Tree (100)](https://leetcode.com/problems/same-tree/) |Same Tree - 08/09/2023]]
- [ ] [[Trees#[Subtree of Another Tree (572)](https://leetcode.com/problems/subtree-of-another-tree/description/) |Subtree of Another Tree - 08/12/2023]]
- [ ] [[Trees#[Lowest Common Ancestor of a Binary Search Tree (235)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/) |Lowest Common Ancestor of a Binary Search Tree - 08/23/2023]]
- [ ] [[Trees#[Binary Tree Level Order Traversal (102)](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) |Binary Tree Level Order Traversal - 08/26/2023]]
- [ ] [[Trees#[Binary Tree Right Side View (199)](https://leetcode.com/problems/binary-tree-right-side-view/description/) |Binary Tree Right Side View - 08/26/2023]]
- [ ] [[Trees#[Count Good Nodes in Binary Tree (1448)](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/) |Count Good Nodes in Binary Tree - 08/26/2023]]



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
## [Diameter of Binary Tree (543)](https://leetcode.com/problems/diameter-of-binary-tree/description/)
###### *08/05/2023*

###### Psuedo Code
``` 
# dfs
# the longest path has to be between two leaf nodes
# which means the maxium path for a current node is the max depth of left plus max depth of right, do for every node and keep track of overall max diameter 
```

###### Python Solution
```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
	diameter = 0

	def helper(node: Optional[TreeNode]) -> int:
		nonlocal diameter
		if node == None:
			return 0
		
		left = helper(node.left)
		right = helper(node.right)
		
		diameter = max(diameter, left+right)
		return max(left, right) + 1

	helper(root)
	return diameter
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
## [Same Tree (100)](https://leetcode.com/problems/same-tree/)
###### *08/09/2023*

###### Psuedo Code
``` 
# check that each corresponding node exists and has the same value
```

###### Python Solution
```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
	if not p and not q:
		return True  

	if p and q and p.val == q.val:
		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  
	
	return False
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(n)
```


---
## [Subtree of Another Tree (572)](https://leetcode.com/problems/subtree-of-another-tree/description/)
###### *08/12/2023*

###### Psuedo Code
``` 
# dfs on the root, call same tree on root and subRoot
```

###### Python Solution
```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
	if not root: 
		return False
	
	if self.sameTree(root, subRoot):
		return True
		
	return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
	if not p and not q: 
		return True

	if p and q and p.val == q.val:
		return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

	return False
```

###### Runtime Complexity
```
O(n*m)
```

###### Space Complexity
```
O(n+m)
```


---
## [Lowest Common Ancestor of a Binary Search Tree (235)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
###### *08/23/2023*

###### Psuedo Code
``` 
# we know that since it is a BST, we can do binary search for val
# if both p and q are on in the same subtree, search that subtree
# if p and q are in separate subtrees, one left and one right, return curr
```

###### Python Solution
```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	if root is None: 
		return None

	curr = root
	while curr:
		if p.val < curr.val and q.val < curr.val:
			curr = curr.left
		elif p.val > curr.val and q.val > curr.val:
			curr = curr.right
		else:
			return curr
	
	return None
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
## [Binary Tree Level Order Traversal (102)](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
###### *08/26/2023*

###### Psuedo Code
``` 
# bfs, only pop one level at a time
```

###### Python Solution
```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	if not root:
		return None

	q = deque()
	res = []
	q.append(root)

	while q:
		l = len(q)
		curr_list = []
		for i in range(l):
			node = q.popleft()
			if node:
				curr_list.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
		res.append(curr_list)

	return res
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(n)
```


---
## [Binary Tree Right Side View (199)](https://leetcode.com/problems/binary-tree-right-side-view/description/)
###### *08/26/2023*

###### Psuedo Code
``` 
# for every level of a bfs search, append the right most value
```

###### Python Solution
```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return None

	q = deque()
	q.append(root)
	res = []

	while q:
		l = len(q)
		for i in range(l):
			node = q.popleft()
			if node and i == l-1:
				res.append(node.val)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		
	
	return res
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
## [Count Good Nodes in Binary Tree (1448)](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)
###### *08/26/2023*

###### Psuedo Code
``` 
# dfs, for each node, keep track of a max_seen
# if the current is greater than the max, increment good
```

###### Python Solution
```python
def goodNodes(self, root: TreeNode) -> int:
	if not root:
		return None

	good_count = 0
	dfs = []
	dfs.append((root, float('-inf')))

	while dfs:
		node, max_seen = dfs.pop()
		if node.val >= max_seen:
			good_count += 1
			max_seen = node.val
		if node.left:
			dfs.append((node.left, max_seen))
		if node.right:
			dfs.append((node.right, max_seen))
		

	return good_count
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(n)
```


---