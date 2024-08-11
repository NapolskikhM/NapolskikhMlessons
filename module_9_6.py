def all_variants(text):
	i = 0 # длина подпоследовательности строки
	a = len(text)
	while i <= a: # цикл по длине подпоследовательности строки
		i += 1
		j = 0
		while j + i <= a: # цикл по строке
			yield text[ j: j+i]			
			j += 1
			
# проверочный код
a = all_variants("abc")
for i in a:
	print(i)