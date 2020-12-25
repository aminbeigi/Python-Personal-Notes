"""Methods List Comprehension that all return the same list 

List comprehension is an elegant way to define and create lists based on existing lists.
Faster than regular normal functions and loops for creating lists.
"""

# "full" for loop
lst = []
for i in range(25):
    if i%2 == 0:
        lst.append(i)
    else:
        lst.append("odd")

# list comprehension
# [f(x) for i in iterable]
comp_lst = [i if i%2==0 else 'odd' for i in range(25)]

# lambda
lamba_lst = [(lambda i: i if i%2==0 else 'odd')(i) for i in range(25)]

# lamba map
map_lamba_lst = list(map(lambda i: i if i%2==0 else 'odd', range(25)))