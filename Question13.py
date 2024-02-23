def find_dup_char(input):
	x=[]
	for i in input:
		if i not in x and input.count(i)>1:
			x.append(i)
	print(" ".join(x))

# Driver program
if __name__ == "__main__":
	input = 'PrteekSingh'
	find_dup_char(input)
