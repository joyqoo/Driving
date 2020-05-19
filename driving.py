country = input('請問你是哪國人?')
age = input('請問年齡?')
age = int(age)
if country=='台灣' or country=='Taiwan':
	if age > 18:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')	
elif country=='美國' or country=='US':
	if age > 18:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
else:
	print('無法辨識此國家')	