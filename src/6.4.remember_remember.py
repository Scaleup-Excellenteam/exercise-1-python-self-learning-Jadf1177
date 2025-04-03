from PIL import Image

def remember_remember(image_path, threshold=50):
    """Extract hidden message from image using vertical pixel pattern.
    
    Args:
        image_path: Path to image file
        threshold: Gray value cutoff (0-255) to consider as message pixel
        
    Returns:
        Extracted string from dark pixel positions
    """
    try:
        img = Image.open(image_path)
        width, height = img.size
    except Exception as e:
        raise RuntimeError(f"Error opening image: {e}")

    # Convert to grayscale and check dimensions
    gray_img = img.convert('L')
    if height > 255:
        raise ValueError("Image too tall for ASCII decoding (max 255px height)")

    message_chars = []
    
    # Use faster pixel access
    pixels = gray_img.load()

    for x in range(width):
        char_found = False
        # Search from bottom to top (common message encoding pattern)
        for y in reversed(range(height)):
            if pixels[x, y] < threshold:
                try:
                    message_chars.append(chr(y))
                    char_found = True
                    break
                except ValueError:
                    continue
        if not char_found:
            message_chars.append('?')  # Placeholder for missing characters

    return "".join(message_chars)

if __name__ == '__main__':
    try:
        message = remember_remember("resources/code.png")
        print("The secret message is:", message)
    except Exception as e:
        print("Error:", str(e))