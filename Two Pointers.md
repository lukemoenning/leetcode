1. [[Two Pointers#[Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/description/) |Valid Palindrome - 04/09/2023]]



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
