products = []
while True:
	name = input('product:')
	if name == 'q':
		break 
	price = input('price:')
	price = int(price)
#这里price做了型别转换，由字串变成了数字，而name还是字串
#数字跟字串在写入时候不能相加，所以第19行要写成str(p[1])
	products.append([name,price])
print(products)

for p in products:
	print('price of',p[0], 'is',p[1] )

with open('products.csv','w', encoding= 'utf-8') as f:
	#utf-8解决乱码问题
	f.write('products, price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')