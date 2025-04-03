from collections import defaultdict
from typing import Callable, TypeVar, List, Dict

T = TypeVar('T')
K = TypeVar('K')

def group_by(func: Callable[[T], K], lst: List[T]) -> Dict[K, List[T]]:
    """Group elements of a list by keys derived from a function.
    
    Args:
        func: A function that computes the grouping key for each element
        lst: List of items to be grouped
        
    Returns:
        Dictionary where keys are function results and values are lists of items
        that produced each key
    """
    result = defaultdict(list)
    for item in lst:
        result[func(item)].append(item)
    return dict(result)

if __name__ == '__main__':
    # Test cases
    print(group_by(len, ["hi", "bye", "yo", "try"])) # Output: {2: ['hi', 'yo'], 3: ['bye', 'try']}
    
    print(group_by(lambda x: x[0], ["apple", "banana", "cherry", "avocado"])) # Output: {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}
   
    print(group_by(lambda x: x % 2, [1, 2, 3, 4, 5])) # Output: {1: [1, 3, 5], 0: [2, 4]}
    