1. [[Two Pointers#[Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/description/) |Valid Palindrome - 04/09/2023]]
2. [[Two Pointers#[Two Sum II - Input Array is Sorted (167)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) ||Two Sum II - 04/16/2023]]



___
## [Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/description/)
###### *04/09/2023*

###### Psuedo Code
``` 
# Two pointers, left and right, one at the beginning and one at the end
    # While left < right
        # Increment/decrement each pointer until they reach an alphanumeric value
        # If s[left] not s[right]
            # Return false
        # Increment left and decrement right
```

###### Python Solution
```
def isPalindrome(self, s: str) -> bool:
	left = 0
	right = len(s)-1

	while left < right:
		while not s[left].isalnum() and left<right:
			left+=1
	
		while not s[right].isalnum() and left<right:
			right-=1
	
		if s[left].lower() != s[right].lower():
			return False
	
		left+=1
		right-=1
	
	return True
```

###### Runtime Complexity
```
O(N)
```

###### Space Complexity
```
O(1)
```

---
## [Two Sum II - Input Array is Sorted (167)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
###### *04/16/2023*

###### Psuedo Code
``` 
    # two pointers, one at the start and the other at the end
    # three cases: if the sum of the two 
        # equals the target, return them
        # less than the target, increment left pointer
        # greater than the target, decrement right pointer
```

###### Python Solution
```
def twoSum(self, numbers: List[int], target: int) -> List[int]:
	left_pointer = 0 
	right_pointer = len(numbers)-1
	while left_pointer < right_pointer:
		nums_sum = numbers[left_pointer]+numbers[right_pointer]

		if nums_sum == target:
			return [left_pointer+1, right_pointer+1]
		elif nums_sum < target:
			left_pointer+=1
		else:
			right_pointer-=1
```

###### Runtime Complexity
```
O(N)
```

###### Space Complexity
```
O(N)
```

---