import json

contact = {
    "name": "Hieu",
    "phone": "123"
}

with open('contact.json', 'w') as file:
    json.dump(contact, file, indent=4)
    
print('JSON saved!')

