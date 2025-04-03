import time
from collections.abc import Callable

def running_2000(f: Callable, *args, **kwargs) -> float:
    """
    Time the execution of a function with optional repetitions.
    
    Args:
        f: Callable function to time
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
        
    Returns:
        Execution time in seconds (average if repetitions > 1)
        
    Raises:
        TypeError: If first argument is not callable
    """
    # Input validation
    if not callable(f):
        raise TypeError("First argument must be a callable function")
        
    # Default values
    repetitions = kwargs.pop('repetitions', 1)
    if repetitions < 1:
        raise ValueError("Repetitions must be ≥ 1")

    total_time = 0.0
    
    try:
        for _ in range(repetitions):
            start = time.perf_counter()
            f(*args, **kwargs)  # Call function but ignore return value
            total_time += time.perf_counter() - start
    except Exception as e:
        print(f"Error during execution: {e}")
        return float('nan')  # Return NaN for failed executions
        
    return total_time / repetitions

if __name__ == '__main__':
    # Original test cases
    print("Runtime for print:", running_2000(print, "Hello")) 
    print("Runtime for zip:", running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print("Runtime for format:", running_2000("Hi {name}".format, name="Bug"))
    
    # New test case with repetitions
    print("Average time:", running_2000(sum, [1, 2, 3], repetitions=1000))