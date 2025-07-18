import requests

ingredients = [
    {
        "name": "Potato",
        "unit": "KILOGRAM",
        "unit_value": 2.5,
        "purchase_place": "Local Market",
        "image_url": ""
    },
    {
        "name": "Sugar",
        "unit": "GRAM",
        "unit_value": 500,
        "purchase_place": "Supermarket",
        "image_url": ""
    },
    {
        "name": "Milk",
        "unit": "LITER",
        "unit_value": 1,
        "purchase_place": "Dairy Store",
        "image_url": ""
    },
    {
        "name": "Butter",
        "unit": "GRAM",
        "unit_value": 200,
        "purchase_place": "Supermarket",
        "image_url": ""
    },
    {
        "name": "Flour",
        "unit": "KILOGRAM",
        "unit_value": 1,
        "purchase_place": "Bakery Supplier",
        "image_url": ""
    },
    {
        "name": "Egg",
        "unit": "UNIT",
        "unit_value": 12,
        "purchase_place": "Farm",
        "image_url": ""
    },
    {
        "name": "Olive Oil",
        "unit": "MILLILITER",
        "unit_value": 750,
        "purchase_place": "Gourmet Store",
        "image_url": ""
    },
    {
        "name": "Rice",
        "unit": "KILOGRAM",
        "unit_value": 2,
        "purchase_place": "Supermarket",
        "image_url": ""
    },
    {
        "name": "Chicken Breast",
        "unit": "KILOGRAM",
        "unit_value": 1.2,
        "purchase_place": "Butcher",
        "image_url": ""
    },
    {
        "name": "Tomato",
        "unit": "KILOGRAM",
        "unit_value": 1.5,
        "purchase_place": "Local Market",
        "image_url": ""
    },
    {
        "name": "Salt",
        "unit": "GRAM",
        "unit_value": 300,
        "purchase_place": "Supermarket",
        "image_url": ""
    },
    {
        "name": "Black Pepper",
        "unit": "GRAM",
        "unit_value": 100,
        "purchase_place": "Spice Store",
        "image_url": ""
    },
    {
        "name": "Onion",
        "unit": "KILOGRAM",
        "unit_value": 1,
        "purchase_place": "Local Market",
        "image_url": ""
    },
    {
        "name": "Garlic",
        "unit": "GRAM",
        "unit_value": 250,
        "purchase_place": "Local Market",
        "image_url": ""
    },
    {
        "name": "Carrot",
        "unit": "KILOGRAM",
        "unit_value": 1,
        "purchase_place": "Local Market",
        "image_url": ""
    },
    {
        "name": "Cheese",
        "unit": "GRAM",
        "unit_value": 300,
        "purchase_place": "Deli",
        "image_url": ""
    },
    {
        "name": "Honey",
        "unit": "MILLILITER",
        "unit_value": 250,
        "purchase_place": "Bee Farm",
        "image_url": ""
    },
    {
        "name": "Lemon Juice",
        "unit": "MILLILITER",
        "unit_value": 100,
        "purchase_place": "Supermarket",
        "image_url": ""
    },
    {
        "name": "Water",
        "unit": "LITER",
        "unit_value": 2,
        "purchase_place": "Supermarket",
        "image_url": ""
    },
    {
        "name": "Vanilla Extract",
        "unit": "MILLILITER",
        "unit_value": 50,
        "purchase_place": "Bakery Supplier",
        "image_url": ""
    }
]

URL = "http://localhost:3000/ingredients"
SECRET_TOKEN = "your_secret_token_here"
for ingredient in ingredients:
    response = requests.post(URL, json=ingredient, headers={"Authorization": f"Bearer {SECRET_TOKEN}"})
    print("Status:", response.status_code)
    print("Response:", response.json())

print(f"All ingredients populated successfully, total: {len(ingredients)}")