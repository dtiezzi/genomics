import datetime as d

def editDistRecursive(x, y):
	if len(x) == 0:
		return len(y)
	elif len(y) == 0:
		return len(x)
	else:
		delt = 1 if x[-1] != y[-1] else 0
		return min(editDistRecursive(x[:-1], y[:-1]) + delt,
						editDistRecursive(x[:-1], y) + 1,
						editDistRecursive(x, y[:-1]) + 1)

a= "OnceUponATime"
b= "Once potAnime"
sd= d.datetime.now() ;
print(editDistRecursive(a, b))
print((d.datetime.now() - sd).total_seconds())
