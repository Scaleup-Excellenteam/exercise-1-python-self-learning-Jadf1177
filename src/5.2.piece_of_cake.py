def piece_of_cake(prices, optionals=None, **ingredients):
    """Calculate total price of ingredients, excluding optional ones.
    
    Args:
        prices: Dict of {ingredient: price_per_100g}
        optionals: List of ingredients to exclude
        **ingredients: ingredient=grams pairs
    
    Returns:
        Total price of non-optional ingredients
    """
    GRAMS_TO_KG = 100  # Conversion factor
    if optionals is None:
        optionals = []
    
    # Input validation
    if not isinstance(optionals, list):
        raise TypeError("optionals must be a list")
    
    total_price = 0.0
    
    for ingredient, grams in ingredients.items():
        if ingredient not in optionals:
            price_per_kg = prices.get(ingredient, 0)
            if grams < 0 or price_per_kg < 0:
                raise ValueError("Values cannot be negative")
            total_price += price_per_kg * grams / GRAMS_TO_KG
    
    return total_price


print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(piece_of_cake({}))
