#Compressing the string

#importing library
import itertools

#taking input
S=input()

#making a list of consecutive numbers lie ['1','222','33''1']
result = [''.join(group) for key, group in itertools.groupby(S)]

#creating tuple list for the output -> (occurences,number)
tuple_list = [(len(group), int(group[0])) for group in result]

# (*) unpacks the tuple list
print(*tuple_list)
