from random import choice


# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
a = list(map(lambda x, y: x == y, first, second))

print(a)

# Замыкание
def get_advanced_writer(file_name):
	def write_everything(*data_set):
		with open(file_name, 'w') as a:			
			for i in data_set:
				a.write(str(i) + '\n')
	return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print()
with open('example.txt') as file:
	print(*file, sep='')
	
# Метод __call__
class MysticBall:

	def __init__(self, *args):
		words = []
		for i in args:
			words.append(i)
		self.words = words
		
	def __call__(self):
		return choice(self.words)
		
		
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
