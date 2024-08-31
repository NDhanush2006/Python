"""
Dictionary :- Merge/update
New operators| and | = allow for merfing and updting Dictionaries
"""

dict1 = {"a": 1, "b":2}
dict2 = {"c": 3, "d":4}
merged = dict1 | dict2
print(merged)

"""
You can now  use multiple context managers in a single with statement more cleanly using the paranthesis context manager

syntax :-
with(
    open('file1.txt') as f1,
    open('file2.txt') as f2,
):
"""


