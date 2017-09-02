one = input('Введите значение 1: ')
two = input('Введите значение 2: ')
def get_summ (one,two,delimetr=' '):
	return str(one)+str(delimetr)+str(two)
print(get_summ(one,two).upper())