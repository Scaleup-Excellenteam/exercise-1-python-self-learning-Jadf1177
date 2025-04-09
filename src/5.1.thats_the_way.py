import os

def thats_the_way(directory, prefix="deep"):
    """Return list of files starting with given prefix in directory."""
    deep_files = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.startswith(prefix):
                    deep_files.append(entry.name)
    except (OSError, PermissionError) as e:
        print(f"Error accessing {directory}: {e}")
    return deep_files

if __name__ == '__main__':
    directory_path = "images"
    print(thats_the_way(directory_path))