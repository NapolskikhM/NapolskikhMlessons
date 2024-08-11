from datetime import datetime
from time import sleep
from threading import Thread
def wite_words(word_count, file_name):
	with open(file_name, 'w') as file:
		for i in range(word_count):
			file.write(f'Какое-то слово № {i + 1} \n')
			sleep(0.1)
	print(f'Завершилась запись в файл {file_name}')
	
time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_stop = datetime.now()
print(f'Работа потоков {time_stop - time_start}')
	

time_start = datetime.now()

thr_5 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_6 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_7= Thread(target=wite_words, args=(200, 'example7.txt'))
thr_8 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()

thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()

time_stop = datetime.now()
print(f'Работа потоков {time_stop - time_start}')


	
			