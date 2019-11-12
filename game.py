def game():
	a=[]
	for x in range(0,9):
		a.append(x+1)
	def display():
		print("THIS IS YOUR DASHBOARD")
		print('',a[0],'|',a[1],'|',a[2],'\n','---------','\n',a[3],'|',a[4],'|',a[5],'\n','---------','\n',a[6],'|',a[7],'|',a[8])
	display()

	print("CHOOSE CHARACTER")
	s1=input("player 1 :")
	s2=input("player 2 :")
	def player1():
		if(s1=='X'):
			choice1()
	def player2():
		if(s2=='O'):
			choice2()
	def choice1():
		c=int(input("enter your choice :"))
		for i in range(0,9):
			if(c==a[i]):
				a[i]=s1
	def choice2():
		c=int(input("enter your choice :"))
		for i in range(0,9):
			if(c==a[i]):
				a[i]=s2

	for j in range(0,9):
		if(j%2==0):
			player1()
			display()
		else:
			player2()
			display()
game()
print("y for yes and n for no")
s=input("Do you want to play again :")
if(s=='y'):
	game()
else:
	print("Good Bye")