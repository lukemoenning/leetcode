- [ ] Done with help 
- [x] Done on own

- [ ] [[Stack#[Valid Parentheses (20)](https://leetcode.com/problems/valid-parentheses/description/) |Valid Parentheses - 07/08/2023]]
- [ ] [[Stack#[Evaluate Reverse Polish Notation (150)](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) |Evaluate Reverse Polish Notation - 07/13/2023]]
- [ ] [[Stack#[Daily Temperatures (793)](https://leetcode.com/problems/daily-temperatures/description/) |Daily Temperatures - 07/13/2023]]
- [ ] [[Stack#[Car Fleet (853)](https://leetcode.com/problems/car-fleet/description/) |Car Fleet - 07/14/2023]]



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
```python
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
## [Daily Temperatures (793)](https://leetcode.com/problems/daily-temperatures/description/) 
###### *07/13/2023*

###### Psuedo Code
``` 
# iterate through temps
# if a stack is empty, apend temp, index to stack
# while current temp greater than top stack, pop and apend current index - top stack index to top stack index
```

###### Python Solution
```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
	result = [0] * len(temperatures)
	stack = []

	for index, temp in enumerate(temperatures):
		if not stack:
			stack.append((temp, index))
		else:
			while stack and temp > stack[-1][0]:
				popped_temp, popped_index = stack.pop()
				result[popped_index] = index-popped_index
			stack.append((temp, index))
			
	return result
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
## [Car Fleet (853)](https://leetcode.com/problems/car-fleet/description/)
###### *07/14/2023*

###### Psuedo Code
``` 
# sort the cars by postion and speed, the first car will be a fleet so add its arrival time to a stack
# for the rest of the cars, calculate the project arrival time, if its faster that top stack it joins the fleet in front
# if its slower it starts its own fleet so we append it to stack
# return the len of stack 
```

###### Python Solution
```python
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
	fleets = []
	cars = sorted(zip(position, speed))[::-1]
	for car in cars:
		pos, speed = car
		arrival_time = (target - pos) / speed # speed*time + postion = target
		if not fleets:
			fleets.append(arrival_time)
		else: 
			if arrival_time > fleets[-1]:
				fleets.append(arrival_time)
	return len(fleets)
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