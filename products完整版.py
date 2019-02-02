#products完整版

#1.get info from file and add into list
products = []
with open('products.csv','r',encoding='utf-8'):
	for line in f:
		if 'products,price' in line:
			continue
		name,price = line.strip().split(',')
		#👆填车厢
		products.append([name,price])
		#👆装火车
print(products)

#2.input(products,price)
while True:
	name = input('name?')
	if name == 'q':
		break
	price = inout('price?')
	price = int(price)
	products.append([name,price])
print（products）

#购买记录
for p in products:
	print(p[0],'的价格是', p[1])

#f.write:栏位名称+input
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('products,price\n')
	for p in products:
		f.write(p[0]+ ','+str(p[1]) + '\n')


#把csv文档数据加入list用append: listname.append([ , ])
#把list清单写入csv用f.write: f.write(p[0]+','+p[2]+'\n')