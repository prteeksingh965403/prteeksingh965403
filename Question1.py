a= 10
b= 0
c = 1
next_number =c 
count = 1
while count <= a:
	print(next_number, end=" ")
	count += 1
	b, c = c, next_number
	next_number = b + c
print()
