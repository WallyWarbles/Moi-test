import time
def lol(): #Запрашивает у пользователя авторизацию для начала программы
		login = input ('Введите ваш логин:')
		password = input('Введите пароль:')
		if login == ('Sultan') or ('Katya') and password == ('6801168'):
			print ('Добро пожаловать :) ')
		else:
			print ('Неправильный логин или пароль.Пожалуйста, повторите попытку')
			sultan()
lol()
time.sleep (4)     #прога останавливается на 4 секунды

def Arifm():        #Арифметическая прогрессия
	i = input('Введите первый член арифм. прогрессии:  ')
	arifm = [i]
	d = input('Введите разность арифм. прогрессии:  ')
	An = input('Введите н-ный член арифм. прогрессии:  ')
	for x in range(int(An)):
		i = int(i) + int(d)
		arifm.append (i)
	print (arifm)

def Geom():
	b = input('Введите первый член геометрической прогрессии:  ')
	geom = [b]
	q = input('Введите знаменатель прогрессии:  ')
	Bn = input('Введите n-ный член прогрессии:  ')
	for x in range(int(Bn)):
		b = int(b) * int(q)
		geom.append (b)
	print (geom)


a=input('Что вы хотите выполнить? Арифметическая прогрессия = A, Геометрическая = G; Введите ваш запрос:  ')
if a == ('A'):
	Arifm()
if a == ('G'):
	Geom()

print ('Программа завершена.')