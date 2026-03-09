def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):  # if it's a list, go deeper
            result += flatten(item)
        else:
            result.append(item)
    return result

def count_down(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        count_down(n - 1)


print(f"Flattened: {flatten([1, [2, 3], [4, [5, 6]], 7])}")
count_down(5)
'''
Write a recursive function called flatten that takes a nested list
and returns a single flat list with all values.

Then write a recursive function called count_down that counts down
from a given number and prints each value.

Call them with:
flatten([1, [2, 3], [4, [5, 6]], 7])
count_down(5)

Expected output:
Flattened: [1, 2, 3, 4, 5, 6, 7]
5
4
3
2
1
Done!
'''