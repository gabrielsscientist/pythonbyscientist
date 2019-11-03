products = ('Pizza', 15, 'Juice', 4, 'Iphone', 1000, 'Mansion', 3000000, 'Ferrari', 500000, 'Fruits', 8,
            'Computer', 2000, 'Clothes', 5000)
print('='*34)
print(f"              PRICES")
print('='*34)
for i in range(0, len(products), 2):
    print(products[i], '.'*(20 - len(products[i])), f'$ {products[i+1]:>10.2f}')
    i += 2
