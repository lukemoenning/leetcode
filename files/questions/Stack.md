1. [[Stack#[Valid Parentheses (20)](https://leetcode.com/problems/valid-parentheses/description/) |Valid Parentheses - 07/08/2023]]
2. [[Stack#[Evaluate Reverse Polish Notation (150)](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) |valuate Reverse Polish Notation - 07/13/2023]]



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
## [Evaluate Reverse Polish Notation (150)](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
###### *07/13/2023*

###### Psuedo Code
``` 
# iterate through the list
# if we hit a number add it to a stack
# if we hit an operation pop two from the stack and make the computation
```

###### Python Solution
```python
def evalRPN(self, tokens: List[str]) -> int:
	stack = []

	for token in tokens:
		if token not in '+-*/':
			stack.append(int(token))
		else:
			second_num = stack.pop()
			if not stack:
				return second_num

			first_num = stack.pop()
			if token == '+':
				stack.append(first_num+second_num)
			elif token == '-':
				stack.append(first_num-second_num)
			elif token == '*':
				stack.append(first_num*second_num)
			else:
				stack.append(int(first_num/second_num))


	return stack.pop()
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