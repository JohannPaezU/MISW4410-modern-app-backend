import requests

ingredients = [
    {
        "name": "Potato",
        "unit": "KILOGRAM",
        "unit_value": 2.5,
        "purchase_place": "Local Market",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/potato.png"
    },
    {
        "name": "Sugar",
        "unit": "GRAM",
        "unit_value": 500,
        "purchase_place": "Supermarket",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/sugar.png"
    },
    {
        "name": "Milk",
        "unit": "LITER",
        "unit_value": 1,
        "purchase_place": "Dairy Store",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/milk.png"
    },
    {
        "name": "Butter",
        "unit": "GRAM",
        "unit_value": 200,
        "purchase_place": "Supermarket",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/butter.png"
    },
    {
        "name": "Flour",
        "unit": "KILOGRAM",
        "unit_value": 1,
        "purchase_place": "Bakery Supplier",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/flour.png"
    },
    {
        "name": "Egg",
        "unit": "UNIT",
        "unit_value": 12,
        "purchase_place": "Farm",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/egg.png"
    },
    {
        "name": "Olive Oil",
        "unit": "MILLILITER",
        "unit_value": 750,
        "purchase_place": "Gourmet Store",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/olive-oil.png"
    },
    {
        "name": "Rice",
        "unit": "KILOGRAM",
        "unit_value": 2,
        "purchase_place": "Supermarket",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/rice.png"
    },
    {
        "name": "Chicken Breast",
        "unit": "KILOGRAM",
        "unit_value": 1.2,
        "purchase_place": "Butcher",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/chicken-breast.png"
    },
    {
        "name": "Tomato",
        "unit": "KILOGRAM",
        "unit_value": 1.5,
        "purchase_place": "Local Market",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/tomato.png"
    },
    {
        "name": "Salt",
        "unit": "GRAM",
        "unit_value": 300,
        "purchase_place": "Supermarket",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/salt.png"
    },
    {
        "name": "Black Pepper",
        "unit": "GRAM",
        "unit_value": 100,
        "purchase_place": "Spice Store",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/black-pepper.png"
    },
    {
        "name": "Onion",
        "unit": "KILOGRAM",
        "unit_value": 1,
        "purchase_place": "Local Market",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/onion.png"
    },
    {
        "name": "Garlic",
        "unit": "GRAM",
        "unit_value": 250,
        "purchase_place": "Local Market",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/garlic.png"
    },
    {
        "name": "Carrot",
        "unit": "KILOGRAM",
        "unit_value": 1,
        "purchase_place": "Local Market",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/carrot.png"
    },
    {
        "name": "Cheese",
        "unit": "GRAM",
        "unit_value": 300,
        "purchase_place": "Deli",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/cheese.png"
    },
    {
        "name": "Honey",
        "unit": "MILLILITER",
        "unit_value": 250,
        "purchase_place": "Bee Farm",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/honey.png"
    },
    {
        "name": "Lemon Juice",
        "unit": "MILLILITER",
        "unit_value": 100,
        "purchase_place": "Supermarket",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/lemon-juice.png"
    },
    {
        "name": "Water",
        "unit": "LITER",
        "unit_value": 2,
        "purchase_place": "Supermarket",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/water.png"
    },
    {
        "name": "Vanilla Extract",
        "unit": "MILLILITER",
        "unit_value": 50,
        "purchase_place": "Bakery Supplier",
        "image_url": "https://raw.githubusercontent.com/JohannPaezU/MISW4410-modern-app-backend/refs/heads/main/images/vanilla-extract.png"
    }
]

URL = "http://localhost:3000/ingredients"
SECRET_TOKEN = "your_secret_token_here"  # Replace with your actual secret token
for ingredient in ingredients:
    response = requests.post(URL, json=ingredient, headers={"Authorization": f"Bearer {SECRET_TOKEN}"})
    print("Status:", response.status_code)
    print("Response:", response.json())

print(f"All ingredients populated successfully, total: {len(ingredients)}")
