def validate_ingredients(ingredients: str) -> str:
    sacred_elements = ["fire", "water", "earth", "air"]
    
    if any(element in ingredients.lower() for element in sacred_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"