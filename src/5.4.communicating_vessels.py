from itertools import chain
from collections.abc import Iterable

def interleave(*iterables):
    """Interleave elements from multiple iterables into a single list.
    
    Args:
        *iterables: One or more iterable collections
        
    Returns:
        List containing elements from all iterables, interleaved
    """
    if not all(isinstance(it, Iterable) for it in iterables):
        raise TypeError("All arguments must be iterable")
        
    return list(generator_interleave(*iterables))

def generator_interleave(*iterables):
    """Generator that interleaves elements from multiple iterables.
    
    Args:
        *iterables: One or more iterable collections
        
    Yields:
        Elements from all iterables in interleaved order
    """
    iterators = [iter(it) for it in iterables]
    while iterators:
        for iterator in list(iterators):  # Safe iteration copy
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)

if __name__ == '__main__':
    # Test cases
    print(interleave('ab', [1, 2, 3], ('@', '%')))  # ['a', 1, '@', 'b', 2, '%']
    print(list(generator_interleave('ab', [1, 2, 3], ('@', '%'))))  # Same output