a=float(input("enter first number :"))
b=float(input("enter second number :"))
print("+ for sum")
print("- for sub")
print("* for mul")
print("/ for div")
print("^ for power")
c=input("enter your choice :")
if (c=="+"):
	print("sum :",a+b)
elif (c=="-"):
	print("sub :",a-b)
elif(c=="*"):
	print("mul :",a*b)
elif(c=="/"):
	print("div :",a/b)
elif(c=="^"):
	print("power :",a**b)
else:
	print("no operation")