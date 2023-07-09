1. [[Stack#[Valid Parentheses (20)](https://leetcode.com/problems/valid-parentheses/description/) |Valid Parentheses - 07/08/2023]]



---
## [Valid Parentheses (20)](https://leetcode.com/problems/valid-parentheses/description/)
###### *07/08/2023*

###### Psuedo Code
``` 
# iterate through the string
# if the current is opening, push to the stack
# if its closing, pop from the stack and current must "pair" with what value got popped
# if we make it all the way through the string and end with an empty stack, return true
```

###### Python Solution
```
def isValid(self, s: str) -> bool:
	stack = []
	pairs = {
		"{": "}",
		"[": "]",
		"(": ")",
	}

	for c in s: 
		if c in pairs:
			stack.append(c)
		else:
			if stack:
				popped = stack.pop()
				if c != pairs[popped]:
					return False
			else:
				return False

	return not stack
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