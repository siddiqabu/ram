def main():
	n=input()
	d=0
	for i in n:
		if i.isnumeric() :
			d=d+1
	print('No of numerics in a string is :%d'%d)
main()
