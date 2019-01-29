products = []
while True:
	name = input('what is the name of product?')
	if name == 'q':
		break
	price = input ('what is the price of product?')
	products.append([name, price])
print(products)
