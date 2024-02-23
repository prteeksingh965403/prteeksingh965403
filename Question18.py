#  A program to remove duplicate words from a given sentence
string = 'Python is most loving language by programmers, which is used in many fields'
print(' '.join(set(string.split())))
