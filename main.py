import matplotlib.pyplot as plt
readData = open('data.base', mode='r')
writeData = open('data.base', mode='a')
x, y = list(), list()
for tr in readData.readlines():
	x.append(int(tr.split(' ')[0]))
	y.append(int(tr.split(' ')[-1]))
print(x, y)


class Window:
	def __init__(self):
		pass

	def work(self):
		for _ in range(int(input('How much point you want input? : '))):
			line = input('New data: ')
			x.append(int(line.split(' ')[0]))
			y.append(int(line.split(' ')[-1]))
			writeData.write('\n' + line.split(' ')[0] + ' ' + line.split(' ')[-1])
		plt.plot(x, y, color='green', marker='o', markersize=7, linestyle='dashed')
		plt.xlabel('Мощность, Вт')
		plt.ylabel('Диаметр, мм')
		plt.title('Первый график')
		plt.show()


wn = Window()
wk = True
while wk:
	try:
		wn.work()
	except Exception as ex:
		print('!!!BUG REPORT!!!')
		print('!!!', ex)
readData.close()
writeData.close()
