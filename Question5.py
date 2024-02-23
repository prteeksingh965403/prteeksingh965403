# CREAT A LIST
List = [1, 2, 'Prteek_Singh', 4, 'MJPRU', 5, 'University']
print("\nList creat with the use of Mixed Values: ")
print(List)
#Insert element in given list
List.append(9)
List.append('Thanks God')
List.append(11)
print('\n list after insert three elements:')
print(List)
# Insert element Using Iterator mathod
print('Insert element  1 to 9 using iterator method: ')
for i in range(1,10):
    List.append(i)
print(List)
# Delet element from given list
print('After remove element 1 to 9 from list:')
for i in range(1,10):
    List.remove(i)
print(List)
#reverse elements from given list
List.reverse()
print("After reverse of list :",List)
