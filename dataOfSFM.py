konst = {'a': 0,
		 'b': 2,
		 'c': 1}


typeOfSMF = input()
diameter = int(input())


def result(type, dia):
	return konst[typeOfSMF] * diameter


print(result(typeOfSMF, diameter))
