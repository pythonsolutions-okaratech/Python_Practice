# generate list in range functions

numbers = list(range(1,11))
# print(numbers)

# # Pop method
# # return  value by pop
# popped_item1 =  numbers.pop()
# popped_item2 = numbers.pop(2)
# print(numbers)

# """ Index Method:
# This method return the index position of a item in list.
# """
# print (numbers.index(2))
# print (numbers.index(2,0,9))

# Pass list to a function
def reverse(l):
    rev = []
    for i in l:
        rev.append(i)
    return l[: : -1]

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative


print (reverse(numbers))
print (negative_list(numbers))