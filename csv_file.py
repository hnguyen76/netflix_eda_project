import csv

product = input('Enter product name: ')
price = input('Enter price: ')

with open("products.csv", 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([product, price])

print('products saved to CSV!')



import csv
try:
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        
        try:
            next(reader)
        except StopIteration:
            print('Product file is empty')
        else:
            for product, price in reader:
                print(f'Product: {product} - Price: {price}')

except FileNotFoundError:
    print('No product file found')
    
