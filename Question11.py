# Function to rotate string left and right by d length

def rotate(str1,n):

	# Create the extended string and index of for rotation
	temp = str1 + str1
	l1 = len(str1)
	l2 = len(temp)
	Lfirst = temp[n : l1+n]
	Lfirst = temp[l1-n : l2-n]

	# now printing the string 
	print ("Left Rotation : ", Lfirst) 
	print ("Right Rotation : ", Lfirst )

# Driver program
if __name__ == "__main__":
	input = 'Prteek_Singh'
	d=2
	rotate(input,d)
