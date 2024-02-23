def remove_tuple_empty(tuple):
      return[t for t in tuple if len(t)>0]

tuple =[(),('prteek',111,'ashish',222),(333,'ankur',444,'aditya',555),('afjal',666)]
print(remove_tuple_empty(tuple))

