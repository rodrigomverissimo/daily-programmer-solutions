"""
link: https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/

Warmup
Implement the flipfront function. Given an array of integers and a number n between 2 and the length of the array (inclusive), return the array with the order of the first n elements reversed.
```
flipfront([0, 1, 2, 3, 4], 2) => [1, 0, 2, 3, 4]
flipfront([0, 1, 2, 3, 4], 3) => [2, 1, 0, 3, 4]
flipfront([0, 1, 2, 3, 4], 5) => [4, 3, 2, 1, 0]
flipfront([1, 2, 2, 2], 3) => [2, 2, 1, 2]
```
Optionally, as an optimization, modify the array in-place (in which case you don't need to return it). It's also fine to have the array be a global variable or member variable, in which case you only need to pass in the argument n.

Challenge
Given an array of integers, sort the array (smallest to largest) using the flipfront function on the entire array. For
example, the array:

[3, 1, 2, 1]
may be sorted with three calls to flipfront:
```
flipfront([3, 1, 2, 1], 4) => [1, 2, 1, 3]
flipfront([1, 2, 1, 3], 2) => [2, 1, 1, 3]
flipfront([2, 1, 1, 3], 3) => [1, 1, 2, 3]
```
Make sure you correctly handle elements that appear more than once in the array!

You may not modify the array by any other means, but you may examine it however you want. You can even make a copy of
the array and manipulate the copy, including sorting it using some other algorithm.

Optional bonus (hard!)
Try to minimize the number of times you call flipfront while sorting. Note that this is different from minimizing the
runtime of your program.

How many flipfront calls do you require to sort this list of 10,000 integers? My record is 11,930. Can you do better?

(This is a repost of Challenge #63 [intermediate], originally posted by u/oskar_s in June 2012.)
"""

from typing import List, Callable
import sys

sys.setrecursionlimit(10 ** 5)

# the flipfront implementation with a lambda
l_flipfront: Callable = lambda array, index: array[index - 1 :: -1] + array[index:]


# the flipfront sort implementation with recursion
def flipfront_sort(array: List[int]) -> List[int]:
    # if we reach the end of the recursion
    if len(array) == 1:
        return array

    # get the argmax to use it for sorting
    argmax: int = max(range(len(array)), key=lambda x: array[x])

    # if the argmax is already in the last position
    if argmax == len(array):
        flipfront_sort(array[:-1]) + array[-1:]

    # if the argmax is in the first position we just need to flip once
    elif argmax == 0:
        array = l_flipfront(array, len(array))
        return flipfront_sort(array[:-1]) + array[-1:]

    # else, we need to flip twice
    else:
        array = l_flipfront(array, argmax + 1)
        array = l_flipfront(array, len(array))
        return flipfront_sort(array[:-1]) + array[-1:]


def read_challenge_file() -> List[int]:
    to_sort: List[int] = list()
    with open("gistfile1.txt", "r") as challenge_file:
        for line in challenge_file:
            to_sort.append(int(line.strip("\n")))
    return to_sort


def challenge():
    print("Warmup:")
    print(l_flipfront(array=[0, 1, 2, 3, 4], index=2))
    print(l_flipfront(array=[0, 1, 2, 3, 4], index=3))
    print(l_flipfront(array=[0, 1, 2, 3, 4], index=5))
    print(l_flipfront(array=[1, 2, 2, 2], index=3))

    print("Main Challenge")

    to_sort: List[int] = read_challenge_file()
    sorted_challenge = flipfront_sort(to_sort)

    print("Did it match the automatic sort?")
    print(sorted_challenge == sorted(to_sort))


"""
I noticed that there was an implementation in the comments that went for a loop. It is 25% faster, because for loops
are faster than recursion as the latter also uses the memory stack. Putting it below for future reference.
"""


def flipfront(x, n):
    x[:n] = x[n - 1 :: -1]


def flipfront_sort_best_solution(x):
    argmax = lambda x: max(enumerate(x), key=(lambda kv: kv[1]))[0]

    for i in reversed(range(1, len(x) + 1)):
        j = argmax(x[:i]) + 1
        if j < i:
            flipfront(x, j)
            flipfront(x, i)


challenge()
