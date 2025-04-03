import re
from pathlib import Path
from typing import List

DEFAULT_FILENAME = "../resources/logo.jpg"
CHUNK_SIZE = 1024
PATTERN = re.compile(rb'[a-z]{5,}(?=!)')  # Lookahead to exclude '!'

def parsle_tongue(filename: str = DEFAULT_FILENAME) -> List[str]:
    """Extract 5+ lowercase letter words preceding '!' from binary file.
    
    Args:
        filename: Path to binary file
        
    Returns:
        List of found words (without trailing '!')
    """
    found_words = []
    
    try:
        with open(filename, "rb") as file:
            while chunk := file.read(CHUNK_SIZE):
                matches = PATTERN.findall(chunk)
                found_words.extend(m.decode() for m in matches)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    
    return found_words

if __name__ == '__main__':
    for word in parsle_tongue():
        print(word)