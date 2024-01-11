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
- [x] [[Trees#[Validate Binary Search Tree (98)](https://leetcode.com/problems/validate-binary-search-tree/description/) |Validate Binary Search Tree - 08/27/2023]]
- [x] [[Trees#[Range Sum of BST (938)](https://leetcode.com/problems/range-sum-of-bst/) |Range Sum of BST - 01/07/2024]]
- [x] [[Trees#[Leaf-Similar Trees (872)](https://leetcode.com/problems/leaf-similar-trees/) |Leaf-Similar Trees - 01/08/2024]]
- [x] [[Trees#[Amount of Time for Binary Tree to be Infected (2385)](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/) |Amount of Time for Binary Tree to be Infected - 01/09/2024]]
- [x] [[Trees#[Maximum Difference Between Node and Ancestor (1026)](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/) |Maximum Difference Between Node and Ancestor - 01/10/2024]]



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
## [Validate Binary Search Tree (98)](https://leetcode.com/problems/validate-binary-search-tree/description/)
###### *08/27/2023*

###### Psuedo Code
``` 
# conditions: min_val < node < max_val
# dfs, ensure each node satisfies conditions
```

###### Python Solution
```python
def isValidBST(self, root: Optional[TreeNode]) -> bool:
	return self.dfs(root, float('-inf'), float('inf'))

def dfs(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
	if not node:
		return True
		
	if node.val <= min_val or node.val >= max_val:
		return False

	return self.dfs(node.left, min_val, node.val) and self.dfs(node.right, node.val, max_val)


########################################################################


def isValidBST(self, root: Optional[TreeNode]) -> bool:
	if not root: 
		return True
	
	stack = []
	stack.append((root, float('-inf'), float('inf')))

	while stack:
		curr, min_val, max_val = stack.pop()

		if curr.val <= min_val or curr.val >= max_val:
			return False

		if curr.left:
			stack.append((curr.left, min_val, curr.val))
		if curr.right:
			stack.append((curr.right, curr.val, max_val))
	
	return True
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
## [Range Sum of BST (938)](https://leetcode.com/problems/range-sum-of-bst/)
###### *01/07/2024*

###### Psuedo Code
``` 
# dfs + check for range
```

###### Python Solution
```python
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
	if not root:
		return 0

	stack = [root]
	range_sum = 0

	while stack:
		curr = stack.pop()
		if low <= curr.val <= high:
			range_sum += curr.val
		if curr.left:
			stack.append(curr.left) 
		if curr.right:
			stack.append(curr.right) 

	return range_sum
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
## [Leaf-Similar Trees (872)](https://leetcode.com/problems/leaf-similar-trees/)
###### *01/08/2024*

###### Psuedo Code
``` 
# helper function, dfs, returns set of sequence
```

###### Python Solution
```python
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
	def buildLeafValueSeq(root):
		seq = []
		stack = [root]

		while stack:
			curr = stack.pop()

			if not curr.left and not curr.right:
				seq.append(curr.val)

			if curr.left:
				stack.append(curr.left)

			if curr.right:
				stack.append(curr.right)

		return seq

	one = buildLeafValueSeq(root1)
	two = buildLeafValueSeq(root2)

	return one == two
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
## [Amount of Time for Binary Tree to be Infected (2385)](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/)
###### *01/09/2024*

###### Psuedo Code
``` 
# build a graph, adj list, then dfs starting at start to find maximum depth

```

###### Python Solution
```python
def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
	max_depth = 0

	adj = self.buildAdjList(root)
	stack = [(start, 0)]
	visited = set()
	print(adj)

	while stack:
		curr = stack.pop()
		val, depth = curr
		
		visited.add(val)
		max_depth = max(max_depth, depth)

		print(val)
		for neighbor in adj[val]:
			if neighbor in visited:
				continue
			stack.append((neighbor, depth+1))

	return max_depth
	
def buildAdjList(self, root: Optional[TreeNode]) -> dict:
	adj = {}

	stack = [root]
	while stack:
		curr = stack.pop()

		if curr.val not in adj:
			adj[curr.val] = []

		if curr.left:
			adj[curr.val].append(curr.left.val)
			if curr.left.val not in adj:
				adj[curr.left.val] = []
			adj[curr.left.val].append(curr.val)
			stack.append(curr.left)

		if curr.right:
			adj[curr.val].append(curr.right.val)
			if curr.right.val not in adj:
				adj[curr.right.val] = []
			adj[curr.right.val].append(curr.val)
			stack.append(curr.right)

	return adj

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
## [Maximum Difference Between Node and Ancestor (1026)](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/)
###### *01/10/2024*

###### Psuedo Code
``` 
# dfs, passing high and low values to each node, update high and low as we traverse and update max_depth as well
```

###### Python Solution
```python
def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
	if not root:
		return 0

	stack = [(root, root.val, root.val)] # node, high, low
	max_depth = 0

	while stack:
		node, high, low = stack.pop()
		max_depth = max(max_depth, abs(high-node.val), abs(low-node.val))
		
		if node.left:
			stack.append((node.left, max(high, node.val), min(low, node.val)))

		if node.right:
			stack.append((node.right, max(high, node.val), min(low, node.val)))

	return max_depth
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
