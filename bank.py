def new_customer():
	name=input("name :")
	age=input("age :")
	address=input("adress :")
	username=input("username :")
	password=input("password :")
	amount=input("amount :")
	a=[name,age,address,username,password,amount]
	f=open(f"{username}.txt",'x')
	for x in a:
		f.write(f"{x}\n")
	f.close()
	print("account opened")
	old_customer()
def old_customer():
	username=input("username :")
	password=input("password :")
	f=open(f"{username}.txt",'r+')
	a=f.readlines()
	if(a[4].strip()==password):
		print("Hello ",a[0])
		log_in(f,a)
	else:
		print("invalid password")
		old_customer()
	f.close()
def log_in(f,a):
	print("Hello",a[0])
	print("press 1 for deposit\npress 2 for withdrawl\npress 3 for exit")
	c=int(input("enter your choice :"))
	if (c==1):
		deposit(f,a)
	elif(c==2):
		withdraw(f,a)
	elif(c==3):
		f.close()
		exit()
def deposit(f,a):
	amount=int(input("enter amount :"))
	d=int(a[5])+amount
	f.write(f"{d}\n")
	print("amount :",d)
	log_in(f,a)
def withdraw(f,a):
	amount=int(input("enter amount :"))
	if(amount<int(a[5])):
		d=int(a[5])-amount
		f.write(f"{d}\n")
		print("current amount:",d)
		log_in(f,a)
	else:
		print("your account balance is",a[5])
		print("low balance")
		log_in(f,a)
def main():
	print("press 1 for new account\npress 2 for existing account\npress 3 for exit")
	p=int(input("enter your choice :"))
	if(p==1):
		new_customer()
	elif(p==2):
		old_customer()
	elif(p==3):
		exit()
	else:
		print("wrong choice")
		main()
main()

