# import json

# product = {
#     "product_name": "Laptop",
#     "price": 1200
# }

# with open('products.json', 'w') as file:
#     json.dump(product, file, indent=4)
    
# print('JSON saved!')

# import json

# with open('products.json', 'r') as file:
#     product = json.load(file)
    
#     print(f'Product name: {product["product_name"]}')
#     print(f'Price: {product['price']}')
    
import json

students = [
    {'name': 'Hieu', 'score': 90},
    {'name': 'Anna', 'score': 85}
]

with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)
print("JSON saved")

with open('students.json', 'r') as file:
    read_students = json.load(file)
    for student in read_students:
        print(f'{student["name"]} - {student["score"]}')
