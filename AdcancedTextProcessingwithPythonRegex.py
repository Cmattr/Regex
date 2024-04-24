def extract_value(text, key):
    # Split the text by semicolons
    entries = text.split(';')
    
    # Search for the key in each entry
    for entry in entries:
        parts = entry.split(':')
        if len(parts) == 2:
            k, v = parts
            if k.strip() == key:
                return v.strip()  # Return the value
    
    return None  # Key not found

# Example usage
text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
occupation = extract_value(text, "Occupation")
if occupation:
    print(f"Occupation: {occupation}")
else:
    print("Occupation not found in the text.")