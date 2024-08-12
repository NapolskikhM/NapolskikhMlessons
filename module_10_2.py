from threading import Thread
from time import sleep

class Knight(Thread):
	
	def __init__(self, name, power):
		super().__init__()
		self.name = name
		self.power = power
		
	def run(self):
		enemy_ = 100
		day_ = 0
		print(f'{self.name}, на нас напали!')
		while enemy_ > 0:
			enemy_ -= self.power
			day_ += 1
			if day_ > 1:
				sleep(1)
			print(f'{self.name} сражается {day_} день(дня)..., осталось {enemy_} воинов')
		print(f'{self.name} одержал победу спустя {day_} дней(дня)')
							
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')