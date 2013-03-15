from utils import profile

@profile
def myFunction(some=None):
	newsome = some + some + some
	prints(newsome)

def prints(some):
	print some

myFunction("testing")
