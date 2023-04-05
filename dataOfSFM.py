konst = {'фиалетовое': '0',
		 'прозрачное': '4',
		 'красное': '6'}


typeOfSMF = input().lower()
diameter = input('Этот параметр вам ненужон, нажмите ENTER')


def result(type, dia):
	if type == 'фиалетовое':
		return 'У данного оптоволокна критический радиус очень мал для измерения'
	return konst[typeOfSMF] + 'mm' if type in konst else 'Нет данного типа волокна'


print(result(typeOfSMF, diameter))
