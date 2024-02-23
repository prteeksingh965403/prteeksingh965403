my_list = list(range(10)) 
chunk_size = 3
while my_list: 
	chunk, my_list = my_list[:chunk_size], my_list[chunk_size:] 
	print(chunk)
