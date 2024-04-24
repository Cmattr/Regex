import re
price_str1 = "$512.11"
price_str2 = "$11.14"
price_str3 = "$110.12"

def tag_products(descriptions):
    
    keyword_mapping = {
        "Smartphone": "Electronics",
        "Cotton t-shirt": "Apparel",
        "Stainless steel kitchen knife set": "Home & Kitchen"
     
    }

    
    tagged_products = []

    for desc in descriptions:
        for keyword, category in keyword_mapping.items():
            if keyword.lower() in desc.lower():
                tagged_products.append((desc, category))
                break  

    return tagged_products

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
tagged_products = tag_products(descriptions)

for product, category in tagged_products:
    print(f"Product: {product} | Category: {category}")
    def convert_price_format(price_str):
    # Extract numeric part from the price string
        price = re.search(r'\$(\d+\.\d+)', price_str)
        if price:
            formatted_price = f"USD {price.group(1)}"
            return formatted_price
        else:
            return None


formatted_price1 = convert_price_format(price_str1)
formatted_price2 = convert_price_format(price_str2)
formatted_price3 = convert_price_format(price_str3)

print(f"smartphone original Price: {price_str1} | Formatted Price: {formatted_price1}")
print(f"cotton t-shirt original Price: {price_str2} | Formatted Price: {formatted_price2}")
print(f"Kitchen knife set original Price: {price_str3} | Formatted Price: {formatted_price3}")