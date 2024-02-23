def convert(lst):
	keys = lst[::2] # slice the list to get keys
	values = lst[1::2] # slice the list to get values
	res_dict = {keys[i]: values[i] for i in range(len(keys))}
	return res_dict
lst = ['a', 1, 'b', 2, 'c', 3]
print(convert(lst)) # {'a': 1, 'b': 2, 'c': 3}
