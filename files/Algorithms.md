
## Sorting Algorithms
- [[Algorithms#Quicksort |QuickSort]]
- [[Algorithms#Binary Search Tree |Binary Search Tree]]



--- 
## QuickSort

###### Algorithm Breakdown
``` 
Divide and Conquer recurisive alogrithm

1. Pick a partition: most commonly the last index.
2. Seperate all values less than that partition on the left and all values greater on the right
3. Place the partition in its sorted place
4. Repeat for the values left of the current partition and right of the current partition
```

###### Runtime Complexity
```
Worse Case: O(N^2)
Average Case: O(NlogN)
```

###### Space Complexity
```
O(1) becuase it is an in-place sort
```

###### Code
```python
def partition(array, low, high):
	pivot = array[high]
	
	greater_element = low - 1
	
	for i in range(low, high):
		if array[i] <= pivot:
			greater_element = greater_element + 1
			
			(array[greater_element], array[i]) = (array[i], array[greater_element])
	
	(array[greater_element + 1], array[high]) = (array[high], array[greater_element + 1])
	
	return greater_element+1

def quickSort(array, low, high):
	partition_index = partition(array, low, high)
	
	quickSort(array, low, partition_index-1)
	quickSort(array, partition_index + 1, high)
```



---
## Binary Search Tree

###### Algorithm Breakdown
``` 
Keep track of min and max a node can be, perform a dfs of the tree and make sure each node value is within its bounds

```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(n)
```

###### Code
```python
def helper(node, min=float('-inf'), max=float('inf')):
	if not node:
		return True
		
	if not min < node.value < max:
		return False
	
	return helper(node.left, min, node.value) and helper(node.right, node.value, max)
		
		
return helper(t)
```



---
