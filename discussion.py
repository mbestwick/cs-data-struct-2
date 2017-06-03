"""
Part 1: Discussion Questions

<<< Recursion >>>

1. Recursion is when a function calls itself to perform iterable actions.

2. A base case tells the recursion when to stop. Without a base case, the
recursion would happen forever and you would never finish what you are trying
to do.


<<< Graphs >>>

1. A graph is a tree with loops ('cyclic').

2. Graphs don't contain a root and do not represent a hierarchy.

3. A city's public transit routes would be good to model with a graph - it
would be a cyclic, un-directed graph.


<<< Performance of Different Data Structures >>>

Data Structure          Index    Search    Add-R    Add-L    Pop-L    Pop-R
--------------------    -----    ------    -----    -----    -----    -----
Python List (Array)      O(1)     O(n)      O(1)     O(n)     O(n)     O(1)
Linked List              O(n)     O(n)      O(1)     O(1)     O(1)     O(n)
Doubly-Linked List       O(n)     O(n)      O(1)     O(1)     O(1)     O(1)
Queue (Array)             x        x        O(1)      x       O(n)      x
Queue (LL, DLL)           x        x        O(1)      x       O(1)      x
Stack (Array, LL, DLL)    x        x        O(1)      x        x       O(1)
Deque (DLL)               x        x        O(1)     O(1)     O(1)     O(1)

Data Structure           Get      Add     Delete   Iterate    Memory
--------------------    -----    -----    ------   -------   --------
Dictionary (HashMap)     O(1)     O(1)     O(1)      O(n)     medium
Set (HashMap)            O(1)     O(1)     O(1)      O(n)     medium
Binary Search Tree      O(logn)  O(logn)  O(logn)    O(1)      low
Tree                     O(n)     O(1)     O(1)      O(1)      low


<<< Sorting >>>

1. Bubble Sort starts with the first element and compares it to the second, and
if greater will swap and keep moving down the line comparing. Once an element
reaches the end, the Bubble Sort starts back at the beginning to repeat the
same process. This process continues until all the iterations are complete.

2. The Merge Sort uses recursion to break down a list into single item lists,
then uses recursion again to merge those single item lists together (sorting as
it merges), and so on, until we have one list again and it's sorted.

3. The Quick Sort chooses a 'pivot' (middle point - hopefully!) and moves
everything lower than the pivot to the left, everything higher to the right,
then recursively quick sorts both sides of the pivot using the same exact
method. Performs depends on how well the pivot is chosen.

"""
