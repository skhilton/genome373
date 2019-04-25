---
title: Quiz Section 4
author: trees, while loops, and functions
date: 2019-04-25
...

# `Python` - `while` loops and functions{data-background-color="#d9d2e9"}

# `while` loops

```python
while <test>:
  statement1
  statement2
```

"While some logical test is true, continue executing the block of statements"

# What does this program do?

<div style="font-size:50%">
```python
sum = 0
count = 1

while count < 3:
  sum = sum + count
  count = count + 1
print(count)
print(sum)
```
</div>

# What does this program do?

<div class="column" style="float:left; width: 50%; font-size:50%">
```python
sum = 0
count = 1

while count < 3:
  sum = sum + count
  count = count + 1
print(count)
print(sum)
```
</div>
<div class="column" style="float:left; width: 50%; font-size:50%">
```python
sum = 0
count = 1
count < 3 TRUE
  sum = 0 + 1
  count = 1 + 1
```

```python
sum = 1
count = 2
count < 3 TRUE
  sum = 1 + 2
  count = 2 + 1
```

```python
sum = 3
count = 3
count < 3 FALSE
```
</div>

# `for` vs. `while` loops

* `for` loops: *determinate* number of loops (probably more common)  
* `while` loops: *indeterminate*  number of loops

# Examples of `for` loops

<div style="font-size:60%">
```python
for base in sequence:
  <do something with each base>

for sequence in database:
  <do something with each sequence>

for index in range(5, 200):
  <do something with each index>
```

# Examples of `while` loops

<div style="font-size:60%">
```python
while error > 0.05:
  <do something to reduce error>

while score > 0:
  <traceback through DP matrix>
```

# Example of infinite loop

You can set up a while loop such that it will run forever

```python
count = 0

while count <=0:
  count = count + 1
```

# What's a function?

> reusable pieces of code that take zero or more arguments, perform some actions, and returns one or more values.

<div class="column" style="float:left; width: 50%; font-size:80%">
```python
len('AGT')
```
</div>
<div class="column" style="float:left; width: 50%; font-size:80%">
* arguments: string or list  
* actions: count number of elements
* return: integer
</div>

# You can write your own functions

<div style="font-size:90%">
```python
def my_function(datapoint):
  result = datapoint * 100
  return result
```
</div>
<div class="fragment" style="font-size:80%">
```python
l = [1, 2, 3]
for i in l:
  print(my_function(i))
```
</div>

<div class="fragment">
You need to define your function *then* call the function
</div>

# Why custom functions?

<div class="fragment">
## Avoid repetition
* easier to look at
* avoid bugs  
</div>

<div class="fragment">
## Self-documenting code
<div style="font-size:60%">
```python
def upgma_iteration(data):
	dist_matrix = calculate_distance_matrix(data)
	smallest_pair  = find_smallest_dist(dist_matrix)
	merged_node_data = merge_nodes(smallest_pair, data)
	return merged_node_data
```
</div>
</div>
